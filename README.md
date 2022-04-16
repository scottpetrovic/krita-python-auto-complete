# Krita: Python Auto-complete generator

Is a Python "fake" module generator for PyKrita. Its purpose is to provide intellisense and code completion in your code editor to simplify the development process when making krita extensions. 

Traditionally, language servers & code editors like VS Code, PyCharm  & Vim (etc) wont be able to recognize the krita module and hence throw warnings and errors at you everywhere as it simply do now know of this "krita" module.

A quick demo video:


https://user-images.githubusercontent.com/20190653/163692838-c6f9d7a2-2b3d-4649-a077-32df41c57842.mp4


Originally forked from: https://github.com/scottpetrovic/krita-python-auto-complete . I built on his code to make it functional with todays code base & potentially more future proof, added parameter types into method comments & had an attempt at creating an automated deployment system to Pypi (when you run the script it will try to upload the package to Pypi immediatly, this is still quite wip).


## Usage & installation

### Pre-packaged packages

This is the easiest way of benefiting from the generator. These pre packaged packages are installed like any other python package, simply download a tar.gz file from any of the prepackaged releases https://github.com/ItsCubeTime/krita-python-auto-complete/releases/latest & run `pip install C:/Path/To/Tar/Gz/file.tar.gz`. Make sure that you call the correct pip - the one thats associated with the intrerpreter of which your IDE is using.

After this, restart your code editor & enjoy <3


### Using the generator itself

Download the `generate-python-autocomplete-file.py` and modify the 2 strings `kritaHomeDir` & `moduleDestinationPath` to suit your needs.

`kritaHomeDir` should point towards the directory that has kritas main CMakeLists.txt - it should point towards the source code of Krita.

`moduleDestinationPath` This is where the package will get created locally on your PC. Make sure you dont have any important files in this directory :3

Now you can run the script file with `python generate-python-autocomplete-file.py`. As of writing this, its known to work on Python 3.10.2 in a Windows 11 environment.

### Installing the module for your code editor

First you will need to figure out what Python installation your code editors language server uses and then find its associated pip executable. Once located, run `pip install pathToTheGeneratedTarGz.tar.gz`. Which will be live under `kritaHomeDir/pyKrita/dist` where `kritaHomeDir` is where you set the variable `kritaHomeDir` in `generate-python-autocomplete-file.py` to point towards.




### Uploading to Pypi
*As of writing this, uploading to pip may not work correctly. Still trying to figure this one out, contributions are welcome*

As the script runs it will attempt uploading to Pypi, where "twine" will ask you for your Pypi login credentials, if you dont want to upload to pypi, you can simply hit ctrl C with your terminal focused to cancel. You will still have your generated files where you pointed your `KritaHomeDir`.

Anyone is welcome to try & upload the generated files to Pypi <3 If you do manage to successfully upload it, please do also open a discussion at https://github.com/ItsCubeTime/krita-python-auto-complete/discussions & drop a link to the pypi adress!

## Contributing

Im open to accept any PRs \^-^/
