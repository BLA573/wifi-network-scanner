# Wi-Fi Network Scanner (Windows)

This is a **beginner Python project** I built while learning how to interact with system commands using Python.  
It uses the Windows `netsh` tool to display nearby Wi-Fi networks.

## 🧠 What I learned

- Running Windows commands in Python with `subprocess`
- Decoding command output with `.decode('ascii')`
- Structuring Python code with functions
- Catching errors with `try/except`

## ⚠️ Requirements

- **OS:** Windows  
- **Python:** 3.x  
- Wi-Fi must be enabled

## 📸 Command Used

The script runs:

```bash
netsh wlan show networks
