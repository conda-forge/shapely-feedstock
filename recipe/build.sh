#!/bin/bash

rm -rf shapely/speedups/_speedups.c
rm -rf shapely/vectorized/_vectorized.c

if [[ "$CONDA_BUILD_CROSS_COMPILATION" == "1" ]]; then
  # workaround until cross-python is fixed
  rm $BUILD_PREFIX/bin/python
  ln -sf $PREFIX/bin/python $BUILD_PREFIX/bin/python
fi

cython shapely/speedups/_speedups.pyx
cython shapely/vectorized/_vectorized.pyx

export GEOS_DIR=${PREFIX}

${PYTHON} -m pip install --no-deps --ignore-installed .
