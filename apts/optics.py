import operator
import functools

class Optics:

  def compute_zoom(path):
    #First item in the path should be the telescope
    telescop = path[0]
    #Last item in the path should be ocular #TODO: handle camera also
    okular = path[-1]
    #Barlow lenses are in the middle 
    barlows = [item.magnification for item in path[1:-1]]
    #Multiply all barlows 
    magnification = functools.reduce(operator.mul, barlows, 1)
    zoom = telescop.focal_length * magnification / okular.focal_length
    return zoom

