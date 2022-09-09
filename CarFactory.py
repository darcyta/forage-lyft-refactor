from Car import Car
from Engine.CapuletEngine import CapuletEngine
from Engine.SternmanEngine import SternmanEngine
from Engine.WilloughbyEngine import WilloughbyEngine
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery

class CarFactory():
  def create_callope(current_date, last_service_date, current_milage, last_service_milage):
    return Car(CapuletEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date,current_date))

  def create_glissade(current_date, last_service_date, current_milage, last_service_milage):
    return Car(WilloughbyEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date,current_date))
  
  def create_palindrome(current_date, last_service_date, warning_light_on):
    return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

  def create_rorschach(current_date, last_service_date, current_milage, last_service_milage):
    return Car(WilloughbyEngine(last_service_milage, current_milage), NubbinBattery(last_service_date,current_date))

  def create_thovex(current_date, last_service_date, current_milage, last_service_milage):
    return Car(CapuletEngine(last_service_milage, current_milage), NubbinBattery(last_service_date,current_date))

