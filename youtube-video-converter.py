from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import unittest
import subprocess
import re




class TestPythonWebsite(unittest.TestCase):
    def setUp(self):
        chromeOptions = Options()
        chromeOptions.headless = True
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--window-size=1420,1080')
        chromeOptions.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)

    def test_serach_in_python_website(self):
        ###############################
        ####### Link Validation #######
        ###############################
        youtubeLink = ""
        while True:
            youtubeLink = input("Please enter the youtube link of the video you want to start with : ")
            if re.search("^https://www.youtube.com.*", youtubeLink):
                break
            else:
                print("\nPlease enter a valid youtube link\n")
        ###############################
        ###### Number Validation ######
        ###############################
        listItemsNum = ""
        while True:
            listItemsNum = input("Please enter the number of videos you want to download : ")
            if re.search("^[-+]?[0-9]+$", listItemsNum):
                break
            else:
                print("\nPlease enter a valid integer number\n")
        ###############################
        ##### convert Validation ######
        ###############################
        convert = ""
        while True:
            convert = input("Do you want to convert them to mp3 (y/n)? : ")
            if convert == "y" or convert == "Y" or convert == "n" or convert == "N":
                break
            else:
                print("\nPlease enter a valid choice bteween (y/n)\n")
        ###############################
        ####### Keep Validation #######
        ###############################
        keep = ""
        while True:
            keep = input("Do you want to keep them to mp3 (y/n)? : ")
            if keep == "y" or keep == "Y" or keep == "n" or keep == "N":
                break
            else:
                print("\nPlease enter a valid choice bteween (y/n)\n")
        ###############################
        ###############################
        driver = self.driver
        driver.get(youtubeLink)
        f = open("link.txt", "w")
        link = driver.current_url
        f.write(link)
        f.close()
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')
        subprocess.check_call("mkdir -p /yotube-list-downloader/downloads/downloads-youtube-playlist",shell=True)
        subprocess.check_call("chown $USER:$USER /yotube-list-downloader/downloads/downloads-youtube-playlist",shell=True)
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
            subprocess.check_call("./script.sh {convert} {i} {keep}".format(convert=convert,i=i,keep=keep),shell=True)
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
