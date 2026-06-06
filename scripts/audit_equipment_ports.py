import os, importlib, inspect
from apts.utils import map_conn, map_gender, get_default_gender, Gender
from apts.opticalequipment.abstract import OpticalEquipment
from apts.opticalequipment.telescope.base import Telescope
from apts.opticalequipment.eyepiece.base import Eyepiece
from apts.opticalequipment.camera.base import Camera
def audit():
    vmods = []
    for r, _, fs in os.walk('apts/opticalequipment'):
        if 'vendors' in r:
            for f in fs:
                if f.endswith('.py') and f != '__init__.py':
                    vmods.append(os.path.relpath(os.path.join(r, f), '.').replace('/', '.').replace('.py', ''))
    ds = []
    for mname in vmods:
        try:
            m = importlib.import_module(mname)
            for _, obj in inspect.getmembers(m):
                if inspect.isclass(obj) and issubclass(obj, OpticalEquipment) and obj.__module__ == mname:
                    if not hasattr(obj, '_DATABASE'): continue
                    for key, entry in obj._DATABASE.items():
                        is_t, is_e, is_c = issubclass(obj, Telescope), issubclass(obj, Eyepiece), issubclass(obj, Camera)
                        if not is_t:
                            ins = entry.get('inputs')
                            if ins:
                                for i, (c, g) in enumerate(ins):
                                    if map_gender(g) != get_default_gender(map_conn(c), True): ds.append({'mod': mname, 'key': key, 'type': 'input'})
                            else:
                                c, g = entry.get('tside_thread'), entry.get('tside_gender')
                                if c and g and map_gender(g) != get_default_gender(map_conn(c), True): ds.append({'mod': mname, 'key': key, 'type': 'input'})
                        if not (is_e or is_c):
                            outs = entry.get('outputs')
                            if outs:
                                for i, (c, g) in enumerate(outs):
                                    if map_gender(g) != get_default_gender(map_conn(c), False): ds.append({'mod': mname, 'key': key, 'type': 'output'})
                            else:
                                c, g = entry.get('cside_thread'), entry.get('cside_gender')
                                if c and g and map_gender(g) != get_default_gender(map_conn(c), False): ds.append({'mod': mname, 'key': key, 'type': 'output'})
        except: continue
    return ds
if __name__ == "__main__": print(len(audit()))
