# Healthcare Management System API

Welcome to the Healthcare Management System API. This API is designed to manage patients, rooms, medications, and more for a healthcare facility.

## Endpoints

### 1. Get List of Patients

- **Endpoint:** `/patients/`
- **Method:** `GET`
- **Description:** Retrieve a list of all patients.

### 2. Get List of Rooms with Beds

- **Endpoint:** `/room/`
- **Method:** `GET`
- **Description:** Retrieve a list of rooms with associated beds.

### 3. Discharge a Patient

- **Endpoint:** `/discharge/<int:patient_id>`
- **Method:** `GET`
- **Description:** Discharge a patient, generate a bill, and return a PDF of the bill.

### 4. Change Room Clean Status

- **Endpoint:** `/change-room-clean-status/<int:room_number>/`
- **Method:** `PATCH`
- **Description:** Toggle the clean status of a room.

### 5. Change Medication Status

- **Endpoint:** `/change-medication-status/<int:medication_id>`
- **Method:** `PATCH`
- **Description:** Toggle the status of a medication.

### 6. Add Medication for a Patient

- **Endpoint:** `/add-medication/<int:patient_id>`
- **Method:** `POST`
- **Description:** Add a medication for a specific patient.

#### Request JSON Structure:

  ```json
  {
    "medicine_id": 1,
    "timing": "Morning",
    "take": "After meal"
  }
```

### 7. Get List of Medicines

- **Endpoint:** `/medicines/`
- **Method:** `GET`
- **Description:** Retrieve a list of all medicines.

  #### Response JSON Structure:

  ```json
  [
    {
      "id": 1,
      "name": "Medicine A",
      "description": "Description of Medicine A",
      "price": 10.99
    },
    {
      "id": 2,
      "name": "Medicine B",
      "description": "Description of Medicine B",
      "price": 15.99
    },
    // ... More medicines
  ]


## Running the Project

1. Clone the repository: `git clone https://github.com/Everest1508/hospital-backend.git`
2. Navigate to the project folder: `cd hospital-backend`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Dependencies

- Django
- Django REST framework
- xhtml2pdf


