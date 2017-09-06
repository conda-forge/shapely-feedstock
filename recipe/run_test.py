from shapely import speedups;

assert speedups.available;

speedups.enable()

from shapely.geometry import LineString

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/Toblerity/Shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

# Check if we can import lgeos.
# https://github.com/conda-forge/shapely-feedstock/issues/17
from shapely.geos import lgeos

# https://github.com/Toblerity/Shapely/issues/519#issuecomment-327484168
from shapely.geometry import Point, Polygon
import shapely.prepared

point = Point(0.95, 0.05)
geom = Polygon([(0, 0), (1, 0), (0, 1), (0, 0)])
assert shapely.prepared.prep(geom).contains(point) == geom.contains(point)
