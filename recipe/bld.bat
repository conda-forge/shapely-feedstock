
set GEOS_LIBRARY_PATH=%LIBRARY_BIN%

del /f shapely\speedups\_speedups.c
del /f shapely\vectorized\_vectorized.c

"%PYTHON%" setup.py build_ext ^
                    -I"%LIBRARY_INC%" ^
		    -lgeos_c ^
		    -L"%LIBRARY_LIB%" ^
		    install ^
		    --single-version-externally-managed ^
		    --record record.txt
if errorlevel 1 exit 1
