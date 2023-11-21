from django.contrib import admin
from ctf.models import *


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    list_filter = ("created_at",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_id", "name", "created_at")
    list_filter = ("created_at",)


@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):
    list_display = ("team", "team_broken", "updated_at", "status")
    list_filter = ("created_at", "team")