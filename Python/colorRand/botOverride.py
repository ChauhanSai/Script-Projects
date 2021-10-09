import tweepy
import time
from PIL import Image
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###",
    "###")
auth.set_access_token("###",
    "###")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###", "###")
auth.set_access_token("###", "###")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# input color
red, green, blue = eval(input("Value r,g,b: "))

timeBreak = 86400.0

print("Waiting ("+str(round(timeBreak - ((time.time() - 1633798800) % timeBreak)))+")")

time.sleep(timeBreak - ((time.time() - 1633798800) % timeBreak))

# setColor
rgb = (red, green, blue)
rgbString=str(red)+", "+str(green)+", "+str(blue)
hexString = '#%02x%02x%02x' % rgb
fileName = hexString
fileName += ".png"

color = Image.new('RGBA', (1920, 1080), (red, green, blue, 255))
color.save(fileName)

media = api.media_upload(fileName)

# Post tweet with image
tweet = "Hex: "+hexString+"\nRGB: "+rgbString+"\nhttps://chauhansai.github.io/Script-Projects/HTML/randomColors/randomColors.html?color="+hexString.replace("#","")
post_result = api.update_status(status=tweet, media_ids=[media.media_id])

print(hexString)

os.remove(fileName)
