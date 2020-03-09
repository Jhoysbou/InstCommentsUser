from getUsers import UserDownloader

downloader = UserDownloader(path_to_chromedriver='./src/chromedriver', path_to_post='https://www.instagram.com/p/B8tgU9qHSA_/')
downloader.get_users()