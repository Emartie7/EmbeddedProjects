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
Target OS:    Ubuntu Server 20.04.2  
Host/Dev OS:  Ubuntu Desktop 20.04.2  
Tools:        Python 3.8.5  

*************************** Development Environment ***************************  
Setup  
1. Create a directory to hold all project artifacts and Source
    ex: >> mkdir rpi4
2. Download Python 3.8.5
    - Verify that pip is installed: >> python -m pip --version
    - Verify that you can create virtual envivonrments:
        ex: sudo apt-get install python pip python-dev python-virtualenv
3. Create a virtual environment to run/develop the project
    ex: virtualenv MyBuggy
4. Navigate to the "root" directory and activate:
    ex:   >> cd MyBuggy
          >> source ./bin/activate

4. Activate virtual environment and download gpiozero and its dependencies:
    >> pip install gpiozero
    >> pip install rpi.gpio pigpio

5. To deactivate environment:
    >> deactivate

See requirements.txt

********************** Executing Source *******************************
1. Load source code onto mountable USB drive
    ex: MotorTest.py
2. Plug USB drive into Rasperry Pi USB port
3. Mount USB  
    ex: sudo mount -t vfat /dev/sda1 /media/external  
      NOTE: you will have to use "mkdir" to create a mounting point/location for
            your USB media beforehand
4. Activate virtual environment (see above).
5. Navigate to mounted USB location
    >> cd /media/external

6. Run python file
    >> python MotorTest.py

7. To deactivate virtual environment:
    >> deactivate

8. Unmount USB drive
    >> cd                 //Make sure you are not in the mounted directory  
    >> sudo umount /dev/sda1
