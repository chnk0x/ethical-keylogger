## Project Overview
This project demonstrates how keyboard activity monitoring works at a behavioral level to help understand how malicious keyloggers operate, enabling better detection and prevention strategies.

##🛠️ Features

- Real-time Monitoring**: Captures keyboard events in real-time.
- Key Categorization**: Classifies keys into letters, numbers, symbols, and control keys.
- Data Encryption**: Encrypts captured data for secure storage.
- Visualization**: Displays key statistics and the sequence of key presses.

##🧩 Ethical Design
- Requires explicit user consent
- No network transmission
- Local encrypted storage only
- Auto-terminates after a fixed duration

##🎯 Skills Demonstrated
- Malware behavior analysis
- Secure coding practices
- Cryptography (Fernet/AES)
- Python system monitoring

##⚠️ Disclaimer
This project is strictly for educational and defensive cybersecurity research purposes.

## 🚀 How to Install & Run

### Prerequisites
- Python 3.10+  
- Pip (Python package manager)  

### Step 1: Clone the Repository
```bash
git clone https://github.com/chnk0x/ethical-keyboard-monitor.git
cd ethical-keyboard-monitor
```
### Step 2: Install Required Libraries
```bash
python -m pip install -r requirements.txt
```
### Step 3: Run the Monitor
```bash
python main.py
```
### Step 4: Decrypt Saved Logs (Optional)
```bash
python decrypt_log.py
