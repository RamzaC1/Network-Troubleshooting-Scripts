from scapy.all import IP, send
from scapy.contrib.igmp import IGMP  # Assuming this is the correct import based on your setup
import sys
import time

def send_igmpv3_report(group_ip):
    """Send an IGMPv3 Join/Report message to a specified group."""
    msg = IP(dst="224.0.0.22") / IGMP(type=0x22, gaddr=group_ip)
    send(msg)

def send_igmpv3_leave(group_ip):
    """Send an IGMPv3 Leave/Report message to a specified group."""
    msg = IP(dst="224.0.0.22") / IGMP(type=0x17, gaddr=group_ip)
    send(msg)

def continuously_send_message(mode, group_ip, interval):
    """Continuously send IGMP join or leave messages at a specified interval."""
    try:
        while True:
            if mode == "join":
                send_igmpv3_report(group_ip)
                print(f"Sent IGMPv3 Join for group {group_ip}")
            elif mode == "leave":
                send_igmpv3_leave(group_ip)
                print(f"Sent IGMPv3 Leave for group {group_ip}")
            else:
                print("Invalid mode. Use 'join' or 'leave'.")
                break
            
            time.sleep(interval)  # Wait for the specified interval before sending the next message
    except KeyboardInterrupt:
        print("Program terminated by user.")

def main():
    if len(sys.argv) < 4:
        print("Usage: python script.py <mode> <group_ip> <interval>")
        sys.exit(1)

    mode = sys.argv[1]
    group_ip = sys.argv[2]
    interval = float(sys.argv[3])  # Interval in seconds

    continuously_send_message(mode, group_ip, interval)

if __name__ == "__main__":
    main()
