
set GEOS_LIBRARY_PATH=%LIBRARY_LIB%

"%PYTHON%" -m cython shapely\speedups\_speedups.pyx
"%PYTHON%" -m cython shapely\vectorized\_vectorized.pyx

"%PYTHON%" -m pip install --no-deps --ignore-installed --verbose . ^
                          --global-option="build_ext" ^
                          --global-option="-I%LIBRARY_INC%" ^
                          --global-option="-L%LIBRARY_LIB%" ^
                          --global-option="-lgeos_c"
if errorlevel 1 exit 1
