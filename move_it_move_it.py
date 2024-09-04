import pyautogui
import threading
import datetime
import keyboard

screenSize = pyautogui.size()
stop_script = False  # Global variable to control stopping the script

def moveMouse():
    if not stop_script:
        pyautogui.moveTo(5, screenSize[1], duration=1)

def clickMouse():
    if not stop_script:
        pyautogui.click()
        main()

def check_stop_time(end_time):
    global stop_script
    if datetime.datetime.now() >= end_time:
        print("Pasiekta pabaiga.")
        stop_script = True
        quit()

def esc_key_listener():
    global stop_script
    while not stop_script:
        if keyboard.is_pressed('esc'):
            print("Skriptas nutrauktas paspaudus 'ESC'.")
            stop_script = True
            quit()

def main():
    check_stop_time(end_time)

    if stop_script:
        return

    threading.Timer(5.0, moveMouse).start()
    threading.Timer(10.0, clickMouse).start()

# Ask the user how many minutes the script should run
runtime_minutes = int(input("Įveskite, kiek minučių norite, kad scriptas veiktu ir paspauskite ENTER: "))
end_time = datetime.datetime.now() + datetime.timedelta(minutes=runtime_minutes)

# Inform the user when the script started and when it will end
print(f"Skriptas pradėtas: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Skriptas baigsis: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print("Noredami nutraukti scripta - paspausdike 'ESC'")

# Start the ESC key listener in a separate thread
esc_listener_thread = threading.Thread(target=esc_key_listener)
esc_listener_thread.start()

main()
