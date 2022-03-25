from django.urls import path

from measurement.views import getData, get_one, create_sensor, add_measurement, change_sensor, \
    get_measurements_one_sensor

urlpatterns = [
    path('data/', getData.as_view()),
    path('add_sensor/', create_sensor.as_view()),
    path('data/<pk>/', get_one.as_view()),
    path('add_temper/', add_measurement.as_view()),
    path("show_measurement/", add_measurement.as_view()),
    path('change/<pk>/', change_sensor.as_view()),
    path('measurements/<pk>', get_measurements_one_sensor.as_view())
    # TODO: зарегистрируйте необходимые маршруты

]