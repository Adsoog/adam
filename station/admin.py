from django.contrib import admin
from .models import Station, Photo, Document, Attendance

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('station', 'description', 'uploaded_at')
    list_filter = ('station', 'uploaded_at')
    search_fields = ('description',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('station', 'description', 'uploaded_at')
    list_filter = ('station', 'uploaded_at')
    search_fields = ('description',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('station', 'description', 'uploaded_at')
    list_filter = ('station', 'uploaded_at')
    search_fields = ('description',)

admin.site.register(Station)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
