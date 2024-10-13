
# Listener and Backdoor Scripts

This repository contains two Python scripts: `listener.py` and `backdoor.py`. Together, these scripts form a simple client-server architecture where `listener.py` serves as the server (listener) and `backdoor.py` acts as the client (backdoor). The backdoor connects to the listener and allows for remote command execution, file uploads, and downloads.

## Overview

### `listener.py`
This script sets up a listener that waits for incoming connections. Once connected, it can send commands to the connected client (backdoor), receive responses, and manage file transfers.

#### Features:
- Establishes a TCP connection with the backdoor.
- Sends and receives data using JSON for communication.
- Supports commands like `download`, `upload`, `cd`, and standard system commands.
- Handles file uploads and downloads with base64 encoding.

### `backdoor.py`
This script connects to the listener and waits for commands. It can execute system commands, change directories, and manage file transfers as instructed by the listener.

#### Features:
- Connects to a specified IP and port to establish a connection with the listener.
- Executes system commands on the host machine.
- Changes the working directory using `cd` commands.
- Uploads and downloads files using base64 encoding.

## Prerequisites

- Python 3.x
- Libraries: `socket`, `json`, `base64`, `subprocess`, `os`

## Usage

1. Start the `listener.py` script on your server or local machine by providing the IP and port for the listener to bind to:

    ```bash
    python3 listener.py
    ```

2. Update the IP and port in `backdoor.py` to match those of the listener and start it on the target machine:

    ```bash
    python3 backdoor.py
    ```

3. Use the listener's prompt to send commands to the connected backdoor:

    - **Change Directory**: `cd <path>`
    - **Download a File**: `download <file_path>`
    - **Upload a File**: `upload <file_path>`
    - **Execute System Command**: `<command>` (e.g., `ls`, `whoami`)
    - **Exit**: `exit`

## Disclaimer

These scripts are intended for educational purposes only. Unauthorized access to computer systems or networks is illegal and unethical. Always ensure you have explicit permission before using these scripts on any system.


# 0x1tsjusthicham