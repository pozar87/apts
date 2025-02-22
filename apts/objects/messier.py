from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels


class Messier(Objects):
  def __init__(self, place):
    super(Messier, self).__init__(place)
    self.objects = Catalogs.MESSIER.copy()
    self.compute()

  def compute(self):
    # Compute transit of messier objects at given place
    self.objects[ObjectTableLabels.TRANSIT] = self.objects[[ObjectTableLabels.RA, ObjectTableLabels.DEC]].apply(
      lambda body: self._compute_tranzit(Objects.fixed_body(body.RA, body.Dec)), axis=1)
    # Compute altitude of messier objects at transit (at given place)
    self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
      [ObjectTableLabels.RA, ObjectTableLabels.DEC, ObjectTableLabels.TRANSIT]].apply(
      lambda body: self._altitude_at_transit(Objects.fixed_body(body.RA, body.Dec), body.Transit), axis=1)
