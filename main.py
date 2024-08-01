import pyautogui
from time import sleep

# INCREATE ESTIMATED PING IF YOUR INTERNET IS SLOW
estimatedPing = 30 # Estimated ping (Just in case of lag)
delay = 5+(estimatedPing/1000) # Delay between messages (5+a bit bc of slow mode)

messages = [
    'HOLD THE LINE!',
    'HOLD!',
]

def Countdown() -> None:
    # Gives you 5 seconds to switch to twitch and click on the "Send a message" bar

    for i in range(5):
        print(5-i)
        sleep(1)
    print('Go')

def Main() -> None:
    # The thing that types
    messageIndex = 0

    while True:
        pyautogui.write(messages[messageIndex])
        pyautogui.press('enter')

        messageIndex = (messageIndex+1) if messageIndex<len(messages) else 0
        sleep(delay)

Countdown()
Main()
input('Script Finished (press enter to close)')
