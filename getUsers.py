import logging
import time

import selenium
import selenium.webdriver as webdriver


class UserDownloader:
    def __init__(self,
                 path_to_chromedriver,
                 path_to_post):
        self._path_to_chromedriver = path_to_chromedriver
        self._path_to_post = path_to_post

        # logger set up
        self._logger = logging.getLogger('SureDownloader_logger')
        self._logger.setLevel(logging.DEBUG)
        # Your path to log
        fh = logging.FileHandler('./src/sure.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self._logger.addHandler(fh)
        self._logger.addHandler(ch)
        self._delay = 1

        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=self._path_to_chromedriver)
        self._logger.info('webdriver has been set up')

    def get_users(self):
        self.driver.get(self._path_to_post)
        while True:
            try:
                self.driver.find_element_by_class_name('afkep').click()
                time.sleep(self._delay)
            except selenium.common.exceptions.NoSuchElementException:
                break

        comments = self.driver.find_elements_by_class_name('ZIAjV')

        users_accounts = ['@' + comments[i].text for i in range(len(comments))]

        users_accounts = set(users_accounts)
        users_in_comments = self.driver.find_elements_by_class_name('notranslate')

        users_in_comments = [users_in_comments[i].text for i in range(len(users_in_comments))]
        users_in_comments = set(users_in_comments)

        users = users_accounts.union(users_in_comments)
        self.driver.close()
        return users

