import requests
import time

# A real attack would target a server; we are targeting a mock login endpoint
target_url = "https://httpbin.org/post"

# A list of common passwords an attacker might try
password_list = ["password123", "qwerty", "admin123", "IITK_Cyber_2026", "letmein123"]
username = "admin"

print(f"[*] Starting Brute Force Simulation against {target_url}...\n")

start_time = time.time()

for index, password in enumerate(password_list):
    # Pack the login form data
    login_data = {"user": username, "pass": password}
    
    # Send the automated POST request to the website
    response = requests.post(target_url, data=login_data)
    
    # Simulate a detection system counting rapid requests
    print(f"📡 Request {index + 1}: Testing password '{password}' -> Server Status: {response.status_code}")
    
    # If the server sees too many requests too fast, an alert is triggered
    if (index + 1) > 3:
        print("⚠️ SECURITY ALERT: Rate-limiting triggered! Excessive login attempts detected.")
        
    time.sleep(0.5) # Short pause between guesses

print(f"\n[*] Simulation completed in {time.time() - start_time:.2f} seconds.")
