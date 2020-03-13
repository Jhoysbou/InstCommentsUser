import logging
import time
from comment import Comment

import selenium
import selenium.webdriver as webdriver


class UserDownloader:
    def __init__(self,
                 path_to_chromedriver):
        self._path_to_chromedriver = path_to_chromedriver

        # logger set up
        self._logger = logging.getLogger('SureDownloader_logger')
        self._logger.setLevel(logging.DEBUG)
        # Your path to log
        fh = logging.FileHandler('./src/icu.log')
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

    def get_users(self, path_to_post) -> [Comment]:
        self.driver.get(path_to_post)
        self._logger.info('instagram is loaded')
        # We need to reveal all comments
        # Click plus button until it exists
        while True:
            try:
                self.driver.find_element_by_class_name('afkep').click()
                time.sleep(self._delay)
            #     Short delay to let button get ready
            except selenium.common.exceptions.NoSuchElementException:
                break
        self._logger.info('all comments revealed')

        comments = self.driver.find_elements_by_class_name('Mr508')

        result = []
        for comment in comments:
            result.append([Comment(
                text=comment.find_element_by_tag_name('span').text,
                user=comment.find_element_by_class_name('ZIAjV').text,
                date=comment.find_element_by_tag_name('time').get_attribute('datetime')
            )])

        return result
