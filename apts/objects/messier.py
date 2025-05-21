import ephem
from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place


class Messier(Objects):
  def __init__(self, place):
    super(Messier, self).__init__(place)
    self.objects = Catalogs.MESSIER.copy()
    self.compute()

  def compute(self, calculation_date=None):
    if calculation_date:
        # Instantiate as Place object
        temp_observer = Place(lat=self.place.lat_decimal, 
                              lon=self.place.lon_decimal, 
                              elevation=self.place.elevation,
                              name=self.place.name + "_temp") # Add name to avoid issues if Place requires it

        # Copy relevant attributes
        # lat, lon, elevation are set by Place constructor
        # local_timezone is determined by Place constructor based on lon/lat
        temp_observer.pressure = self.place.pressure
        temp_observer.temp = self.place.temp
        temp_observer.horizon = self.place.horizon
        
        # Set the date
        temp_observer.date = ephem.Date(calculation_date)
        
        # Recompute sun and moon for the new date
        temp_observer.sun = ephem.Sun()
        temp_observer.sun.compute(temp_observer)
        temp_observer.moon = ephem.Moon()
        temp_observer.moon.compute(temp_observer)
        
        observer_to_use = temp_observer
    else:
        observer_to_use = self.place

    # Compute transit of messier objects at given place
    self.objects[ObjectTableLabels.TRANSIT] = self.objects[[ObjectTableLabels.RA, ObjectTableLabels.DEC]].apply(
      lambda body: self._compute_tranzit(Objects.fixed_body(body.RA, body.Dec), observer_to_use), axis=1)
    # Compute altitude of messier objects at transit (at given place)
    self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
      [ObjectTableLabels.RA, ObjectTableLabels.DEC, ObjectTableLabels.TRANSIT]].apply(
      lambda body: self._altitude_at_transit(Objects.fixed_body(body.RA, body.Dec), body.Transit, observer_to_use), axis=1)
