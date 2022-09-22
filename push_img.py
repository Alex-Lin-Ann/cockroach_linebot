#顯示在imgur的圖片
import pyimgur

CLIENT_ID = "e0e5447c40d7cef"
PATH = r"C:\Users\TibeMe_user\Desktop\cockroach_linebot_test\static\cockroach.jpeg" #A Filepath to an image on your computer"
title = "Uploaded with PyImgur"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title=title)
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.type)