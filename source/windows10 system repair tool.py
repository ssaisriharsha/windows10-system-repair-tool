import os
import time
print("=====================================================================")
print("                                                                     ")
print("                        STARTING SYSTEM REPAIR                       ")
print("                                                                     ")
print("=====================================================================")
print("                                                                     ")
print("These are the jobs this application can do for you.")
print("1.Clean The DISM Component Store")
print("2.Repair Corrupted Windows Files Using SFC")
print("3.Repair Corrupted Windows Files Using DISM")
choice = input("Enter the serial number of the job which you want this application to do (1/2/3): ")
if choice == "1":
    print("Analyzing Component Store")
    os.system("dism.exe /Online /Cleanup-Image /AnalyzeComponentStore")
    time.sleep(3)
    print("Warning: You have to cleanup component store only if necessary.")
    time.sleep(3)
    Confirmation = input("Do you want to cleanup the component store?(y/n): ")
    if Confirmation.upper() == "Y":
        os.system("dism.exe /Online /Cleanup-Image /StartComponentCleanup")
        time.sleep(3)
        print("Now Exiting!")
    elif Confirmation.upper() == "N":
        print("Skipping Component Cleanup As Per The User's Instructions")
        time.sleep(3)
        print("Now Exiting!")
        time.sleep(1)
    else:
        print('You have to enter only "y" or "n"')
        time.sleep(3)
        print("Now Exiting!")
        time.sleep(1)
elif choice == "2":
    print("Starting SFC Repair Job")
    os.system("SFC /SCANNOW")
    time.sleep(3)
    print("Operation Cpmpleted Successfully!")
    time.sleep(3)
    print("Now Exiting!")
elif choice == "3":
    Internet_Connection = input("Do you have an active internet connection?(y/n): ")
    if Internet_Connection.upper() == "N":
        iso_file = input("Do you have windows10 wim file?(y/n): ")
        if iso_file.upper() == "Y":
            Location = input("Enter the location of the wim file: ")
            print("Starting DISM")
            os.system("dism.exe /Online /Cleanup-Image /RestoreHealth /Source:" + Location + " /LimitAccess")
            time.sleep(3)
            print("Now Exiting!")
        else:
            print("Sorry but you need either internet connection or wim file in order to run Dism")
            time.sleep(3)
            print("Now Exiting!")
    elif Internet_Connection.upper() == "Y":
        print("Starting DISM")
        os.system("dism.exe /Online /Cleanup-Image /RestoreHealth")
        time.sleep(3)
        print("Now Exiting")
    else:
        print("You have to enter only Y/N")
        time.sleep(3)
else:
    print("Choice Not Valid")
    time.sleep(3)
    print("Now Exiting!")
