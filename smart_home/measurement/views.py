# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, AllMesurementsOneSensor

# @api_view(['GET','POST','PUT',"DELETE"])
# def getData(request):
#     if request.method == "GET":
#         data = Sensor.objects.all()
#         ser = SensorSerializer(data, many=True)
#         print(data)
#         return Response(ser.data)
#     # elif request.method =="POST":
#     #     ser = SensorSerializer(Sensor, many=True)
"""ВЫВОД ВСЕХ ДАТЧИКОВ"""
class getData(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


"""ДОБАВЛЕНИЕ ДАТЧИКА"""
class create_sensor(APIView):
    def post(self, request):

        print("Вывод данных из post")
        text = request.data
        print(text)
        ser = SensorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)


"""ИЗменеНИЕ ДАТЧИКА"""
class change_sensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



"""ПОЛУЧИТЬ ДАННЫЕ ПО ОДНОМУ ДАТЧИКУ (имя,место установки)"""
class get_one(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class get_measurements_one_sensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AllMesurementsOneSensor



"""ДОБАВИТЬ ИЗМЕРЕНИЕ ТЕМПЕРАТУРЫ"""
class add_measurement(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self,request):
        print("ADD_TEMPER")
        ser = MeasurementSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            print(request.data)
            return Response(ser.data)

        else:
            print('Ошибка')
            return Response(ser.errors)



