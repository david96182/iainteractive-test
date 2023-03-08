from django.db import models
from .custom_fields import APPLICANT_STATUS
from .validators import validate_age, validate_letters_only


class Grimoire(models.Model):
    name = models.CharField(max_length=30)
    leaves = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.leaves} leave(s) clover"


class MagicAffinity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Applicant(models.Model):
    name = models.CharField(max_length=20, validators=[validate_letters_only])
    last_name = models.CharField(max_length=20, validators=[validate_letters_only])
    identification = models.CharField(max_length=10)
    age = models.SmallIntegerField(validators=[validate_age])
    magic_affinity = models.ForeignKey(MagicAffinity, on_delete=models.CASCADE)
    grimoire = models.ForeignKey(Grimoire, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.magic_affinity}"


class Application(models.Model):
    status = models.CharField(max_length=1, choices=APPLICANT_STATUS, default='1')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.applicant.name} {self.applicant.last_name}: {APPLICANT_STATUS[int(self.status)-1][1]}"
