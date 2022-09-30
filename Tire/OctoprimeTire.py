from Tire.Tire import Tire

class OctoprimeTire(Tire):
  def __init__(self, tire_array):
    self.tire_array = tire_array

  def needs_service(self):
    tire_sum = 0
    for tire in self.tire_array:
      tire_sum += tire
    return tire_sum >= 3