from django.contrib import admin
from .models import Skill, contactmessage, StudentProfile
admin.site.register(Skill)
admin.site.register(StudentProfile)
@admin.register(contactmessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)

# Register your models here.
