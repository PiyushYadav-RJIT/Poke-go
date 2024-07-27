import pyautogui
import time

# Function to throw a Poké Ball with a swipe-up action
def throw_pokeball():
    print("Throwing the Poké Ball")
    
    # Define starting and ending points for the swipe (adjust as needed)
    start_x, start_y = 170,548  # Starting point (middle of the screen)
    end_x, end_y = 173,328    # Ending point (adjust Y coordinate for swipe direction)

    # Perform the swipe gesture
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.3, button='left')

# Example usage


time.sleep(5)
throw_pokeball()
