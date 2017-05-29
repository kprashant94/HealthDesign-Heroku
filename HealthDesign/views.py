from django.shortcuts import render, get_object_or_404
from .forms import DemographicsForm, GuardianForm, ProviderForm, ImmunizationsForm, CarePlanForm, ProblemListForm, ProceduresForm, AllergiesForm, MedicationForm, EncountersForm
from .models import Demographics, Guardian, Provider, Immunizations, CarePlan, Encounters,Allergies,Medication, Procedures, ProblemList
from django.db.models import Q


def index(request):
    demographics_list = Demographics.objects.all()
    query = request.GET.get("q")
    if query:
        demographics_list = demographics_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).distinct()
    return render(request, 'HealthDesign/index.html', {'demographics_list': demographics_list})


def detail(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def demographics_create(request):
    form = DemographicsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        demographics = form.save(commit=False)
        demographics.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
    }
    return render(request, 'HealthDesign/demographics_form.html', context)

def demographics_update(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = DemographicsForm(request.POST or None, request.FILES or None, instance=demographics)
    if form.is_valid():
        demographics = form.save(commit=False)
        demographics.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
    }
    return render(request, 'HealthDesign/demographics_form.html', context)

def demographics_delete(request, demographics_id):
    get_object_or_404(Demographics, pk=demographics_id).delete()
    demographics_list = Demographics.objects.all()
    return render(request, 'HealthDesign/index.html', {'demographics_list': demographics_list})

def guardian_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = GuardianForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        guardian = form.save(commit=False)
        guardian.demographics = demographics
        guardian.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/guardian_form.html', context)

def guardian_update(request, demographics_id, guardian_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    guardian = get_object_or_404(Guardian, pk=guardian_id)
    form = GuardianForm(request.POST or None, request.FILES or None, instance=guardian)
    if form.is_valid():
        guardian = form.save(commit=False)
        guardian.demographics = demographics
        guardian.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/guardian_form.html', context)

def guardian_delete(request, demographics_id, guardian_id):
    get_object_or_404(Guardian, pk=guardian_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def provider_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = ProviderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        provider = form.save(commit=False)
        provider.demographics = demographics
        provider.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/provider_form.html', context)

def provider_update(request, demographics_id, provider_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    provider = get_object_or_404(Provider, pk=provider_id)
    form = ProviderForm(request.POST or None, request.FILES or None, instance=provider)
    if form.is_valid():
        provider = form.save(commit=False)
        provider.demographics = demographics
        provider.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/provider_form.html', context)

def provider_delete(request, demographics_id, provider_id):
    get_object_or_404(Provider, pk=provider_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def allergies_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = AllergiesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        allergy = form.save(commit=False)
        allergy.demographics = demographics
        allergy.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/allergies_form.html', context)

def allergies_update(request, demographics_id, allergies_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    allergy = get_object_or_404(Allergies, pk=allergies_id)
    form = AllergiesForm(request.POST or None, request.FILES or None, instance=allergy)
    if form.is_valid():
        allergy = form.save(commit=False)
        allergy.demographics = demographics
        allergy.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/allergies_form.html', context)

def allergies_delete(request, demographics_id, allergies_id):
    get_object_or_404(Allergies, pk=allergies_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def immunizations_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = ImmunizationsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        immunization = form.save(commit=False)
        immunization.demographics = demographics
        immunization.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/immunizations_form.html', context)

def immunizations_update(request, demographics_id, immunizations_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    immunization = get_object_or_404(Immunizations, pk=immunizations_id)
    form = ImmunizationsForm(request.POST or None, request.FILES or None, instance=immunization)
    if form.is_valid():
        immunization = form.save(commit=False)
        immunization.demographics = demographics
        immunization.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/immunizations_form.html', context)

def immunizations_delete(request, demographics_id, immunizations_id):
    get_object_or_404(Immunizations, pk=immunizations_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def medication_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = MedicationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        medication = form.save(commit=False)
        medication.demographics = demographics
        medication.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/medication_form.html', context)

def medication_update(request, demographics_id, medication_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    medication = get_object_or_404(Medication, pk=medication_id)
    form = MedicationForm(request.POST or None, request.FILES or None, instance=medication)
    if form.is_valid():
        medication = form.save(commit=False)
        medication.demographics = demographics
        medication.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/medication_form.html', context)

def medication_delete(request, demographics_id, medication_id):
    get_object_or_404(Medication, pk=medication_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def careplan_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = CarePlanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        careplan = form.save(commit=False)
        careplan.demographics = demographics
        careplan.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/careplan_form.html', context)

def careplan_update(request, demographics_id, careplan_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    careplan = get_object_or_404(CarePlan, pk=careplan_id)
    form = CarePlanForm(request.POST or None, request.FILES or None, instance=careplan)
    if form.is_valid():
        careplan = form.save(commit=False)
        careplan.demographics = demographics
        careplan.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/careplan_form.html', context)

def careplan_delete(request, demographics_id, careplan_id):
    get_object_or_404(CarePlan, pk=careplan_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})


def encounters_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = EncountersForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        encounter = form.save(commit=False)
        encounter.demographics = demographics
        encounter.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/encounters_form.html', context)

def encounters_update(request, demographics_id, encounters_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    encounter = get_object_or_404(Encounters, pk=encounters_id)
    form = EncountersForm(request.POST or None, request.FILES or None, instance=encounter)
    if form.is_valid():
        encounter = form.save(commit=False)
        encounter.demographics = demographics
        encounter.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/encounters_form.html', context)

def encounters_delete(request, demographics_id, encounters_id):
    get_object_or_404(Encounters, pk=encounters_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def problemlist_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = ProblemListForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        problemlist = form.save(commit=False)
        problemlist.demographics = demographics
        problemlist.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/problemlist_form.html', context)

def problemlist_update(request, demographics_id, problemlist_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    problemlist = get_object_or_404(ProblemList, pk=problemlist_id)
    form = ProblemListForm(request.POST or None, request.FILES or None, instance=problemlist)
    if form.is_valid():
        problemlist = form.save(commit=False)
        problemlist.demographics = demographics
        problemlist.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/problemlist_form.html', context)

def problemlist_delete(request, demographics_id, problemlist_id):
    get_object_or_404(ProblemList, pk=problemlist_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})

def procedures_create(request, demographics_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    form = ProceduresForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        procedure = form.save(commit=False)
        procedure.demographics = demographics
        procedure.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/procedures_form.html', context)

def procedures_update(request, demographics_id, procedures_id):
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    procedure = get_object_or_404(Procedures, pk=procedures_id)
    form = ProceduresForm(request.POST or None, request.FILES or None, instance=procedure)
    if form.is_valid():
        procedure = form.save(commit=False)
        procedure.demographics = demographics
        procedure.save()
        return render(request, 'HealthDesign/detail.html', {'demographics': demographics})
    context = {
        "form": form,
        "demographics": demographics
    }
    return render(request, 'HealthDesign/procedures_form.html', context)

def procedures_delete(request, demographics_id, procedures_id):
    get_object_or_404(Procedures, pk=procedures_id).delete()
    demographics = get_object_or_404(Demographics, pk=demographics_id)
    return render(request, 'HealthDesign/detail.html', {'demographics': demographics})