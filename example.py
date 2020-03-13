import csv
from getUsers import UserDownloader
from comment import Comment
from FollowersScrapper import followersScrapper
from src.password import *

downloader = followersScrapper(path_to_chromedriver='./src/chromedriver')
downloader.login(login, passwor)
users = downloader.get_followers(path_to_account='https://www.instagram.com/p/B8tgU9qHSA_/')

# write users in scv
# with open('unique_users.csv', 'w') as file:
#     csv.writer(file).writerows(users)
