import webbrowser, time
import pyautogui as pag

url = str(input('Enter the meeting id :'))
meeting_time = int(input('Enter total minutes of the meeting: '))
comment_ask = input('Type yes/no to print your attendance info in comments :')
# name, regNo, classSec = '','',''

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

    print('Meeting Started')
    time.sleep(2)

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



if __name__ == "__main__":
    meeting_join()
    if(foo):
        comment(name,regNo,classSec)
    time.sleep(meeting_time*60)
    pag.hotkey('ctrl','w')
    print('Meeting ended')