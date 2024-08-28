from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from projects.models import Project
from .models import Photo, Station
from .serializers import PhotoSerializer, ProjectSerializer, StationSerializer, DocumentSerializer, AttendanceSerializer

class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class StationListView(APIView):
    def get(self, request, project_id, *args, **kwargs):
        stations = Station.objects.filter(project_id=project_id)
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

class PhotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, station_id, *args, **kwargs):
        try:
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            return Response({"error": "Station not found."}, status=status.HTTP_404_NOT_FOUND)

        # Adicional validación de datos
        if 'image' not in request.data:
            return Response({"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Agregar station_id al contexto del serializer
        serializer = PhotoSerializer(data=request.data)
        
        if serializer.is_valid():
            # Asignar la estación antes de guardar
            photo_instance = serializer.save(station=station)
            return Response(PhotoSerializer(photo_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, station_id, *args, **kwargs):
        try:
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            return Response({"error": "Station not found."}, status=status.HTTP_404_NOT_FOUND)

        # Validación adicional para asegurarse de que el archivo esté presente
        if 'file' not in request.data:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            # Asignar la estación antes de guardar
            document_instance = serializer.save(station=station)
            return Response(DocumentSerializer(document_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AttendanceUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, station_id, *args, **kwargs):
        try:
            station = Station.objects.get(id=station_id)
        except Station.DoesNotExist:
            return Response({"error": "Station not found."}, status=status.HTTP_404_NOT_FOUND)

        # Validación adicional para asegurarse de que el archivo esté presente
        if 'attendance_record' not in request.data:
            return Response({"error": "No attendance record provided."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AttendanceSerializer(data=request.data)
        
        if serializer.is_valid():
            # Asignar la estación antes de guardar
            attendance_instance = serializer.save(station=station)
            return Response(AttendanceSerializer(attendance_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)