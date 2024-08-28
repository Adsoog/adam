import os
from datetime import datetime

def rename_file(instance, filename, file_type):
    description = instance.description.replace(' ', '_') if instance.description else 'No_Description'
    station_name = instance.station.name.replace(' ', '_')
    project_name = instance.station.project.project_name.replace(' ', '_')
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Generar el nuevo nombre del archivo
    base_name, extension = os.path.splitext(filename)
    new_filename = f"{description}_{station_name}_{project_name}_{current_date}{extension}"
    
    return os.path.join(file_type, new_filename)
