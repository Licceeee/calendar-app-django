from django.contrib import admin
from calendarapp.models import Event, EventMember


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]