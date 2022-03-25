from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor', 'temperature', "created_at"]



class SensorSerializer(serializers.ModelSerializer):
    # measurements = MeasurementSerializer(read_only=True,many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'discription']


class AllMesurementsOneSensor(serializers.ModelSerializer):
    sensor_measurem = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'discription', "sensor_measurem"]
