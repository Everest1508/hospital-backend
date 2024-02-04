from django.db import models

# Create your models here.
class Emergency(models.Model):
    name = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    
    def __str__(self):
        return self.name +" -- "+self.relation


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    medical_history = models.TextField(null=True)
    emergency_contact = models.ForeignKey(Emergency,on_delete=models.CASCADE)
    admission_date = models.DateField(auto_now=False, auto_now_add=False)
    attending_physician = models.CharField(max_length=50)
    attending_nurse = models.CharField(max_length=50)
    discharge = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name +" "+self.last_name+" -- Physician : "+self.attending_physician
    
    def delete(self, using=None, keep_parents=False):
        associated_bed = Bed.objects.filter(patient=self)

        super().delete(using=using, keep_parents=keep_parents)

        if associated_bed.exists():
            bed = associated_bed.first()
            bed.status = False
            bed.save()

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return self.medicine_name+"---"+str(self.price)+"rs"


class Medication(models.Model):
    medicine= models.ForeignKey(Medicine,on_delete=models.SET_NULL,null=True)
    timing=models.CharField(max_length=30,choices=(("morning","Morning"),("afternoon","Afternoon"),("evening","Evening")),null=True)
    take = models.CharField(max_length=30,choices=(("after","After Meal"),("before","Before Meal")),null=True)
    status = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.patient.first_name+" "+self.patient.last_name+" Medications"

class Test(models.Model):
    test_name = models.CharField(max_length=50,choices=(("MRI","MRI"),("Blood Test","Blood Test")))
    status = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)
    bill = models.FloatField(null=True)
    
    def __str__(self):
        return self.patient.first_name+" "+self.patient.last_name+" Test"

class Room(models.Model):
    room_number = models.IntegerField(null=True)
    clean_status = models.BooleanField(default=False)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return "Room No. "+str(self.room_number)


class Bed(models.Model):    
    bed_no = models.IntegerField(null=True,unique=True)
    status = models.BooleanField(default=False)
    patient = models.OneToOneField(Patient,on_delete=models.SET_NULL,null=True,blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return "Bed No. "+str(self.bed_no) +"-"+ ("Occupied" if self.status else "Vacant")