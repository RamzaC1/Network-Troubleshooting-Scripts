
# TheResolver CLI Application

TheResolver is a command-line interface (CLI) application written in Python, designed to resolve domain names from IP addresses. It offers users the flexibility to resolve IPs from a file, manually enter IP addresses, change the default DNS server, and export results to a file.

## Features

- **Resolve from File:** Read IP addresses from `IPlist.txt`, resolve them to domain names, and output the results to the CLI.
- **Manually Enter IPs:** Users can manually input IP addresses to resolve.
- **Change Default DNS Server:** Allows setting a custom DNS server for resolving IP addresses.
- **Export Results:** Option to export the resolution results to a text file.

## Requirements

- Python 3.6+
- dnspython

## Installation

Ensure Python 3.6 or higher is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Install `dnspython` using pip:

```bash
pip install dnspython
```

## Usage

1. Clone the repository or download the source code to your local machine.
2. Navigate to the application directory in your terminal.
3. Run the application with:

```bash
python main.py
```

4. Follow the on-screen prompts to select an option and use the application.

### Resolving IP Addresses from a File

1. Prepare a text file named `IPlist.txt` in the application directory with IP addresses separated by commas.
2. Choose option `1` when running the application.

### Manually Entering IP Addresses

1. Choose option `2` and enter the IP addresses separated by commas when prompted.

### Changing the Default DNS Server

1. Choose option `3` and enter the new DNS server IP address when prompted.

### Exiting the Application

- Choose option `4` to exit the application.

## Custom DNS Server Validation

The application validates the custom DNS server by attempting to resolve a known IP address. If the resolution fails, it prompts the user that the DNS server was not valid.

## Exporting Results

After resolving IP addresses, the application prompts the user to export the results to a text file. If chosen, the user can specify the filename.

## Contributing

Contributions to TheResolver are welcome. Please feel free to report any issues or suggest enhancements on the project's issues page.

## License

Specify your license or state that the project is unlicensed and available for free use.
