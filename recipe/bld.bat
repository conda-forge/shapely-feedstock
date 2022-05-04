
set GEOS_LIBRARY_PATH=%LIBRARY_LIB%

"%PYTHON%" -m cython shapely\speedups\_speedups.pyx
"%PYTHON%" -m cython shapely\vectorized\_vectorized.pyx

%PYTHON% setup.py build_ext -I"%LIBRARY_INC%" -lgeos_c -L"%LIBRARY_LIB%" install --single-version-externally-managed --record record.txt
if errorlevel 1 exit 1
