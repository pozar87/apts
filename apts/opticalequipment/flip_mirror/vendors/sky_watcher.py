from ..base import FlipMirror


class SkyWatcherFlipMirror(FlipMirror):
    _DATABASE = {
        "Sky_Watcher_Flip_Mirror": {
            "brand": "Sky-Watcher",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 470,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sky_Watcher_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Flip_Mirror"])
