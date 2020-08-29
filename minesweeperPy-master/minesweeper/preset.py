from .generator import Generator
from .error import *

class Presets:
    easy = {"size_x": 10, "size_y": 8, "mines": 10}
    medium = {"size_x": 16, "size_y": 16, "mines": 40}
    hard = {"size_x": 25, "size_y": 20, "mines": 100}
    expert = {"size_x": 50, "size_y": 30, "mines": 200}

def generate_preset_raw(level=None, blank_id: str=" ", mine_id: str="M"):
    """
    Generates a grid using the level settings provided and the IDs of mines and blank cells.
    :param level: Preset
    :param blank_id: string (default " ")
    :param mine_id: string (default "M")
    :return list
    """
    if not level:
        raise NoPresetGiven("Expected level to be a variable from %s.Presets, got: %s" % (__name__, level))

    gen = Generator(size_x=level["size_x"], size_y=level["size_y"], blank_id=blank_id, mine_id=mine_id)
    return gen.generate_raw(level["mines"])

def generate_preset(level=None, blank_id: str=" ", mine_id: str="M"):
    """
    Generates a grid using the level settings provided and the IDs of mines and blank cells in a dict object.
    :param level: Preset
    :param blank_id: string (default " ")
    :param mine_id: string (default "M")
    :return dict
    """
    return {"grid": generate_preset_raw(level, blank_id, mine_id),
            "size_x": level["size_x"], "size_y": level["size_y"],
            "blank_id": blank_id, "mine_id": mine_id}
