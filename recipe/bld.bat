set LIB=%LIBRARY_LIB%;%LIB%
set LIBPATH=%LIBRARY_LIB%;%LIBPATH%
set INCLUDE=%LIBRARY_INC%;%INCLUDE%;%RECIPE_DIR%

set GEOS_LIBRARY_PATH=%LIBRARY_BIN%\geos_c.dll

"%PYTHON%" -m pip install --no-deps --ignore-installed --verbose . ^
                          --global-option=build_ext ^
                          --global-option="-I%LIBRARY_INC%" ^
                          --global-option="-L%LIBRARY_LIB%" ^
                          --global-option="-lgeos_c"
if errorlevel 1 exit 1
