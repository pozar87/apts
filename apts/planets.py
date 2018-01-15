import ephem
import pandas 

from .objects import Objects

class Planets(Objects):
  def __init__(self, place):
   super(Planets, self).__init__(place)
   # Init object list with all planets
   self.objects = pandas.DataFrame([
      ephem.Mercury(), 
      ephem.Venus(), 
      ephem.Mars(), 
      ephem.Jupiter(), 
      ephem.Saturn(), 
      ephem.Uranus(), 
      ephem.Neptune()], 
      columns=['Name'])
   # Compute transit of planets at given place   
   self.objects['Transit'] = self.objects[['Name']].apply(
     lambda body: self.compute_tranzit(body.Name), axis=1)
   # Compute altitude of planets at transit (at given place)
   self.objects['Altitude'] = self.objects[['Name', 'Transit']].apply(
     lambda body: self.altitude_at_transit(body.Name, body.Transit), axis=1)
   # Calculate planets magnitude
   self.objects['Magnitude'] = self.objects[['Name']].apply(
     lambda body: body.Name.mag, axis=1)
     
     
     
         
