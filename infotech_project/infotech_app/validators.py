import os
from rest_framework import serializers

ALLOWED_FILE_TYPES = ['.xls', '.xlsx', '.csv']


def validate_file_type(file):
    extension = os.path.splitext(file.name)[1].lower()
    if extension not in ALLOWED_FILE_TYPES:
        raise serializers.ValidationError(
            f"Unsupported file type: {extension}. Allowed types are: {', '.join(ALLOWED_FILE_TYPES)}"
            )

def validate_data(data):
    validated_data = {}
    if not data.get("address"):
        raise serializers.ValidationError("Address is required.")
    coord = data.get("coordinates", "").replace(',', "")
    if coord:
        try:
            latitude, longitude = map(float, coord.split())
            validated_data["latitude"] = latitude
            validated_data["longitude"] = longitude
        except ValueError:
            raise serializers.ValidationError("Invalid coordinates format.")
    else:
        raise serializers.ValidationError("Coordinates are required.")
    technology = data.get("technology")
    if technology is None or (isinstance(technology, float)):
        data["technology"] = ""

    validated_data["ne"] = data["ne"]
    validated_data["address"] = data["address"]
    validated_data["latitude"] = latitude
    validated_data["longitude"] = longitude
    validated_data["gsm"] = "gsm" in data["technology"]
    validated_data["umts"] = "umts" in data["technology"]
    validated_data["lte"] = "lte" in data["technology"]
    validated_data["status"] = data["status"]

    return validated_data