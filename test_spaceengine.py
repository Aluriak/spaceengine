
from spaceengine import SpaceEngine, Planet

spen = SpaceEngine()

for star in spen.addons_stars:
    print('Add a planet to', star.name)
    spen.add(Planet.randomly_built(parent=star.name))
