import pyautogui, time

minutes = 0.15
sec = minutes*60
i = 0
while True:
    print("esperando ...")
    time.sleep(sec) 
    pyautogui.click(x=92, y=66)
    time.sleep(10)
    pyautogui.click(x=1318, y=623)
    pyautogui.click(x=1318, y=623)
    pyautogui.click(x=1318, y=623)
    
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{i}.png")
    i+=1
    print(i)
    