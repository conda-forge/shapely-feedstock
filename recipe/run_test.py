import platform
import pytest
import os
import sys

implementation = platform.python_implementation()
print(f"implementation: {implementation}")
target_platform = os.environ.get("target_platform")
print(f"target platform: {target_platform}")
py_version = sys.version_info[:2]
print(f"python version: {py_version}")

pytest_args = ["tests"]
skip_tests = []

if implementation == "PyPy":
    skip_tests += [
        "test_query",
        "test_references",
        "test_pickle_persistence",
        "test_nearest_",
    ]
    if target_platform in ["osx-64", "win-64"]:
        pytest_args.append("--continue-on-collection-errors")
        skip_tests.append("test_vectorized")
elif implementation == "CPython":
    from shapely import speedups
    import shapely.speedups._speedups
    import shapely.vectorized
    import shapely.vectorized._vectorized

    assert speedups.available

    speedups.enable()
    pytest_args.append("--with-speedups")

if skip_tests:
    pytest_args.extend(
        ["-k", " and ".join(f"not {test}" for test in skip_tests)]
    )

print(f"pytest_args: {pytest_args}")
retcode = pytest.main(pytest_args)
assert retcode == 0

from shapely.geometry import LineString

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/shapely/shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

# Check if we can import lgeos.
# https://github.com/conda-forge/shapely-feedstock/issues/17
from shapely.geos import lgeos

print(f"done {__file__}")
