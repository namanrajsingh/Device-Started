from telegram import Bot
from keys import TOKEN, ID, DEV_NAME
from asyncio import run
from  socket import create_connection
from  time import sleep
from os import remove,path
from datetime import datetime

bot = Bot(token=TOKEN)

import cv2
jpgFile = 'captured_image.jpg'

def capture_image():
    # Open a connection to the camera (0 represents the default camera, change it if necessary)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()
    # Get the current date and time
    current_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    # Define the font and position for the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (10, 30)  # Position of the text
    font_scale = 1
    color = (255, 255, 255)  # White color text
    thickness = 2

    # Add the date and time to the frame
    cv2.putText(frame, current_time, position, font, font_scale, color, thickness, cv2.LINE_AA)
    if ret:
        return frame
    else:
        print("Error: Could not capture an image.")
        return None

def cameraCapture():
    # Capture an image
    captured_image = capture_image()
    filename="captured_image.jpg"
    # Check if the image was successfully captured
    if captured_image is not None:
        # Save the image
        cv2.imwrite(filename, captured_image)
    return filename

def check_internet():
    try:
        # Connect to the DNS server at Google's IP address
        create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

    
async def send_image():
    try:
        with open(jpgFile, 'rb') as f:
            await bot.send_photo(chat_id=ID, photo=f,caption="Your {} is started.".format(DEV_NAME))
    except Exception as e:
        pass


if __name__ == "__main__":

    if path.isfile(jpgFile):
        run(send_image())
        remove(jpgFile)

    cameraCapture()

    while True:
        if check_internet():
            run(send_image())
            try:
                remove(jpgFile)
            except FileNotFoundError:
                pass
            break 
        else:
            sleep(5) 

    
