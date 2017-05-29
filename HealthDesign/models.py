from django.db import models
from django.core.urlresolvers import reverse


class Demographics(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    martial_status = models.CharField(max_length=10)
    religious_affiliation = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=30)
    language_spoken = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    birthday = models.DateField()


class Guardian(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

class Provider(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

class Allergies(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    allergy_name = models.CharField(max_length=50)
    reaction = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)

class Immunizations(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    date = models.DateField()
    immunizations_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    dose_quantity = models.CharField(max_length=50)
    instructions = models.CharField(max_length=100)


class Medication(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=50)
    medication_name = models.CharField(max_length=50)
    instructions = models.CharField(max_length=100)
    dose_quantity = models.CharField(max_length=50)
    rate_quantity = models.CharField(max_length=50)
    prescriber_name = models.CharField(max_length=50)

class CarePlan(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField()
    instructions = models.CharField(max_length=100)

class Encounters(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    encounter = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField()


class ProblemList(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    observation = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    date = models.DateField()
    comment = models.CharField(max_length=100)


class Procedures(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    procedure = models.CharField(max_length=50)
    date = models.DateField()
    provider = models.CharField(max_length=50)
    location = models.CharField(max_length=100)






