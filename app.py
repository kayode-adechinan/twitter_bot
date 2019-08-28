from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TwitterBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome('./chromedriver')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        bot.implicitly_wait(10)  # seconds
        email = bot.find_element_by_class_name('js-username-field')
        password = bot.find_element_by_class_name('js-password-field')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        bot.implicitly_wait(10)  # seconds

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        bot.implicitly_wait(10)  # seconds
        for i in range(1, 3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            bot.implicitly_wait(2)  # seconds
            tweets = bot.find_elements_by_class_name('tweet')
            links = [
                elem.get_attribute('data-permalink-path') for elem in tweets
            ]
            for link in links:
                if link:
                    bot.get('https://twitter.com' + link)
                    try:
                        bot.find_element_by_class_name(
                            'HeartAnimation').click()
                        bot.implicitly_wait(10)  # seconds
                    except Exception as ex:
                        bot.implicitly_wait(10)  # seconds


if __name__ == "__main__":

    ed = TwitterBot('xxxxxxxxxxx@xxxxxxxx.xxxx', 'xxxxxxxxxxxxxx')
    ed.login()
    ed.like_tweet('webdevelopment')
