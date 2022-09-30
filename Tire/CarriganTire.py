from Tire.Tire import Tire

class CarriganTire(Tire):
  def __init__(self, tire_array):
    self.tire_array = tire_array

  def needs_service(self):
    needs_service = False
    for tire in self.tire_array:
      if tire >= 0.9:
        needs_service = True
    return needs_service