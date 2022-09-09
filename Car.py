from abc import ABC, abstractmethod

class Car(ABC):
  def __init__(self, engine, battery):
    self.engine = engine
    self.battery = battery

  @abstractmethod
  def needs_service(self):
    return self.engine.needs_service() and self.battery.needs_service()