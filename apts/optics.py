import operator
import functools
import math

class Optics:
  def _expand(path):
    #First item in the path should be the telescope
    telescop = path[0]
    #Last item in the path is output
    output = path[-1]
    #Barlow lenses are in the middle 
    barlows = [item.magnification for item in path[1:-1]]
    return (telescop, barlows, output)

  def compute_zoom(path):
    #First item in the path should be the telescopem second barows lenses and finally ocular
    telescop, barlows, okular = Optics._expand(path)
    #Multiply all barlows 
    magnification = functools.reduce(operator.mul, barlows, 1)
    zoom = telescop.focal_length * magnification / okular.focal_length
    return zoom

  def compute_camera_zoom(path):
    #First item in the path should be the telescopem second barows lenses and finally camera
    telescop, barlows, camera = Optics._expand(path)
    #Multiply all barlows
    magnification = functools.reduce(operator.mul, barlows, 1)
    zoom = telescop.focal_length * magnification / math.sqrt(camera.sensor_width**2 + camera.sensor_height**2)
    return zoom

