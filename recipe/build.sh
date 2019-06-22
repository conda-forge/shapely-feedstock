#!/bin/bash

rm -rf shapely/speedups/_speedups.c
rm -rf shapely/vectorized/_vectorized.c

export GEOS_DIR=${PREFIX}

# Workaround weird setup.py logic that only triggers force_cython if the MANIFEST.in file is present.
touch MANIFEST.in

${PYTHON} -m pip install --no-deps --ignore-installed .
