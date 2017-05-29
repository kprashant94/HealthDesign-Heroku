from django import forms
from django.contrib.auth.models import User

from .models import Demographics, Guardian, Provider, Allergies, Immunizations, Medication, ProblemList, CarePlan, Encounters, Procedures


class DemographicsForm(forms.ModelForm):
    class Meta:
        model = Demographics
        fields = ['first_name', 'last_name', 'gender', 'martial_status', 'religious_affiliation',
                  'ethnicity',
                  'language_spoken',
                  'address',
                  'telephone',
                  'birthday'
                  ]


class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'role', 'address', 'telephone']


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', 'address', 'telephone' ]

class AllergiesForm(forms.ModelForm):
    class Meta:
        model = Allergies
        fields = ['allergy_name', 'reaction', 'severity']


class ImmunizationsForm(forms.ModelForm):
    class Meta:
        model = Immunizations
        fields = ['date', 'immunizations_name', 'type', 'dose_quantity', 'instructions']

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['date', 'type', 'medication_name', 'instructions', 'dose_quantity', 'rate_quantity', 'prescriber_name']

class CarePlanForm(forms.ModelForm):
    class Meta:
        model = CarePlan
        fields = ['name', 'date', 'instructions']

class EncountersForm(forms.ModelForm):
    class Meta:
        model = Encounters
        fields = ['encounter', 'provider', 'location', 'date']

class ProblemListForm(forms.ModelForm):
    class Meta:
        model = ProblemList
        fields = ['observation', 'status', 'date', 'comment']


class ProceduresForm(forms.ModelForm):
    class Meta:
        model = Procedures
        fields = ['procedure', 'date', 'provider', 'location']
