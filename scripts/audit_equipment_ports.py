import importlib
import inspect
import os

from apts.opticalequipment.abstract import OpticalEquipment
from apts.opticalequipment.camera.base import Camera
from apts.opticalequipment.eyepiece.base import Eyepiece
from apts.opticalequipment.telescope.base import Telescope
from apts.utils import get_default_gender, map_conn, map_gender


def audit():
    vmods = []
    for r, _, fs in os.walk("apts/opticalequipment"):
        if "vendors" in r:
            for f in fs:
                if f.endswith(".py") and f != "__init__.py":
                    vmods.append(
                        os.path.relpath(os.path.join(r, f), ".")
                        .replace("/", ".")
                        .replace(".py", "")
                    )
    ds = []
    for mname in vmods:
        try:
            m = importlib.import_module(mname)
            for _, obj in inspect.getmembers(m):
                if (
                    inspect.isclass(obj)
                    and issubclass(obj, OpticalEquipment)
                    and obj.__module__ == mname
                ):
                    if not hasattr(obj, "_DATABASE"):
                        continue
                    for key, entry in obj._DATABASE.items():
                        is_t = issubclass(obj, Telescope)
                        is_e = issubclass(obj, Eyepiece)
                        is_c = issubclass(obj, Camera)
                        if not is_t:
                            ins = entry.get("inputs")
                            if ins:
                                for i, (c, g) in enumerate(ins):
                                    expected_g = get_default_gender(map_conn(c), True)
                                    if map_gender(g) != expected_g:
                                        ds.append(
                                            {
                                                "mod": mname,
                                                "key": key,
                                                "type": "input",
                                            }
                                        )
                            else:
                                c = entry.get("tside_thread")
                                g = entry.get("tside_gender")
                                if c and g:
                                    expected_g = get_default_gender(map_conn(c), True)
                                    if map_gender(g) != expected_g:
                                        ds.append(
                                            {
                                                "mod": mname,
                                                "key": key,
                                                "type": "input",
                                            }
                                        )
                        if not (is_e or is_c):
                            outs = entry.get("outputs")
                            if outs:
                                for i, (c, g) in enumerate(outs):
                                    expected_g = get_default_gender(map_conn(c), False)
                                    if map_gender(g) != expected_g:
                                        ds.append(
                                            {
                                                "mod": mname,
                                                "key": key,
                                                "type": "output",
                                            }
                                        )
                            else:
                                c = entry.get("cside_thread")
                                g = entry.get("cside_gender")
                                if c and g:
                                    expected_g = get_default_gender(map_conn(c), False)
                                    if map_gender(g) != expected_g:
                                        ds.append(
                                            {
                                                "mod": mname,
                                                "key": key,
                                                "type": "output",
                                            }
                                        )
        except Exception:
            continue
    return ds


if __name__ == "__main__":
    print(len(audit()))
