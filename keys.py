# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
TOKEN = 'YOUR TOKEN'

# Replace 'USER_CHAT_ID' with the chat ID of the user or group where you want to send the image
ID = 'YOUR ID'

DEV_NAME = "YOUR DEVICE NAME"

##### DO NOT EDIT THE BELOW CODE#########
if TOKEN == 'YOUR_BOT_TOKEN':
    import ctypes
    ctypes.windll.user32.MessageBoxW(0, "Bot token has not been provided. Please update the TOKEN in keys.py.", "Token Not provided", 1)
    exit()
