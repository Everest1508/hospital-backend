from django.contrib import admin
from .models import *
from django import forms


class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'

    # def save(self, commit=True):
    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.status and instance.patient:
            instance.status = True
        else:
            instance.status = False

        if commit:
            instance.save()

        return instance

class BedAdmin(admin.ModelAdmin):
    form = BedForm
    
    def save_model(self, request, obj, form, change):
        if obj.patient is None:
            print("No patient provided, setting status to False")
            obj.status = False
        else:
            print("Patient provided, setting status to True")
            obj.status = True
        if obj.patient is not None:
            obj.status = True

        super().save_model(request, obj, form, change)
        

        
        

class BedInline(admin.TabularInline):
    model = Bed
    extra = 0
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)

        class CustomBedFormset(formset):
            def clean(self):
                for form in self.forms:
                    patient = form.cleaned_data.get('patient')
                    status = form.cleaned_data.get('status')
                    if not patient and status:
                        form.add_error('status', 'Status cannot be True without selecting a patient.')
                    if patient and not status:
                        form.add_error('status', 'Turn on Bed Status')

        return CustomBedFormset
    
class MedicationInline(admin.TabularInline):
    model = Medication
    extra = 0
    
class TestInline(admin.TabularInline):
    model = Test
    extra = 0
    
class RoomAdmin(admin.ModelAdmin):
    inlines = [BedInline]


class PatientAdmin(admin.ModelAdmin):
    search_fields = ["first_name","last_name"]
    inlines = [MedicationInline,TestInline]



admin.site.register(Room,RoomAdmin)
admin.site.register(Bed,BedAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Medication)
admin.site.register(Emergency)
admin.site.register(Medicine)
admin.site.register(Test)