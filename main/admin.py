from django.contrib import admin
from .models import Inquiry, Contact, ServiceInquiry , ScheduleContact

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    # Optional: Display full message in detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    
@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'created_at')
    search_fields = ('name', 'email', 'phone', 'service')
    list_filter = ('service', 'created_at')
    
@admin.register(ScheduleContact)
class ScheduleContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'subject', 'message')