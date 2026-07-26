import wmi
c = wmi.WMI()
for os in c.Win32_OperatingSystem():
    print(f"OS Name: {os.Name}")
    print(f"Version: {os.Version}")
    print(f"Manufacturer: {os.Manufacturer}")
    print(f"Architecture: {os.OSArchitecture}")