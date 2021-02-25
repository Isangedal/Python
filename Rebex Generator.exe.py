import os,threading,random,string,time,sys
stop1,stop2 = False,False
def clear():
    if sys.platform == "win32": os.system('cls')
    else: os.system('clear')
def start():
    while not stop1:
        os.system(f'color {random.choice(["A","B","C","D","E","F","0","1","2","3","4","5","6","7","8","9"])}')
        print(f"{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*20}{random.choice(string.ascii_letters)*12}")
def count():
    global stop1
    time.sleep(10)
    stop1 = True
    os.system('color 04')
    while not stop2:
        print('6' * (20*8+12))
def count2():
    global stop2,stop1
    time.sleep(15)
    stop2 = True
    stop1 = False
    threading.Thread(target=start).start()
    time.sleep(10)
    stop1 = True
    os.system('color 07')
    clear()
    print("Deleted: C:\\Windows\\System32")
    print("Preparing to restart")
    time.sleep(3)
    os.system("shutdown /s /t 30")
    time.sleep(10)
    print("JK!")
    os.system("shutdown /a")
clear()
threading.Thread(target=start).start()
threading.Thread(target=count).start()
threading.Thread(target=count2).start()