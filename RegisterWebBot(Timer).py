from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
option = Options()
option.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())
#User 
Timers = [True, "14:44:58"]
username = ""
password = ""
planXpath = ""
scheduleSelector = ""
#
driver.get("") #Target Web

def Logger():
    if(EC.presence_of_all_elements_located(('XPATH', '/html/body/div/div/div/form'))): 

        driver.find_element_by_name("Username").send_keys(username)
        driver.find_element_by_id("Password").send_keys(password)
        driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        if(EC.presence_of_all_elements_located(('XPATH', '/html/body/div[2]/nav/ul/li[2]/div/div/div[1]'))):
            FindPlan()
        else:
            Logger()
    else:
        Logger()

def FindPlan():   
    try: 
        if(EC.presence_of_all_elements_located(('XPATH', planXpath))): 
            driver.find_element_by_xpath(planXpath).click() 
            if(EC.presence_of_all_elements_located(('class', 'js-schedule-content'))):        
                Regist()
            else:
                FindPlan()
        else:
            FindPlan()
    except:
        FindPlan()
def Regist():
    try:
        while Timers[0]:
            now = time.localtime()
            current_time = time.strftime("%H:%M:%S", now)
            if(current_time == Timers[1]):
                Timers[0] = False                
            else:
                pass
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(('id', 'accordian1')))
        if(EC.presence_of_all_elements_located(('id', 'accordian1'))):            
           driver.find_element_by_css_selector(scheduleSelector).click() 
           WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(('class name', 'swal-modal')))
           if(EC.presence_of_all_elements_located(('class name', 'swal-modal'))):
               driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[2]/button').click()
               if(EC.presence_of_all_elements_located(('class name', 'swal-icon swal-icon--error'))):
                    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(('class name', 'swal-icon--error__x-mark')))
                    driver.find_element_by_xpath('/html/body/div[5]/div/div[4]').click()
                    print('Still trying')
                    Regist()
               else:
                   Success()
        else:
            Regist()
    except:
        Regist()
def Success():
    driver.close()
    print('Congraturation! Done registered!')
Logger()
