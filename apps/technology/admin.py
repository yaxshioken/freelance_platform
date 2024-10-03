from django.contrib import admin

from apps.technology.models import Profession, Technology


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass
@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass
