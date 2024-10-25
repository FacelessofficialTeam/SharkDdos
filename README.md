# SharkDdos DDoS Tool Own By Facelessofficial 

## Overview

**SharkDdos** is a powerful DDoS simulation tool that allows you to test the resilience of your network or server against various types of Distributed Denial of Service attacks. It supports multiple attack vectors, including UDP, TCP, HTTP, and SYN floods, making it an essential tool for security professionals.

## Features

- **Multiple Attack Types**: UDP, TCP, HTTP, and SYN flood options.
- **Configurable Parameters**: Customize the target, port, duration, number of threads, and proxy settings.
- **User-Agent Spoofing**: Randomizes user agents and referers for HTTP requests to evade basic protections.
- **Thread Management**: Efficiently launches multiple threads for concurrent attack execution.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via pip)

## Installation

To install SharkDdos, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/FacelessofficialTeam/SharkDdos.git
   cd SharkDdos
   python SharkDdos.py <target> <port> <duration> [--threads <num_threads>] [--udp] [--tcp] [--http] [--syn] [--proxy <ip:port>]
   
