
IGMP Tester README
==================

Description:
------------
The IGMP Tester is a Python-based command-line interface (CLI) tool designed to send IGMPv3 Join and Leave messages continuously to a specified multicast group. It is intended for network testing and educational purposes.

Requirements:
-------------
- Python 3.x
- Scapy library

Installation:
-------------
Ensure Python 3.x is installed on your system. You can download Python from https://www.python.org/downloads/.

Install Scapy using pip:
```sh
pip install scapy
```

Usage:
------
To use the IGMP Tester, run the script from the command line with the following arguments:
```sh
python script.py <mode> <group_ip> <interval>
```

- `<mode>`: Specifies the operation mode. Use "join" to send IGMP Join messages, or "leave" to send IGMP Leave messages.
- `<group_ip>`: Specifies the IP address of the multicast group.
- `<interval>`: Specifies the interval (in seconds) between each message.

Example:
```sh
python script.py join 239.255.255.250 5
```
This command will send an IGMP Join message to the `239.255.255.250` group every 5 seconds.

To stop the script, press Ctrl+C.

Note:
-----
- Use this tool responsibly and ensure you have permission to test on the network.
- Continuous IGMP messages can affect network performance. Use in a controlled environment.

