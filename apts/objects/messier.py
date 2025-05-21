import ephem
from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels


class Messier(Objects):
  def __init__(self, place):
    super(Messier, self).__init__(place)
    self.objects = Catalogs.MESSIER.copy()
    self.compute()

  def compute(self, calculation_date=None):
    if calculation_date:
        temp_observer = ephem.Observer()
        temp_observer.lat = self.place.lat
        temp_observer.lon = self.place.lon
        temp_observer.elevation = self.place.elevation
        temp_observer.pressure = self.place.pressure
        temp_observer.temp = self.place.temp
        temp_observer.horizon = self.place.horizon
        temp_observer.date = ephem.Date(calculation_date)
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
