import os
import cv2
import random
import time
from instabot import Bot
bot = Bot()
bot.login(username = 'Your_username',password = 'Your_password')
while True:
    dir_list = os.listdir("images")    
    for i in range(len(dir_list)):
        a = random.choice(dir_list)
        print(a)
        img = cv2.imread("images\\"+a)
        cv2.imwrite("image.jpeg",img)
        comments = [add your comments here] #["comment1","comment2"] add more than 2 comments
        tags= [Add your hastags here] #["#lol","startup","#fun"] add more than 10 tags
        final_tags = " ".join(random.sample(tags, 10))
        final_caption = str(random.choice(comments))+"    DO follow us             @drakemeemer            @drakemeemer                       @drakemeemer                       "+final_tags
        print(final_caption)
        bot.upload_photo("image.jpeg",caption = final_caption)
        dir_list.remove(a)
        print(dir_list)
        time.sleep(60*60*4 - 4)