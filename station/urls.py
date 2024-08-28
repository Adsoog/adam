from django.urls import path
from .views import ProjectListView, StationListView, PhotoUploadView, DocumentUploadView, AttendanceUploadView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list_api'),
    path('projects/<int:project_id>/stations/', StationListView.as_view(), name='station_list_api'),
    path('photos/<int:station_id>/upload/', PhotoUploadView.as_view(), name='photo_upload_api'),
    path('document/<int:station_id>/upload/', DocumentUploadView.as_view(), name='document_upload_api'),
    path('attendance/<int:station_id>/upload/', AttendanceUploadView.as_view(), name='attendance_upload_api'),
]
