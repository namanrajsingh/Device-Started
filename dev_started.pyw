from telegram import Bot
from keys import TOKEN, ID, DEV_NAME
from asyncio import run

bot = Bot(token=TOKEN)

import cv2

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


async def send_image():
    try:
        with open('captured_image.jpg', 'rb') as f:
            await bot.send_photo(chat_id=ID, photo=f,caption="Your {} is started now".format(DEV_NAME))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    cameraCapture()
    run(send_image())