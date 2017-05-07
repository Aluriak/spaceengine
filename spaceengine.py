"""Definition of the SpaceEngine class.

"""

import os
from collections import namedtuple
from bodies import Star, Planet


EXPECTED_SUBDIRS = {'data', 'config', 'docs', 'cache', 'screenshots',
                    'addons', 'system', 'export'}


def _possible_path() -> str or None:
    """Return the first found path where Space Engine seems installed,
    or None if not found."""
    all_paths = (os.path.abspath(os.path.expanduser(_)) for _ in (
        '~/.wine/drive_c/SpaceEngine',  # linux + wine
        'C:/SpaceEngine',  # windows: not tested
    ))
    return next((path for path in all_paths if _valid_se_path(path)), None)


def _valid_se_path(path:str) -> bool:
    """True if given path seems to be a Space Engine installation directory"""
    if not path: return
    if not os.path.exists(path): return
    if not os.path.isdir(path): return
    found_subdirs = frozenset(dirent.name for dirent in os.scandir(path))
    print(found_subdirs)
    return found_subdirs.issubset(EXPECTED_SUBDIRS)


class SpaceEngine:

    def __init__(self, path_to_se:str=None):
        path_to_se = path_to_se or _possible_path()
        if not _valid_se_path(path_to_se):
            raise SystemError("Path to SpaceEngine install directory ({}) "
                              "is not valid".format(path_to_se))
        self.install_dir = path_to_se

    def add(self, body:Planet or Star):
        """Add given body into the addons directory, ready to be read
        by Space Engine itself."""
        if isinstance(body, Planet):
            ...  # TODO
        elif isinstance(body, Star):
            ...  # TODO
        else:
            raise ValueError("Body '{}' is neither Star or Planet, but {}."
                             "".format(body, type(body)))


    @property
    def addons_stars(self) -> iter:
        for filename in os.scandir(self.addons_stars_dir):
            if filename.is_file:
                yield Star.from_scfile(filename.path)
    @property
    def addons_planets(self) -> iter:
        for filename in os.scandir(self.addons_planets_dir):
            if filename.is_file:
                yield Planet.from_scfile(filename.path)

    @property
    def addons_dir(self) -> str:
        return os.path.join(self.install_dir, 'addons')

    @property
    def addons_stars_dir(self) -> str:
        return os.path.join(self.install_dir, 'addons/catalogs/stars')

    @property
    def addons_planets_dir(self) -> str:
        return os.path.join(self.install_dir, 'addons/catalogs/planets')
