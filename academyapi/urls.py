from django.urls import path
from .views import GrimoireList, GrimoireDetail, ApplicantList, ApplicationList, ApplicantDetail, MagicAffinityList, \
    ApplicationDetail, ApplicantWithGrimoireList

urlpatterns = [
    path("grimoire/<int:pk>/", GrimoireDetail.as_view(), name="grimoire_detail"),
    path("grimoires/", GrimoireList.as_view(), name="grimoire_list"),
    path("applicant/<int:pk>/", ApplicantDetail.as_view(), name="applicant_detail"),
    path("applicants/", ApplicantList.as_view(), name="applicant_list"),
    path("applications/", ApplicationList.as_view(), name="application_list"),
    path("application/<int:pk>", ApplicationDetail.as_view(), name="application_list"),
    path('magic_affinity/', MagicAffinityList.as_view(), name="magic_affinity_list"),
    path('applicant_with_grimoire/<int:pk>', ApplicantWithGrimoireList.as_view(), name="applicant_with_grimoire_list"),
]
