import os
import subprocess
import time

try:
    # Change directory to the specified path
    target_directory = r"D:\TSCERESSQL\Mitsukoshi\\"
    os.chdir(target_directory)

    # Wait for 10 seconds
    time.sleep(10)

    # Start Mitsukoshi.exe
    subprocess.Popen("Mitsukoshi.exe")
except Exception as e:
    print(f"An error occurred: {e}")
