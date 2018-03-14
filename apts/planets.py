import ephem
import pandas 
import numpy

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
      columns=['Ephem'])
   # Add name
   self.objects['Name'] = self.objects[['Ephem']].apply(
     lambda body: body.Ephem.name, axis=1)   
   # Compute transit of planets at given place   
   self.objects['Transit'] = self.objects[['Ephem']].apply(
     lambda body: self.compute_tranzit(body.Ephem), axis=1)
   # Compute altitude of planets at transit (at given place)
   self.objects['Altitude'] = self.objects[['Ephem', 'Transit']].apply(
     lambda body: self.altitude_at_transit(body.Ephem, body.Transit), axis=1)
   # Calculate planets magnitude
   self.objects['Magnitude'] = self.objects[['Ephem']].apply(
     lambda body: body.Ephem.mag, axis=1)
   # Calculate planets RA
   self.objects['RA'] = self.objects[['Ephem']].apply(
     lambda body: numpy.degrees(body.Ephem.ra)*24/360, axis=1)
   # Calculate planets Dec
   self.objects['Dec'] = self.objects[['Ephem']].apply(
     lambda body: numpy.degrees(body.Ephem.dec), axis=1)
   # Calculate planets distance from Earth
   self.objects['Distance'] = self.objects[['Ephem']].apply(
     lambda body: body.Ephem.earth_distance, axis=1)
   # Calculate planets phase
   self.objects['Phase'] = self.objects[['Ephem']].apply(
     lambda body: body.Ephem.phase, axis=1)
     
     
     
     
         
