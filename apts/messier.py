from .objects import Objects
from .catalogs import Catalogs

class Messier(Objects):
  def __init__(self, place):
    super(Messier, self).__init__(place)
    self.objects = Catalogs.MESSIER.copy()
    # Compute transit of messier objects at given place
    self.objects['Transit'] = self.objects[['RA', 'Dec']].apply(
        lambda body: self.compute_tranzit(Objects.fixed_body(body.RA, body.Dec)), axis=1)
    # Compute altitude of messier objects at transit (at given place)
    self.objects['Altitude'] = self.objects[['RA', 'Dec', 'Transit']].apply(
        lambda body: self.altitude_at_transit(Objects.fixed_body(body.RA, body.Dec), body.Transit), axis=1)
        
