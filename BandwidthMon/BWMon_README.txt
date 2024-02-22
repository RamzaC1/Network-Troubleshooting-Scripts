
BWMon.py - Bandwidth Monitoring Script
======================================

Description
-----------
BWMon.py is a Python script designed for monitoring and logging network bandwidth usage on Windows 10/11 systems. It tracks the amount of data sent and received over the network, logging these details at specified intervals. Upon exiting, the script provides a summary of the average, highest, and lowest bandwidth usage, along with the total runtime.

Requirements
------------
- Python 3.x
- psutil library

Installation
------------
1. Ensure Python 3.x is installed on your system.
2. Install the psutil library using pip:
   ```
   pip install psutil
   ```

Usage
-----
To run BWMon.py, navigate to the script's directory in the command prompt or PowerShell and execute:
```
python BWMon.py --interval [SECONDS]
```
Replace `[SECONDS]` with the desired interval between bandwidth measurements in seconds. If no interval is specified, the default interval is 10 seconds.

Features
--------
- Monitors and logs network bandwidth usage.
- Allows customization of the monitoring interval via command-line arguments.
- On script termination (Ctrl+C), displays a summary of bandwidth usage including average, highest, and lowest data sent and received, and the total script runtime.

Output
------
- Log entries are appended to `network_usage_log.txt` in the script's directory, detailing the timestamp, data sent, and data received for each interval.
- Summary statistics are displayed in the command prompt or PowerShell upon script exit.

Note
----
This script is intended for use on Windows 10/11 systems and requires Python 3.
