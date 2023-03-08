from rest_framework import generics, status
from rest_framework.response import Response

from .models import Grimoire, Applicant, Application, MagicAffinity
from .serializers import GrimoireSerializer, ApplicantSerializer, ApplicationSerializer, MagicAffinitySerializer


class GrimoireList(generics.ListCreateAPIView):
    queryset = Grimoire.objects.all()
    serializer_class = GrimoireSerializer


class GrimoireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grimoire.objects.all()
    serializer_class = GrimoireSerializer


class ApplicantList(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def delete(self, request, pk=None):
        application = Application.objects.get(pk=pk)
        applicant = Applicant.objects.get(application=application)
        applicant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MagicAffinityList(generics.ListCreateAPIView):
    queryset = MagicAffinity.objects.all()
    serializer_class = MagicAffinitySerializer


class ApplicantWithGrimoireList(generics.ListAPIView):
    queryset = Applicant.objects.filter(grimoire=1)
    serializer_class = ApplicantSerializer

    def get_queryset(self, pk):
        queryset = Applicant.objects.filter(grimoire=pk)
        return queryset

    # get applicants with X grimnoire
    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = ApplicantSerializer(queryset, many=True)
        return Response(serializer.data)
