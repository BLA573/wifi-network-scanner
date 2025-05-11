import subprocess

def show_wifi_networks():
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
        decoded_result = result.decode('ascii')
        print(decoded_result)
    except subprocess.CalledProcessError:
        print("Failed to retrieve Wi-Fi networks.")

if __name__ == "__main__":
    show_wifi_networks()
