
BWMac.py - Bandwidth Monitoring Script for macOS
================================================

Description
-----------
BWMac.py is a Python script specifically tailored for monitoring and logging network bandwidth usage on macOS systems. It tracks the amount of data sent and received over the network, logging these details at specified intervals. Upon exiting, the script provides a summary of the average, highest, and lowest bandwidth usage, along with the total runtime.

Requirements
------------
- macOS operating system
- Python 3.x installed (Python 2.x is not supported)
- psutil library

Installation
------------
1. Ensure Python 3.x is installed on your macOS. This can typically be done via Homebrew with `brew install python`, or by downloading directly from the Python website.
2. Install the psutil library using pip:
   ```
   pip3 install psutil
   ```

Usage
-----
To run BWMac.py, open the Terminal and navigate to the script's directory. Make the script executable and then execute it as follows:
1. Make the script executable:
   ```
   chmod +x BWMac.py
   ```
2. Run the script with an optional interval parameter:
   ```
   ./BWMac.py --interval [SECONDS]
   ```
Replace `[SECONDS]` with the desired interval between bandwidth measurements in seconds. If no interval is specified, the default interval is 10 seconds.

Features
--------
- Monitors and logs network bandwidth usage.
- Customizable monitoring interval via command-line arguments.
- Summary statistics upon script termination including average, highest, and lowest data sent and received, and total runtime.

Output
------
- Log entries are appended to `network_usage_log.txt` in the script's directory, detailing the timestamp, data sent, and data received for each interval.
- Summary statistics are displayed in the Terminal upon script exit.

Note
----
This script is intended for use on macOS systems and requires Python 3.x. Ensure you have the necessary permissions to execute scripts on your system.
