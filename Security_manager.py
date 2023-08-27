import subprocess

def block_usb_ports():
    reg_content = r"""
    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\USBSTOR]
    "Start"=dword:00000004
    """

    with open("block_usb.reg", "w") as reg_file:
        reg_file.write(reg_content)

    subprocess.run(["regedit", "/s", "block_usb.reg"], shell=True)
    print("USB ports blocked.")

def disable_bluetooth():
    powershell_script = r"""
    Set-Service -Name bthserv -StartupType Disabled
    """

    with open("disable_bluetooth.ps1", "w") as ps1_file:
        ps1_file.write(powershell_script)

    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", ".\\disable_bluetooth.ps1"], shell=True)
    print("Bluetooth disabled.")

def disable_command_prompt():
    # This functionality cannot be directly implemented using a Python script.
    print("Please follow the provided manual steps to disable the command prompt.")

def block_website_access():
    website_block_entry = "127.0.0.1 facebook.com"
    hosts_file_path = r"C:\Users\vangu\OneDrive\Desktop\python\Security_managerr.py"

    with open(hosts_file_path, "a") as hosts_file:
        hosts_file.write("\n" + website_block_entry)

    print("Website access to facebook.com blocked.")

if __name__ == "__main__":
    print("Security Manager")

    while True:
        print("\nChoose an option:")
        print("1. Block USB Ports")
        print("2. Disable Bluetooth")
        print("3. Disable Command Prompt")
        print("4. Block Website Access to facebook.com")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            block_usb_ports()
        elif choice == "2":
            disable_bluetooth()
        elif choice == "3":
            disable_command_prompt()
        elif choice == "4":
            block_website_access()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")