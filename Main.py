import cv2
import pyautogui
import time
import os
import numpy as np

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to capture a screenshot
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

# Function to detect an element on the screen using template matching
def detect_element(template_path, region=None, threshold=0.8):
    screen = capture_screenshot()
    if region:
        screen = screen[region[1]:region[3], region[0]:region[2]]
    template = cv2.imread(template_path, 0)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return (max_loc[0] + region[0], max_loc[1] + region[1]) if region else max_loc
    return None

# Function to tap on an element detected on the screen
def tap_element(x,y):
    coordinates= (x,y)
    if coordinates:
        pyautogui.click(coordinates)
        print(f"Tapped on element at {coordinates}")
    else:
        print("Element not found")

# Main script to combine functionalities
def main():
    print("Starting Pokémon GO interaction script...")

    # Example template paths (replace with actual paths to your templates)
    status_template_path = 'caught.png'
    ok_button_template_path = 'ok.png'

    # Define regions for status and OK button detection (adjust as needed)
    status_region = (182, 257, 382, 337)  # Example region for status message
    ok_button_region = (182, 257, 382, 400)  # Example region for OK button

    # Step 1: Tap on the Pokémon
    print("Move your mouse pointer to the Pokémon and wait for 10 seconds...")
    time.sleep(10)
    tap_element(67,458)
    print("tap")
    time.sleep(3)

    tap_pokemon(170,548)
    print("pok")
    time.sleep(3)
    # Step 2: Prepare to throw the Poké Ball
    prepare_throw()

    # Step 3: Choose the Poké Ball
    # choose_pokeball()

    # Step 4: Aim and throw the Poké Ball
    throw_pokeball()

    # Step 5: Use a berry
    # use_berry()

    # Step 6: Wait for the catch result
    wait_for_catch()

    # Step 7: Confirm if the Pokémon is caught by checking the status
    print("Checking for status message...")
    status_coordinates = detect_element(status_template_path, region=status_region)
    if status_coordinates:
        print("Status message found, Pokémon caught!")
        print("Checking for OK button...")

        # Step 8: Detect and tap the OK button
        ok_button_coordinates = detect_element(ok_button_template_path, region=ok_button_region)
        tap_element(ok_button_coordinates)
    else:
        print("Status message not found, Pokémon escaped.")

    print("Pokémon GO interaction script finished.")

    tap_element(162,692)

# Other functions used in the script (placeholders)
def get_mouse_coordinates():
    x, y = pyautogui.position()
    return x, y

def tap_pokemon(x,y):
    x, y = get_mouse_coordinates()
    pyautogui.click(x, y)
    print(f"Tapped on Pokémon at ({x}, {y})")

def prepare_throw():
    print("Preparing to throw the Poké Ball")

def choose_pokeball():
    print("Choosing a Great Ball")

def throw_pokeball():
    print("Throwing the Poké Ball")
    
    # Define starting and ending points for the swipe (adjust as needed)
    start_x, start_y = 170,548  # Starting point (middle of the screen)
    end_x, end_y = 173,345    # Ending point (adjust Y coordinate for swipe direction)

    # Perform the swipe gesture
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.3, button='left')


def use_berry():
    print("Using a Razz Berry")

def wait_for_catch():
    print("Waiting for catch result...")
    time.sleep(3)

def confirm_catch():
    return True

if __name__ == "__main__":
    main()
