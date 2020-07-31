import webbrowser, time
import pyautogui as pag

url = str(input('Enter the meeting id :'))
meeting_time = int(input('Enter total minutes of the meeting: '))


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




if __name__ == "__main__":
    meeting_join()
    # comment()
    time.sleep(meeting_time*60)
    pag.hotkey('ctrl','w')
    print('Meeting ended')