#!/usr/bin/python3
import time, sys, os, random, pickle, ctypes
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)

try:
    from tkinter import *
except:
    from Tkinter import *
    
try:input = raw_input
except:pass


print("Using 'Virtual' Python Version " + sys.version)


try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except:
    print("Selinium is not installed. \nInstall it by doing: pip install selenium")

try:
    done = pickle.load(open("save.p", "rb"))
except:
    done = []
    pickle.dump(done,open("save.p", "wb"))
for a in done:print(a)

def updateClickBox(row, col):
    row, col = (str(row), str(col))
    try:
        clickBox = waitXPATH(".//*[@id='topiclist']/div[2]/div[2]/p[%s]/span[3]/span[%s]" % (row, col))
    except:
        clickBox = False
    return clickBox

def closeBox():
    global gui
    global username
    global password
    global SchoolCode
    global sCode
    username, password, SchoolCode, sCode = (uName.get(), uPassword.get(), SchoolC.get(), sCode.get())
    #for a in (username, password, SchoolCode, sCode):print(a)
    gui.destroy()

def Badclick(button):browser.find_element_by_xpath(button).click()
def click(button):waitXPATH(button).click()

##def waitXPATH(Name):
##    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, Name)))
##    return element

def waitXPATH(Name):
    while True:
        try:
            element = browser.find_element_by_xpath(Name)
            return element
        except:time.sleep(1)

def NOWAIT(Name):
    time.sleep(2)
    try:
        element = browser.find_element_by_xpath(Name)
        return element
    except:return False

    
def save(done):pickle.dump(done,open("save.p", "wb"))

def waitCLASS(Name):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASSNAME, Name)))
    return element
def waitID(Name):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, Name)))
    return element                                           
def waitNAME(Name):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, Name)))
    return element
def exists(Name):
    found = True
    try:element = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, Name)))
    except:found = False
    return found
def anyMore(x):
    global i
    if NOWAIT(x):return True
    else:return False
def work(mode = 1):
    global runMode
    global wordList
    global index
    global item
    #Foreign means any language ;)
    FToEng = waitXPATH(".//*[@id='viewContainer']/div[2]/div[3]/div[4]/div[1]/div[1]/div[1]/button") #Foreign to English
    EngToF = waitXPATH(".//*[@id='viewContainer']/div[2]/div[3]/div[4]/div[2]/div[1]/div[1]/button") #English to Foreign
    
    wordCount = waitXPATH(".//*[@id='viewContainer']/div[2]/div[3]/div[2]/div[4]/div[2]")
    wordCountText = wordCount.get_attribute('innerHTML')
    wordCount = int(wordCountText.strip())
    print("Number of words to 'learn': " + str(wordCount) + "\n")
    if mode == 1:FToEng.click()
    else:EngToF.click()
    time.sleep(random.randint(3,5))
    if mode == 1:
        print("Learning Vocab...\n")
        wordList = []
        for i in range(1, wordCount + 1):
            try:word1 = waitXPATH(".//*[@id='cardBox']/div/div[%s]/div/div[1]/span[1]" % i).text + "; " + NOWAIT(".//*[@id='cardBox']/div/div[%s]/div/div[1]/span[3]" % i).text
            except:word1 = waitXPATH(".//*[@id='cardBox']/div/div[%s]/div/div[1]/span[1]" % i).text
        
            try:word2 = NOWAIT(".//*[@id='cardBox']/div/div[%s]/div/div[3]/div/span[1]" % i).text + "; " + NOWAIT(".//*[@id='cardBox']/div/div[%s]/div/div[3]/div/span[3]" % i).text
            except:word2 = NOWAIT(".//*[@id='cardBox']/div/div[%s]/div/div[3]/div/span[1]" % i).text
##            word1.replace(u"\u2026", "")
##            word2.replace(u"\u2026", "")
            if word2 == False:
                try:word2 = waitXPATH(str(".//*[@id='cardBox']/div/div[%s]/div/div[4]/span" % i)).text + "; " + NOWAIT(str(".//*[@id='cardBox']/div/div[%s]/div/div[4]/span" % i)).text
                except:word2 = waitXPATH(str(".//*[@id='cardBox']/div/div[%s]/div/div[4]/span" % i)).text
                
            wordList.append((word1, word2))
    print(wordList)
    waittime = random.randint(60,120)
    print("Waiting %s seconds to look like you are learning the answers" % waittime)
    for i in range(waittime):
        sys.stdout.write("\r" + str(waittime-i))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

    waitXPATH(".//*[@id='launchLearningButton']").click()
    time.sleep(random.randint(6,8))
    waitXPATH(".//*[@id='inplaySpecialCharactersModal']/div/div[3]/div[2]/button").click()
    
    reps = 0
    while reps < wordCount:
        entryBox = NOWAIT(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[5]/div[1]/div/input")
        if entryBox == False:
            normal = False

            entryBox = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[6]/div[1]/div/input")

            finAnswer = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[6]/div[1]/button")

        else:
            normal = True
            finAnswer = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[5]/div[1]/button")

        translateText = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[2]/span").text
        if anyMore(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[2]/span[3]"):translateText = translateText + "; " + waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[2]/span[3]").text     

        if normal == True:finAnswer2 = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[5]/div[1]/button")
        else:finAnswer2 = waitXPATH(".//*[@id='cardBox']/div/div[contains(@class, 'qaCard hide-qa-card show-qa-card active')]/div/div/div[6]/div[1]/button")
        
        for tupl in wordList:
            word1, word2 = tupl
            if translateText == word1:ansText = word2
            elif translateText == word2:ansText = word1

        print(translateText)
        timeTaken = random.randint(5, 20)
        timePer = timeTaken / len(ansText)

        for c in ansText:
            entryBox.send_keys(c)
            time.sleep(timePer)
        
        time.sleep(random.randint(5,8))
        finAnswer.click()
        time.sleep(random.randint(3,5))
        try:finAnswer2.click()
        except:pass
        time.sleep(random.randint(3,5))
        reps += 1

    time.sleep(random.randint(6,8))    
    waitXPATH(".//*[@id='inplayCompleteModal']/div/div[2]/div[2]/button").click()
    
    if mode == 1:
        print("\nCompleted 1st Activity!\n")
        #save([str(index),str(item), "1"])
        work(mode = 2)
    else:print("\nCompleted 2nd Activity!\n")
    

    
try:
    index = 0
    for line in open("VocabExpressStuff.txt"):
        line = line.replace("\n", "")
        if index == 0:username = line
        elif index == 1:password = line
        elif index == 2:SchoolCode = line
        elif index == 3:sCode = bool(line)
        index += 1
    runMode = 0
except:
    runMode = 1
    gui = Tk()
    sCode = BooleanVar()
    uName = Entry(gui)
    uPassword = Entry(gui)
    SchoolC = Entry(gui)
    
    gui.geometry("400x125")
    gui.title('Login to Vocab Express')
    Checkbutton(gui, text="No School Code (Function not added yet)", variable=sCode).grid(row=3, sticky=W)
    Label(gui, text="Username:").grid(row=0, column=0)
    Label(gui, text="Password:").grid(row=1, column=0)
    Label(gui, text="School Code:").grid(row=2, column=0)
    uName.grid(row=0,column=1)
    uPassword.grid(row=1, column=1)
    SchoolC.grid(row=2, column=1)
    Button(gui, text="Start Botting!",command=closeBox).grid(row=4, column= 0)
    gui.mainloop()
    
    save = open("VocabExpressStuff.txt", "w")
    save.write(username + "\n" + password + "\n" + SchoolCode + "\n" + str(sCode))
    save.close()
    print("\n\nSaved login details to VocabExpressStuff.txt \nOpen the file to change login details.\n")
    time.sleep(3)
    
    while not username:time.sleep(1)
current_folder = os.getcwd()
chromedriver = os.path.join(current_folder, "chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)
##browser = webdriver.PhantomJS()
##browser.set_window_size(1120, 550)

browser.get('https://www.vocabexpress.com/login/')

elem = browser.find_element_by_name('uname')
elem.send_keys(username)
elem = browser.find_element_by_name('pwd')
elem.send_keys(password)
click('.//*[@id=\'main-body\']/div/div/div[2]/form/footer/div[2]/a[1]')
time.sleep(3)

if False:
    click(".//*[@id='main-body']/div/div/div[2]/form/div/p[4]/input")
    click(".//*[@id='main-body']/div/div/div[2]/form/p[3]/input")
else:
    elem = browser.find_element_by_name('ocde')
    elem.send_keys(SchoolCode + Keys.RETURN)
print("Logged In!")
time.sleep(2)

try:Badclick(".//*[@id='exit']")
except:pass

try:Badclick(".//*[@id=\'modal-container\']/div[3]/div[2]/button")
except:pass

time.sleep(2)

try:
    Badclick(".//*[@id='mainMenu']/div/ul/li[6]/a")        #Preview New Version if not released yet
    print("Using Preview Version :)")
except:pass

time.sleep(5)

click(".//*[@id='homeContainer']/div/div[1]/div[1]/div/div[2]/div[1]")
time.sleep(3)

table = waitXPATH(".//*[@id='viewContainer']/div[2]/div[1]/div[1]/div[2]/ul/li/ul/li[1]/ul")
tableList = table.find_elements_by_class_name("leaf-node")
valList = []
twoDList = []
for val in tableList:
    valList.append(val.text)
    newvallist = val.text.split("\n")
    del newvallist[0]
    for newval in newvallist:newvallist[newvallist.index(newval)] = int(newval)
    twoDList.append(newvallist)

index = 1
for row in twoDList:
    for item in row:
        if [str(index),str(item)] not in done:
            print("Row: " + str(index) + " Col: " + str(item)) #Code below scrolls element into view
            browser.execute_script('return arguments[0].scrollIntoView();', waitXPATH(".//*[@id='viewContainer']/div[2]/div[1]/div[1]/div[2]/ul/li/ul/li[1]/ul/li[%s]/div[2]/div[%s]" % (index, item)))
            click(".//*[@id='viewContainer']/div[2]/div[1]/div[1]/div[2]/ul/li/ul/li[1]/ul/li[%s]/div[2]/div[%s]" % (index, item))  #Need to improve by scrolling down if not found
            time.sleep(2)
            work()
            time.sleep(4)
            click(".//*[@id='viewContainer']/div[2]/div[3]/div[1]/button")   #Only for testing
            time.sleep(2)
            done.append([str(index),str(item)])
            save(done)
            time.sleep(2)
            #if runMode == 0:sys.exit()

    index += 1 
        

input("DONE!")

browser.quit()
