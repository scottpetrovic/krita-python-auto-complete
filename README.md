# Krita: Python Auto-complete generator

Is a Python "fake" module generator for PyKrita. Its purpose is to provide intellisense and code completion in your code editor to simplify the development process when making krita extensions.

A quick demo video:


https://user-images.githubusercontent.com/20190653/163692838-c6f9d7a2-2b3d-4649-a077-32df41c57842.mp4


Originally forked from: https://github.com/scottpetrovic/krita-python-auto-complete . I built on his code to make it functional with todays code base & potentially more future proof, added parameter types into method comments & had an attempt at creating an automated deployment system to Pypi (when you run the script it will try to upload the package to Pypi immediatly, this is still quite wip).


## Usage guides

### Using the generator itself

Download the `generate-python-autocomplete-file.py` and modify the 2 strings `kritaHomeDir` & `moduleDestinationPath` to suit your needs.

`kritaHomeDir` should point towards the directory that has kritas main CMakeLists.txt - it should point towards the source code of Krita.

`moduleDestinationPath` This is where the package will get created locally on your PC. Make sure you dont have any important files in this directory :3

Now you can run the script file with `python generate-python-autocomplete-file.py`. As of writing this, its known to work on Python 3.10.2 in a Windows 11 environment.

### Installing the module for your code editor

First you will need to figure out what Python installation your code editors language server uses and then find its associated pip executable. Once located, run `pip install pathToTheGeneratedTarGz.tar.gz`. Which will be live under `kritaHomeDir/pyKrita/dist` where `kritaHomeDir` is where you set the variable `kritaHomeDir` in `generate-python-autocomplete-file.py` to point towards.

## Uploading to Pypi

As the script runs it will attempt uploading to Pypi, where "twine" will ask you for your Pypi login credentials, if you dont want to upload to pypi, you can simply hit ctrl C with your terminal focused to cancel. You will still have your generated files where you pointed your `KritaHomeDir`.

Anyone is welcome to upload the generated files to Pypi <3
