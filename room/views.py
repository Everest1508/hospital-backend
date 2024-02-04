from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import PatientSerializer, RoomSerializer,RoomWithBedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import F,Sum,FloatField
from django.utils import timezone
from django.template.loader import get_template
from django.template import Context
from datetime import datetime, time
from xhtml2pdf import pisa


class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class RoomStatusView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomWithBedAPIView(APIView):
    def get(self, request, format=None):
        try:
            room = Room.objects.all()
            serializer = RoomWithBedSerializer(room, many=True)
            return Response(serializer.data)
        except:
            return Response({"msg": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        
class RoomCleanStatusAPIView(APIView):
    def patch(self, request, room_number):
        # Retrieve room
        room = get_object_or_404(Room, room_number=room_number)

        # Toggle clean status
        room.clean_status = not room.clean_status
        room.save()

        return Response({"msg": f"Room {room_number} clean status updated successfully."},
                        status=status.HTTP_200_OK)


class MedicationStatusAPIView(APIView):
    def patch(self, request, medication_id):
        # Retrieve medication
        medication = get_object_or_404(Medication, id=medication_id)

        # Toggle medication status
        medication.status = not medication.status
        medication.save()

        return Response({"msg": f"Medication status toggled successfully."},
                        status=status.HTTP_200_OK)

class AddMedicationAPIView(APIView):
    def post(self, request, patient_id):

        patient = get_object_or_404(Patient, id=patient_id)

        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            medicine_id = serializer.validated_data.get('medicine_id')

            medicine = get_object_or_404(Medicine, id=medicine_id)

            medication = Medication.objects.create(
                medicine=medicine,
                timing=serializer.validated_data.get('timing'),
                take=serializer.validated_data.get('take'),
                patient=patient
            )

            return Response({"msg": "Medication added successfully."},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class DischargePatientAPIView(APIView):
    def get(self, request, patient_id):

        patient = get_object_or_404(Patient, id=patient_id)

        if patient.discharge:
            return JsonResponse({"msg": "Patient is already discharged."}, status=status.HTTP_400_BAD_REQUEST)

        admission_datetime = timezone.make_aware(datetime.combine(patient.admission_date, time.min))
        days_admitted = (timezone.now() - admission_datetime).days
        medications = Medication.objects.filter(patient=patient).select_related('medicine')

        tests = Test.objects.filter(patient=patient)

        medication_bill = medications.aggregate(total=Sum(F('medicine__price') * days_admitted, output_field=FloatField()))['total'] or 0
        room_price = Room.objects.get(id=patient.bed.room.id).price * days_admitted
        nursing_charges = 50
        test_charges = tests.aggregate(total=Sum(F('bill'), output_field=FloatField()))['total'] or 0
        total_bill = medication_bill + room_price + nursing_charges + test_charges

        # Generate PDF
        template = get_template('bill_template.html')
        context = {
            'patient': patient,
            'days_admitted': days_admitted,
            'medications': medications,
            'tests': tests,  
            'medication_bill': medication_bill,
            'room_price': room_price,
            'nursing_charges': nursing_charges,
            'test_charges': test_charges, 
            'total_bill': total_bill,
        }
        html_content = template.render(context, request)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{patient.first_name}_{patient.last_name}_bill.pdf"'
        pisa_status = pisa.CreatePDF(html_content, dest=response)

        if pisa_status.err:
            return JsonResponse({"msg": "Error generating PDF."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        patient.discharge = True
        patient.save()

        bed = patient.bed
        bed.status = False
        bed.patient = None
        bed.save()

        return response