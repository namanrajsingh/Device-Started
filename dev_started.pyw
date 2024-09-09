from telegram import Bot
from keys import TOKEN, ID, DEV_NAME
from asyncio import run
from  socket import create_connection
from  time import sleep
from os import remove,path
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
        # save_image(captured_image)
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
            await bot.send_photo(chat_id=ID, photo=f,caption="Your {} is started now".format(DEV_NAME))
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

    
