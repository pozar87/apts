import uuid
import numpy

from apts.utils import *
from enum import Enum


class OpticalEqipment:
    """
    Basic class for optical equipment
    """

    _SEPARATOR = "_"
    OUT = "out"
    IN = "in"

    def __init__(self, focal_length, vendor):
        self._id = str(uuid.uuid4())
        self._type = OpticalType.OPTICAL

        self.focal_length = focal_length * ureg.mm
        self.vendor = vendor

    def get_name(self):
        return str(self.__class__.__name__)

    def type(self):
        return self._type

    def label(self):
        return str(self)

    def id(self):
        return self._id

    def in_id(self, connection_type):
        return self._SEPARATOR.join([self._id, connection_type.name, self.IN])

    def out_id(self, connection_type):
        return self._SEPARATOR.join([self._id, connection_type.name, self.OUT])

    def get_parent_id(name):
        return name.split(OpticalEqipment._SEPARATOR)[0]

    def _register(self, equipment):
        # Register equipment node
        equipment.add_vertex(self.id(), self)

    def _register_output(self, equipment, connection_type=ConnectionType.F_1_25):
        # Add output node
        equipment.add_vertex(self.out_id(
            connection_type), node_type=OpticalType.OUTPUT, connection_type=connection_type)
        # Connect node to its output
        equipment.add_edge(self.id(), self.out_id(connection_type))

    def _register_input(self, equipment, connection_type=ConnectionType.F_1_25):
        # Add input node
        equipment.add_vertex(self.in_id(
            connection_type), node_type=OpticalType.INPUT, connection_type=connection_type)
        # Connect node to its input
        equipment.add_edge(self.in_id(connection_type), self.id())

    def __str__(self):
        # Format: <vendor>
        return "{} f={}".format(self.vendor, self.focal_length)


class Telescope(OpticalEqipment):
    """
    Class representing telescope
    """

    def __init__(self, aperture, focal_length, vendor="unknown telescope", connection_type=ConnectionType.F_1_25, t2_output=False):
        super(Telescope, self).__init__(focal_length, vendor)
        self.aperture = aperture * ureg.mm
        self.connection_type = connection_type
        self.t2_output = t2_output

    def speed(self):
        return self.aperture / self.focal_length

    def max_range(self):
        return 2 + 5 * numpy.log10(self.aperture.magnitude)

    def min_useful_zoom(self):
        return self.aperture / 6

    def max_useful_zoom(self):
        return self.aperture.magnitude * 2

    def register(self, equipment):
        """ 
        Register telescope in optical equipment graph. Telescope node is build out of two vertices:
        telescope node and its output. Telescope node is automatically connected with SPACE node.  
        """
        # Add telescope node
        super(Telescope, self)._register(equipment)
        # Add telescope output node and connect it to telescope
        self._register_output(equipment, self.connection_type)
        # Connect telescope node to space node
        equipment.add_edge(Constants.SPACE_ID, self.id())
        # Handling optional T2 output
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2)

    def __str__(self):
        # Format: <vendor> <aperture>/<focal length>
        return "{} {}/{}".format(self.vendor, self.aperture.magnitude, self.focal_length.magnitude)


class OutputOpticalEqipment(OpticalEqipment):

    def __init__(self, focal_length, vendor):
        super(OutputOpticalEqipment, self).__init__(focal_length, vendor)

    def exit_pupil(self, telescop, zoom):
        return telescop.aperture / zoom

    def brightness(self, telescop, zoom):
        return (self.exit_pupil(telescop, zoom) / (7 * ureg.mm))**2 * 100


class Eyepiece(OutputOpticalEqipment):
    """
    Class representing ocular
    """

    def __init__(self, focal_length, vendor="unknown ocular", field_of_view=52, connection_type=ConnectionType.F_1_25):
        super(Eyepiece, self).__init__(focal_length, vendor)
        self._connection_type = connection_type
        self._field_of_view = field_of_view * ureg.deg

    def zoom_divider(self):
        return self.focal_length

    def field_of_view(self, telescop, zoom, barlow_magnification):
        return self._field_of_view / zoom

    def output_type(self):
        return Constants.EYE_ID

    def register(self, equipment):
        """ 
        Register ocular in optical equipment graph. Ocular node is build out of two vertices:
        ocular node and its input. Ocular node is automatically connected with output IMAGE node.  
        """
        # Add ocular node
        super(Eyepiece, self)._register(equipment)
        # Add ocular input node and connect it to ocular
        self._register_input(equipment, self._connection_type)
        # Connect ocular with output eye node
        equipment.add_edge(self.id(), Constants.EYE_ID)

    def __str__(self):
        return "{} f={}".format(self.vendor, self.focal_length.magnitude)
        # Format: <vendor> f=<focal_length>


class Camera(OutputOpticalEqipment):
    """
    Class representing DSLR camera mounted via T2 adapter
    """

    def __init__(self, sensor_width, sensor_height, width, height, vendor="unknown camera", connection_type=ConnectionType.T2):
        super(Camera, self).__init__(0, vendor)
        self.connection_type = connection_type
        self.sensor_width = sensor_width * ureg.mm
        self.sensor_height = sensor_height * ureg.mm
        self.width = width
        self.height = height

    def pixel_size(self):
        return numpy.sqrt(self.sensor_width**2 + self.sensor_height**2) / math.sqrt(self.width**2 + self.height**2)

    def zoom_divider(self):
        return numpy.sqrt(self.sensor_width**2 + self.sensor_height**2)

    def field_of_view(self, telescop, zoom, barlow_magnification):
        return self.sensor_height * 3438 / (telescop.focal_length * barlow_magnification) / 60 * ureg.deg

    def output_type(self):
        return Constants.IMAGE_ID

    def register(self, equipment):
        # Add camera node
        super(Camera, self)._register(equipment)
        # Add camera input node and connect it to camera
        self._register_input(equipment, self.connection_type)
        # Connect camera with output image node
        equipment.add_edge(self.id(), Constants.IMAGE_ID)

    def __str__(self):
        # Format: <vendor> <width>x<height>
        return "{} {}x{}".format(self.vendor, self.sensor_width.magnitude, self.sensor_height.magnitude)


class Barlow(OpticalEqipment):
    """
    Class representing Barlow lenses
    """

    def __init__(self, magnification, vendor="unknown barlow", connection_type=ConnectionType.F_1_25, t2_output=False):
        super(Barlow, self).__init__(0, vendor)
        self.connection_type = connection_type
        self.t2_output = t2_output
        self.magnification = magnification

    def register(self, equipment):
        """ 
        Register barlow lens in optical equipment graph. Barlow node is build out of three vertices:
        barlow node its input and output. Ocular node is automatically connected with them.  
        """
        # Add barlow lens node
        super(Barlow, self)._register(equipment)
        # Add barlow lens output node and connect it to barlow lens
        self._register_output(equipment, self.connection_type)
        # Add barlow lens input node and connect it to barlow lens
        self._register_input(equipment, self.connection_type)
        # Handling optional T2 outpout
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2)

    def __str__(self):
        # Format: <vendor> x<magnification>
        return "{} x{}".format(self.vendor, self.magnification)
