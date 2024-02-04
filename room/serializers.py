# serializers.py
from rest_framework import serializers
from .models import Emergency, Patient, Bed, Room, Medication,Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
        
class MedicationSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer()
    class Meta:
        model = Medication
        fields = "__all__"

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    emergency_contact = EmergencySerializer()
    medication = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient
        fields = ["id","first_name","last_name","blood_group"
                  ,"date_of_birth","gender","age"
                  ,"medical_history","emergency_contact"
                  ,"admission_date","attending_physician"
                  ,"attending_nurse","medication"]
        
    def get_medication(self, obj):
        medications = Medication.objects.filter(patient=obj)
        return MedicationSerializer(medications, many=True).data

class BedSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = Bed
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    bed = BedSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class RoomWithBedSerializer(serializers.ModelSerializer):
    bed = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ["id","room_number","bed"]
        
    def get_bed(self, obj):
        beds = Bed.objects.filter(room=obj)
        return BedSerializer(beds, many=True).data