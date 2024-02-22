import psutil
import time
import argparse
from datetime import datetime
import signal
import sys

# Initialize lists to store sent and received data for analysis
sent_data = []
recv_data = []
start_time = time.time()

def signal_handler(sig, frame):
    # Calculate runtime
    run_time = time.time() - start_time
    hours, remainder = divmod(run_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Calculate and print statistics
    if sent_data and recv_data:  # Check to ensure lists are not empty
        print("\n--- Network Usage Summary ---")
        print(f"Average Sent: {sum(sent_data)/len(sent_data):.2f} MB, Highest Sent: {max(sent_data):.2f} MB, Lowest Sent: {min(sent_data):.2f} MB")
        print(f"Average Received: {sum(recv_data)/len(recv_data):.2f} MB, Highest Received: {max(recv_data):.2f} MB, Lowest Received: {min(recv_data):.2f} MB")
        print(f"Total Runtime: {int(hours)}h:{int(minutes)}m:{int(seconds)}s")
    else:
        print("No data collected.")
    
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_network_usage():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    return bytes_sent, bytes_recv

def log_network_usage(bytes_sent, bytes_recv, interval):
    bytes_sent_diff = (bytes_sent[1] - bytes_sent[0]) / (1024 * 1024)
    bytes_recv_diff = (bytes_recv[1] - bytes_recv[0]) / (1024 * 1024)
    
    # Append data for analysis
    sent_data.append(bytes_sent_diff)
    recv_data.append(bytes_recv_diff)
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{current_time} | Sent: {bytes_sent_diff:.2f} MB, Received: {bytes_recv_diff:.2f} MB in the last {interval} seconds."
    
    print(log_message)
    with open("network_usage_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

def main():
    parser = argparse.ArgumentParser(description='Network Bandwidth Usage Monitoring Script')
    parser.add_argument('-i', '--interval', type=int, default=10, help='Interval in seconds between measurements')
    args = parser.parse_args()
    interval = args.interval
    
    print(f"Monitoring network usage every {interval} seconds... Press Ctrl+C to stop.")
    
    while True:
        bytes_sent_start, bytes_recv_start = get_network_usage()
        time.sleep(interval)
        bytes_sent_end, bytes_recv_end = get_network_usage()
        
        log_network_usage((bytes_sent_start, bytes_sent_end), (bytes_recv_start, bytes_recv_end), interval)

if __name__ == "__main__":
    main()
