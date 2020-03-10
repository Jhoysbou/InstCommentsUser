import csv
from getUsers import UserDownloader

downloader = UserDownloader(path_to_chromedriver='./src/chromedriver', path_to_post='https://www.instagram.com/p/B8tgU9qHSA_/')
users = downloader.get_users()
# write users in scv
with open('unique_users.csv', 'w') as file:
    csv.writer(file).writerows(users)
