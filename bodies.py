"""Definition of bodies classes.

"""


class Star:

    def __init__(self, name:str, starclass:str):
        self._name = str(name)
        self._class = str(starclass)

    @staticmethod
    def from_scfile(path:str):
        import parser
        return parser.parse_sc(path)

    @property
    def name(self) -> str: return self._name


class Planet:

    def __init__(self, name:str, parent:str):
        self._name = str(name)
        self._parent = str(parent)

    @staticmethod
    def randomly_built(name=None, parent=None):
        if name is None:
            name = 'random'
        if parent is None:
            parent = 'random'
        return Planet(name=name, parent=parent)
