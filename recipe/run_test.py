import platform
import py
import os
import sys

implementation = platform.python_implementation()
print('implementation: {}'.format(implementation))
target_platform = os.environ["target_platform"]
print(f'target platform: {target_platform}')
py_version = sys.version_info[:2]
print(f'python version: {py_version}')

pytest_args = ['tests']

py.test.cmdline.main(pytest_args)

from shapely.geometry import LineString

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/shapely/shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

