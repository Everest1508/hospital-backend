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
- **Body**
```json
{
  "image":"image"
}
```


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
      "price": 10.99
    },
    {
      "id": 2,
      "name": "Medicine B",
      "price": 15.99
    },
    // ... More medicines
  ]

### 8. Get Details of a Specific Room

- **Endpoint:** `/room-details/<int:room_number>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific room based on its room number.

#### Response JSON Structure:

  ```json
    {
      "room_number": 101,
      "floor": 1,
      "capacity": 2,
      "price": 50.99,
      // ... More room details
    }
  ```

### 9. Health Authentication

- **Endpoint:** `/auth/`
- **Method:** `GET`
- **Description:** Perform health authentication and retrieve data.

  #### Response JSON Structure:

  ```json
  {
    // Your response data structure
  }```

### 10. Get Room Status

- **Endpoint:** `/room-clean-status/<int:room_number>`
- **Method:** `GET`

  #### Response JSON Structure:
```json
{
  "msg":true
}
```

### 11. Get Single Patient

- **Endpoint:** `/patients/<int:id>`
- **Method:** `GET`

  #### Response JSON Structure:

```json

{
  "patient details"
}
```

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

## Logout Problem in Admin

Replace this lines in ```venv/jazzmin/template/admin/base.html``` from line number 163 to 165

```html
<a href="{% url 'admin:logout' %}" class="dropdown-item">
    <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
</a>
```

with

```html
<form action="{% url 'admin:logout' %}" method="post">
    {% csrf_token %}
    <button type="submit" class="dropdown-item">
        <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
    </button>
</form>
```

