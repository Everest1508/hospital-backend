from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('patients/',PatientListView.as_view() ),
    path('patients/<int:id>/',PatientAPIView.as_view() ),
    path('room/',RoomWithBedAPIView.as_view() ),
    path('discharge/<int:patient_id>/',DischargePatientAPIView.as_view()),
    path('change-room-clean-status/<int:room_number>/', RoomCleanStatusAPIView.as_view(), name='change-room-clean-status'),
    path('room-clean-status/<int:room_number>/', RoomCleanStatusAPIView.as_view(), name='room-clean-status'),
    path('change-medication-status/<int:medication_id>/',MedicationStatusAPIView.as_view(),name="change-medication-status"),
    path('get-medicines/',MedicineListView.as_view(),name="get-medicines"),
    path('room-details/<int:room_number>/', RoomDetailsView.as_view(), name='room-details'),
    path('auth/', AuthApiView.as_view(), name='auth-api'),
    path('add-medicine/<int:patient_id>/<int:medicine_id>/', AddMedicationAPIView.as_view(), name='add-medicine'),
    path('get-medicine/', MedicineListView.as_view(), name='add-medicine'),
]
