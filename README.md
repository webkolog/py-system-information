# PY System Information

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/webkolog/py-system-information/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-system-information/actions)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

**Version:** 1.0

**Created Date:** 2026-07-26

**Last Updated:** 2026-07-26

**Compatibility:** Python 3.6+ (Windows Only)

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

---

**PY System Information** is a lightweight Python script that leverages the Windows Management Instrumentation (WMI) API to quickly fetch and display key operating system details. It provides clean, readable information about your current Windows environment.

## Features

- Fetches full Operating System Name.
- Retrieves exact build Version.
- Identifies OS Manufacturer.
- Detects System Architecture (e.g., 64-bit / 32-bit).

## Prerequisites & Dependencies

This script is strictly compatible with **Windows** operating systems. It relies on the `WMI` package and the `pywin32` extensions to communicate with the Windows kernel.

Ensure you have the required dependency installed before running the script:

```bash
pip install wmi

```

> **Note:** Installing the `wmi` package via pip will automatically fetch the required `pywin32` dependencies in most environments.

## Installation

To use this script, clone the repository or simply download the source file into your project:

```bash
git clone https://github.com/webkolog/py-system-information.git
cd py-system-information

```

## Usage

You can run the script directly from your terminal or integrate the snippet into your automated devops/monitoring workflows.

```python
import wmi

# Initialize the WMI client
c = wmi.WMI()

# Loop through operating system properties
for os in c.Win32_OperatingSystem():
    print(f"OS Name: {os.Name}")
    print(f"Version: {os.Version}")
    print(f"Manufacturer: {os.Manufacturer}")
    print(f"Architecture: {os.OSArchitecture}")

```

## Example Output

When executed on a standard setup, the console output will look similar to this:

```text
OS Name: Microsoft Windows 11 Pro|C:\Windows|\Device\Harddisk0\Partition3
Version: 10.0.22631
Manufacturer: Microsoft Corporation
Architecture: 64-bit

```

## Error Handling

Since this script communicates directly with the Windows API via WMI, running it on **non-Windows platforms** (Linux, macOS) will raise an `ImportError` or a missing module exception. It is highly recommended to wrap the initialization inside an OS-check block if deploying cross-platform:

```python
import platform
import sys

if platform.system() != "Windows":
    print("Error: This script requires a Windows environment.")
    sys.exit(1)

```

## License

This project is open-source software licensed under the [MIT license](https://mit-license.org/).

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Contributing

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to expand the gathered data properties (like CPU/RAM metadata), please feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For any questions or support regarding **PY System Information**, you can refer to the project's GitHub repository issues or contact the author directly via Webkolog.
