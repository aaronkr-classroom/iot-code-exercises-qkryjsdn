# main.py
# 모듈확인 help('module')
from lib.room_sensor import RoomSensor

sensor1 = RoomSensor("Kitchen", 25, 44, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 350)
sensor3 = RoomSensor("Balcony", 33, 74, 150)

sensors = [sensor1, sensor2, sensor3]

comfortable_count = 0
normal_count = 0
warning_count = 0

for sensor in sensors:
    sensor.show_info()
    comfort = sensor.comfort_level()
    light = sensor.light_status()

    print(comfort)
    print(light)
    print()

    if comfort == "Comfortable":
        comfortable_count += 1
    elif comfort == "Normal":
        normal_count += 1
    elif comfort == "Warning":
        warning_count += 1

print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")
