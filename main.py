import urllib.request
from selenium import webdriver
from time import sleep
import os


class InstaBot:

    def __init__(self, username, pwd):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/?hl=en')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\'username\']")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\'password\']")\
            .send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
        sleep(2)


class Post(InstaBot):

    @staticmethod
    def createDirectory(profile):
        global imagePath, videoPath

        currentPath = os.getcwd()
        parentPath = os.path.join(currentPath, profile)
        if not os.path.exists(parentPath):
            os.mkdir(parentPath)

        imagePath = os.path.join(parentPath, 'image')
        if not os.path.exists(imagePath):
            os.mkdir(imagePath)

        videoPath = os.path.join(parentPath, 'video')
        if not os.path.exists(videoPath):
            os.mkdir(videoPath)



    def downloadPost(self, profile):

        posts = []
        download_url = ''
        global webPage
        self.createDirectory(profile)
        webPage = 'https://www.instagram.com/' + profile + ''
        self.driver.get(webPage)

        links = self.driver.find_elements_by_tag_name('a')

        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post:
                posts.append(post)

        for post in posts:
            self.driver.get(post)
            shortcode = self.driver.current_url.split('/')[-2]
            typeOfPost = self.driver.find_element_by_xpath('//meta[@property="og:type"]').get_attribute('content')

            if typeOfPost == 'video':
                download_url = self.driver.find_element_by_xpath('//meta[@property="og:video"]')\
                    .get_attribute('content')
                pathOfDirectory = videoPath + '\{}.mp4'.format(shortcode)
                urllib.request.urlretrieve(download_url, pathOfDirectory)
            else:
                download_url = self.driver.find_element_by_xpath('//meta[@property="og:image"]')\
                    .get_attribute('content')
                pathOfDirectory = imagePath + '\{}.jpg'.format(shortcode)
                urllib.request.urlretrieve(download_url, pathOfDirectory)

class TaggedPost(Post):

    def __int__(self):

        taggedPage = webPage + '/tagged'
        self.driver.get(taggedPage)



if __name__ == '__main__':

<<<<<<< HEAD
    # lines = []
    # with open('login.txt', encoding='utf-8')as f:
    #     for line in f:
    #         lines.append(line)
    # f.close()
    #
    # user = lines[0]
    # passwd = lines[1]

    bot = Post()
    #bot = Post(user, passwd)
    bot.downloadPost()
=======
    bot = Post()
    bot.downloadPost('7metrow')
>>>>>>> 89989f925e8ac1ae69cf4a5999715ef96a257046






