# This App is used to resolve mutliple IP addresses
# Make sure the IP addresses are sperated by commas
#

from dns import resolver, reversename
from dns.exception import DNSException
import sys

# Global variable for DNS server
dns_server = "8.8.8.8"

def resolve_dns_setup():
    """Configures the DNS resolver with the global DNS server."""
    resolver.default_resolver = resolver.Resolver(configure=False)
    resolver.default_resolver.nameservers = [dns_server]

def reverse_dns_lookup(ip):
    """Performs a reverse DNS lookup."""
    try:
        query = reversename.from_address(ip)
        answers = resolver.resolve(query, "PTR")
        return answers[0].to_text()[:-1]  # Remove trailing dot
    except resolver.NXDOMAIN:
        return "no DNS record found"
    except DNSException:
        return "DNS query failed"

def export_results_to_file(results, choice):
    """Exports results to a file if the user agrees."""
    if choice.lower() == 'y':
        filename = input("Enter the name for the txt file: ")
        with open(filename, "w") as file:
            for result in results:
                file.write(result + "\n")
        print(f"Results exported to {filename}.")

def resolve_from_file():
    """Resolves IP addresses from a file."""
    resolve_dns_setup()
    results = []
    try:
        with open("IPlist.txt", "r") as file:
            ips = file.read().split(',')
        for ip in ips:
            ip = ip.strip()
            resolved_name = reverse_dns_lookup(ip)
            result = f"{ip} - {resolved_name}"
            print(result)
            results.append(result)
        export_choice = input("Export results to a file? (y/n): ")
        export_results_to_file(results, export_choice)
    except FileNotFoundError:
        print("IPlist.txt not found in the folder.")

def manually_enter_ips():
    """Allows manual entry of IP addresses for resolution."""
    resolve_dns_setup()
    results = []
    ip_input = input("Enter the IP addresses separated by commas: ")
    ips = ip_input.split(',')
    for ip in ips:
        ip = ip.strip()
        resolved_name = reverse_dns_lookup(ip)
        result = f"{ip} - {resolved_name}"
        print(result)
        results.append(result)
    export_choice = input("Export results to a file? (y/n): ")
    export_results_to_file(results, export_choice)

def change_default_dns_server():
    """Changes the default DNS server."""
    global dns_server
    new_dns_server = input("Enter the new DNS server IP: ")
    if test_dns_server(new_dns_server):
        dns_server = new_dns_server
        print("DNS server changed successfully.")
    else:
        print("DNS server was not valid. Going back to the home screen.")

def test_dns_server(server_ip):
    """Tests if a DNS server is valid."""
    try:
        resolver.default_resolver = resolver.Resolver(configure=False)
        resolver.default_resolver.nameservers = [server_ip]
        resolver.resolve("google.com")
        return True
    except:
        return False

def main():
    """Main function to run the CLI application."""
    while True:
        print("\nChoose an option:")
        print("1. Resolve from file")
        print("2. Manually enter IPs")
        print("3. Change default DNS server")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            resolve_from_file()
        elif choice == "2":
            manually_enter_ips()
        elif choice == "3":
            change_default_dns_server()
        elif choice == "4":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
