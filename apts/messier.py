from datetime import timedelta

from .catalogs import Catalogs

class Messier:
  def __init__(self, place):
    self.objects = Catalogs.MESSIER.copy()
    # Compute transit of messier objects at given place
    self.objects['Transit'] = self.objects[['RA', 'Dec']].apply(
        lambda body: Catalogs.compute_tranzit(Catalogs.fixed_body(body.RA, body.Dec), place), axis=1)
    # Compute altitude of messier objects at transit (at given place)
    self.objects['Altitude'] = self.objects[['RA', 'Dec', 'Transit']].apply(
        lambda body: Catalogs.altitude_at_transit(Catalogs.fixed_body(body.RA, body.Dec), place, body.Transit), axis=1)
        
  def get_visible(self, conditions, start, stop, hours_margin=0, sort_by=['Transit']):
    visible = self.objects
    visible = visible[
        # Filter objects by they transit
        (visible.Transit > start - timedelta(hours=hours_margin)) &
        (visible.Transit < stop + timedelta(hours=hours_margin)) &
        # Filter objects by they min altitude at transit
        (visible.Altitude > conditions.MIN_OBJECT_ALTITUDE) &
        # Filter object by they magnitude
        (visible.Magnitude < conditions.MAX_OBJECT_MAGNITUDE)]
    # Sort objects by given order    
    visible = visible.sort_values(sort_by, ascending=[1])    
    return visible    


