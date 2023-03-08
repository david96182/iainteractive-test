"""Common Serializers"""
import random

from rest_framework import serializers

from .custom_fields import APPLICANT_STATUS
from .models import Applicant, Grimoire, Application, MagicAffinity


class GrimoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grimoire
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        exclude = ("grimoire",)

    def create(self, data):
        applicant = Applicant.objects.create(**data)
        Application.objects.create(applicant=applicant)
        return applicant

    def update(self, instance, validated_data):
        instance.name = validated_data.get("first_name", instance.name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.identification = validated_data.get(
            "identification", instance.identification
        )
        instance.age = validated_data.get("age", instance.age)
        instance.magic_affinity = validated_data.get(
            "magic_affinity", instance.magic_affinity
        )
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['grimoire'] = GrimoireSerializer(instance.grimoire).data
        return data


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        # assign random grimoire to applicant if status is accepted
        if instance.status == "3":
            applicant = Applicant.objects.get(pk=instance.applicant.id)
            applicant.grimoire = random.choice(Grimoire.objects.all())
            applicant.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['applicant'] = ApplicantSerializer(instance.applicant).data
        data['status'] = APPLICANT_STATUS[int(instance.status)-1][1]
        return data


class MagicAffinitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MagicAffinity
        fields = '__all__'
