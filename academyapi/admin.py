from django.contrib import admin
from .models import Applicant, Application, Grimoire, MagicAffinity

admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Grimoire)
admin.site.register(MagicAffinity)
