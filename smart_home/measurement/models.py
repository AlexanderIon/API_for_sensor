from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor (models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=256)
    #sensor_measurem

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_measurem')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
