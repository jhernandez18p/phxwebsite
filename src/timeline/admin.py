from django.contrib import admin
from .models import Timeline

# Register your models here.
@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    search_fields = ['es_name',]
    list_display = (
                    'es_name',
                )
    class Meta:
        model = Timeline