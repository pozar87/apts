import ephem

class Planets:
  def __init__(self, place):
   self.planets = pd.DataFrame([
      ephem.Mercury(), 
      ephem.Venus(), 
      ephem.Mars(), 
      ephem.Jupiter(), 
      ephem.Saturn(), 
      ephem.Uranus(), 
      ephem.Neptune()], 
      columns=['Name'])
   # Compute transit of planets at given place   
   self.planets['Transit'] = self.planets[['Name']].apply(
     lambda body: Catalogs.compute_tranzit(body.Name, place), axis=1)
   # Compute altitude of planets at transit (at given place)
   self.planets['Altitude'] = self.planets[['Name', 'Transit']].apply(
     lambda body: Catalogs.altitude_at_transit(body.Name, place, body.Transit), axis=1)
        
  def get_visible(self, conditions, start, stop, hours_margin=0, sort_by=['Transit']):
    visible = self.planets
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
