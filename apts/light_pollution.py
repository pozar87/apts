from PIL import Image
from importlib import resources

class LightPollution:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.image_path = str(resources.files("apts").joinpath("data/world202t4_low3.png"))
        self.im = Image.open(self.image_path)
        self.pix = self.im.load()

    def _latlon_to_pixel(self, lat, lon):
        # Image dimensions: 14400x5600
        # Latitude range: 75N to 65S -> 140 degrees
        # Longitude range: 180W to 180E -> 360 degrees
        img_width, img_height = self.im.size

        # Normalize longitude to 0-360
        lon_norm = lon + 180
        x = int((lon_norm / 360) * img_width)

        # Normalize latitude to 0-140 (from 75 to -65)
        lat_norm = 75 - lat
        y = int((lat_norm / 140) * img_height)

        return x, y

    def get_light_pollution(self):
        x, y = self._latlon_to_pixel(self.lat, self.lon)
        
        if self.pix is None:
            return -1

        palette_index = self.pix[x, y]

        if not isinstance(palette_index, int):
            return -1

        # This mapping is based on the key.png from the data source
        # and the palette extracted from the image.
        bortle_scale = {
            0: 1,  # Dark Grey
            1: 1,  # Grey
            2: 1,  # Black
            3: 2,  # Dark Blue
            4: 3,  # Blue
            5: 4,  # Dark Green
            6: 4.5, # Green
            7: 5,  # Olive
            8: 6,  # Yellow
            9: 7,  # Brown/Orange
            10: 7, # Orange
            11: 8, # Dark Red
            12: 8, # Red
            13: 9, # Light Grey
            14: 9  # White
        }

        return bortle_scale.get(palette_index, -1)
