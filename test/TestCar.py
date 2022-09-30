import unittest
from datetime import datetime

from CarFactory import CarFactory

class TestCallope(unittest.TestCase):
  def test_battery_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 3 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_callope( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_battery_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 1 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_callope( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

  def test_engine_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 30001
    last_service_milage = 0

    car = CarFactory.create_callope( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_engine_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 30000
    last_service_milage = 0

    car = CarFactory.create_callope( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

class TestGlissade(unittest.TestCase):
  def test_battery_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 3 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_glissade( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_battery_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 1 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_glissade( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

  def test_engine_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 60001
    last_service_milage = 0

    car = CarFactory.create_glissade( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_engine_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 60000
    last_service_milage = 0

    car = CarFactory.create_glissade( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

class TestPalindrome(unittest.TestCase):
  def test_battery_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 3 )
    warning_light_on = False

    car = CarFactory.create_palindrome( today, last_service_date, warning_light_on )
    self.assertTrue( car.needs_service() )

  def test_battery_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 1 )
    warning_light_on = False

    car = CarFactory.create_palindrome( today, last_service_date, warning_light_on )
    self.assertFalse( car.needs_service() )

  def test_engine_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    warning_light_on = True

    car = CarFactory.create_palindrome( today, last_service_date, warning_light_on )
    self.assertTrue( car.needs_service() )

  def test_engine_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    warning_light_on = False

    car = CarFactory.create_palindrome( today, last_service_date, warning_light_on )
    self.assertFalse( car.needs_service() )

class TestRorschach(unittest.TestCase):
  def test_battery_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 5 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_rorschach( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_battery_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 3 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_rorschach( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

  def test_engine_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 60001
    last_service_milage = 0

    car = CarFactory.create_rorschach( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_engine_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 60000
    last_service_milage = 0

    car = CarFactory.create_rorschach( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

class TestThovex(unittest.TestCase):
  def test_battery_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 5 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_thovex( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_battery_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today.replace( year=today.year - 3 )
    current_milage = 0
    last_service_milage = 0

    car = CarFactory.create_thovex( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

  def test_engine_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 30001
    last_service_milage = 0

    car = CarFactory.create_thovex( today, last_service_date, current_milage, last_service_milage )
    self.assertTrue( car.needs_service() )

  def test_engine_not_needs_service( self ):
    today = datetime.today().date()
    last_service_date = today
    current_milage = 30000
    last_service_milage = 0

    car = CarFactory.create_thovex( today, last_service_date, current_milage, last_service_milage )
    self.assertFalse( car.needs_service() )

if __name__ == '__main__':
    unittest.main()