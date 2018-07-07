# Krita: Python Auto-complete generator
Iif you have the Krita source code, you can use this to generate the auto-complete file for Python.Many Python editors need a PY file to read for auto complete information. This script reads the C++ header files and creates a python file that can be used for auto-completion. the file is generated in the same location as the header files are. The final file is independent, so it doesn't matter where it ends up being stored. Pointing your Python editor to the file location for a module path should be enough for the auto-complete to pick up.


The Python file has a lot of notes, so make sure to check that out to see exactly what is going on.


If you look in the Output folder, you can see what the final generated file looks like. This is what you would use in your Python editor.


Grab the Krita source code from here as a pre-requisite
https://github.com/KDE/krita

