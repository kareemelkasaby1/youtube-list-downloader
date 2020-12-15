from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from time import sleep
import subprocess


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class TestPythonWebsite(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        chromeOptions = Options()
        chromeOptions.headless = True
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--window-size=1420,1080')
        chromeOptions.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
        # KOKOKOKOKOKOKEODKSFDSKFSFGKOKFG

    def test_serach_in_python_website(self):
        youtubeLink = input("Please enter the youtube link of the video you want to start with : ")
        listItemsNum = input("Please enter the number of videos you want to download : ")
        convert = input("Do you want to convert them to mp3 (y/n)? : ")
        driver = self.driver
        driver.get(youtubeLink)
        f = open("link.txt", "w")
        link = driver.current_url
        f.write(link)
        f.close()
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')
        subprocess.check_call("./script.sh {convert}".format(convert=convert),shell=True)
        for i in range(0,int(listItemsNum)-1):
            nextBtn = driver.find_element_by_class_name("ytp-next-button")
            driver.execute_script("arguments[0].click();", nextBtn)
            slowNetwork = True
            link = driver.current_url
            f = open("link.txt", "w")
            f.write(link)
            f.close()
            driver.execute_script('document.getElementsByTagName("video")[0].pause()')
            subprocess.check_call("./script.sh {convert} {i}".format(convert=convert,i=i),shell=True)
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
