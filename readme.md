
This is a basic script that will copy the port settings on one Meraki MS switch to the corresponding ports on a another switch.

Simple instructions for Windows users:
1. Install Python 3.9 from the windows app store
2. At command prompt type: ‘pip3 install meraki’
3. Copy the attached python script to a directory on your PC
4. Edit the file and put your API key in between the single quotes’
5. At command prompt cd to the directory where you have the python script, type ‘python3.9 clone.py’
6. Enter old SN
7. Enter new SN
8. Script will run. If the switch you are cloning has less than 48 ports, you will get errors at the end. That is fine since the script is set up for 48 ports, once it runs out of ports to look at, it stops. You can edit line 14 for the exact port count if this annoys you ;)
