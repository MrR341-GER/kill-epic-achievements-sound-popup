# This kills the Epic Games Overlay and therefore the Achievement Popup and Sound

import psutil
import time

process_name = "EOSOverlayRenderer-Win64-Shipping.exe"

while True:
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                psutil.Process(process.info['pid']).terminate()
                print(f"Process {process_name} with PID {process.info['pid']} terminated.")
            except psutil.NoSuchProcess as e:
                print(f"Process {process_name} already terminated.")
            except psutil.AccessDenied as e:
                print(f"Access Denied to terminate process {process_name}. You might need to run the script as Administrator.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    time.sleep(0.1)  # sleep for 100 milliseconds
