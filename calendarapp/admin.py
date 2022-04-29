from django.contrib import admin
from calendarapp.models import (Event, EventMember, Routine, DailyRoutine)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
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
    list_display = ["event", "user", "created_at", "updated_at", "id"]
    list_filter = ["event"]


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at", "id"]
    list_filter = ["name"]
    search_fields = ["name"]

    # filters routines by logged in user // for autocomplete - not for dropdown
    def get_search_results(self, request, queryset, search_term):
        results = super().get_search_results(request, queryset, search_term)
        queryset = self.model.objects.filter(user=request.user)
        return queryset, results


@admin.register(DailyRoutine)
class DailyRoutineAdmin(admin.ModelAdmin):
    list_display = ["date", "routine", "get_user"]
    autocomplete_fields = ["routine"]

    # filters routines by logged in user // for dropdown - not for autocomplete
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "routine":
            kwargs["queryset"] = Routine.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
