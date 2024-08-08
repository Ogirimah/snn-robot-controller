## Installing CoppeliaSIM

- Go to [CoppeliaSim website](https://www.coppeliarobotics.com/) and install the educational only version.
- Make sure Python is installed in your computer, then runn the below script in a terminal to install the dependencies that enables the control of CoppeliaSim with Python
> python3 -m pip install Coppeliasim-zmqremoteapi-client

- The next time you open CoppeliaSim, you will be asked to select between Lua (the difault programming language) and Python. Please choose Python.

- To run CoppeliaSim without GUI use
> coppeliaSimHeadless.dll

- The 'remote1.py' script connects to CoppeliaSim using the ZeroMQ Remote API server.
To run it just type `py remote1.py` in a terminal. Not that the 'absolute_path' is the location where the 'Scene2.ttt' is saved