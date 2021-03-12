********************* Rasperry Pi 4 Buggy Source Setup ************************
File:   RPiBuggyReadme.md
Author: Edward Martinez
Description: Notes and instructions on setup for running the "buggy" project.
              Includes System description, dev environment setup, and operation procedures
Revision History:

Revision  Date          Notes
1.0       2021 03 11    Intial Commit with system description and dev. environment notes

**************************** System Description *******************************
Hardware:     Rasperry Pi 4 (4GB model)
Peripherals:  See Rpi Buggy/Design Documentation/BuggyBOM.xlsx
Target OS:    Ubuntu Server
Host/Dev OS:  Ubuntu Desktop
Tools:        Python 3

*************************** Development Environment ***************************
Setup
1. Create a directory to hold all project artifacts and Source
    ex: >> mkdir rpi4
2. Download Python 3.8
    - Verify that pip is installed: >> python -m pip --version
    - Verify that you can create virtual envivonrments:
        ex: sudo apt-get install python pip python-dev python-virtualenv
3. Create a virtual environment to run/develop the project
    ex: virtualenv MyBuggy
4. Navigate to the "root" directory and activate:
    ex:   >> cd MyBuggy
          >> source ./bin/activate

See requirements.txt for list of dependencies
