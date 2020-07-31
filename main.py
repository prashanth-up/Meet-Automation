# Made By Prashanth Umapathy
# Specialises in Extreme Laziness

# Very important imports
import webbrowser, time
import pyautogui as pag
import schedule

# Meeing info
url = str(input('Enter the meeting id :'))
meeting_time = int(input('Enter total minutes of the meeting: '))
comment_ask = input('Type yes/no to print your attendance info in comments :')
meet_join_time = input('Enter meeting time in 24hour format (eg: "15:30" for 3:30pm): ')


meet_join_time = str(meet_join_time)

# Comment Check
if (comment_ask.lower() == 'yes' or 'y' or 'Y'):
    print("Please Enter the following details to be shown in comments")
    name = input('Please enter your name :')
    regNo = input('Enter your register number :')
    classSec = input('Enter your Year and Section :')
    foo = True
else:
    foo = False

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


# Opens the meeting ID
def meeting_join():
    webbrowser.get(chrome_path).open(url)

    time.sleep(4)

    pag.hotkey('ctrl','d')
    pag.hotkey('ctrl','e')

    time.sleep(3)

    for i in range(5):
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')

    print("Session has started and will continue for %s minutes"%meeting_time)
    print('Press (Ctrl+c) to exit the program ')
    time.sleep(2)

# Adds the comment in meeting
def comment(name,regNo,classSec):
    time.sleep(15)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('enter')

    time.sleep(4)

    pag.write(name, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(regNo, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(classSec, interval=0.1)
    pag.press('enter')

# Where the wizards work
def mainFunc():
    meeting_join()
    if(foo):
        comment(name,regNo,classSec)
    time.sleep(meeting_time*60)
    pag.hotkey('ctrl','w')
    print('Meeting ended')

if __name__ == "__main__":
    # Schedule it to the time given
    schedule.every().day.at("%s"%meet_join_time).do(mainFunc)
    print("Scheduling meeting at ",meet_join_time)

    while True: 
    # Check whether any scheduled task is pending to run or not
        schedule.run_pending() 
        time.sleep(1) 