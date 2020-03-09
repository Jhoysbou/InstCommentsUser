import logging
import selenium
import selenium.webdriver as webdriver


class UserDownloader:
    def __init__(self,
                 path_to_chromedriver,
                 path_to_post):
        self._path_to_chromedriver = path_to_chromedriver
        self._path_to_post = path_to_post

        # logger set up
        self.logger = logging.getLogger('SureDownloader_logger')
        self.logger.setLevel(logging.DEBUG)
        # Your path to log
        fh = logging.FileHandler('./src/sure.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.delay = 0.1

        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=self._path_to_chromedriver)
        self.logger.info('webdriver has been set up')

    def get_users(self):
        self.driver.get(self._path_to_post)
        print('done')
