import pyautogui
import time

# Function to get the current mouse pointer coordinates
def get_mouse_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse coordinates: X={x}, Y={y}")
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        print("Program terminated.")

# Run the function to print mouse coordinates
get_mouse_coordinates()
