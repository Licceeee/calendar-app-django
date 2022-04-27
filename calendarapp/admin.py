from django.contrib import admin
from calendarapp.models import (Event, EventMember, Routine)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = [
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
        "id",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ["event", "user", "created_at", "updated_at", "id"]
    list_filter = ["event"]


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    model = Routine
    list_display = ["id", "name", "user", "created_at", "updated_at", "id"]
    list_filter = ["name"]
