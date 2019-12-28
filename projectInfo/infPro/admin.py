from django.contrib import admin

from .models import ProjectInformation, ProductionProjectInformation

admin.site.register(ProjectInformation)
admin.site.register(ProductionProjectInformation)

# Register your models here.
