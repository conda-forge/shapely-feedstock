import platform
import py

implementation = platform.python_implementation()
print('implementation: {}'.format(implementation))

# SvgTestCase.test_collection is failing due to GEOS 3.9 different coordinate order
# (it's fixed on master so can be removed again with Shapely 1.8)
pytest_args = ['tests', '-k', 'not test_collection']

if implementation != 'PyPy':
    from shapely import speedups
    import shapely.speedups._speedups
    import shapely.vectorized
    import shapely.vectorized._vectorized

    assert speedups.available;

    speedups.enable()
    pytest_args.append('--with-speedups')

py.test.cmdline.main(pytest_args)

from shapely.geometry import LineString

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/Toblerity/Shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

# Check if we can import lgeos.
# https://github.com/conda-forge/shapely-feedstock/issues/17
from shapely.geos import lgeos
