from PIL import Image, ImageOps
import requests
from io import BytesIO
import time
canvasX = 6000
canvasY = 6000

x1 = 782
y1 = 198
x2 = 781 #new one 975
y2 = 1017 #new one 1017
# ts stores the time in seconds
ts = time.time()

response = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art.png?=" + str(ts))
img = Image.open(BytesIO(response.content))
img_orig  = Image.open(BytesIO(response.content))
img = img.resize((img.size[0] * 3, img.size[1] * 3), Image.NEAREST)

response2 = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art-2.png?=" + str(ts))
img2 = Image.open(BytesIO(response2.content))
img2 = img2.resize((img2.size[0] * 3, img2.size[1] * 3), Image.NEAREST)

mask_url = "https://github.com/italyplace/thing/raw/main/mask2x.png"
response = requests.get(mask_url)
mask_i = Image.open(BytesIO(response.content))
#mask_i = ImageOps.invert(mask_i.convert('RGB'))
mask_i.save("mask_i.png")
mask = Image.new("1", (canvasX, canvasY), 0)
mask.paste(mask_i)
mask.save("mask.png")

tl = (x1 * 3, y1  * 3) # top left corner
tl2 = (x2 * 3, y2  * 3) # top left corner

final_img2 = Image.new('RGBA', (canvasX, canvasY))
unmasked_img2 = Image.new('RGBA', (canvasX, canvasY))
unmasked_img2.paste(img, tl)
unmasked_img2.paste(img2, tl2)

final_img2 = Image.composite(final_img2, unmasked_img2, mask)

final_img2.save("template.png")

fill_color = (69,42,0) 

final_img_bot = Image.new('RGBA', (canvasX, canvasY))
final_img_bot.paste(img,tl)
final_img_bot.paste(img2,tl2)
final_img_bot.save("art-botready.png")


topleft1 = (x1, y1)
topleft2 = (x2, y2)

response = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art.png?=" + str(ts))
img = Image.open(BytesIO(response.content))
bottomleft1 = (topleft1[0] + img.size[0], topleft1[1] + img.size[1])

response2 = requests.get("https://raw.githubusercontent.com/italyplace/rplace/main/art-2.png?=" + str(ts))
img2 = Image.open(BytesIO(response2.content))
bottomleft2 = (topleft2[0] + img2.size[0], topleft2[1] + img2.size[1])

left = min(topleft1[0], topleft2[0])
top = min(topleft1[1], topleft2[1])
right = max(bottomleft1[0], bottomleft2[0])
bottom = max(bottomleft1[1], bottomleft2[1])

final_img_bot = Image.new('RGBA', (2000, 2000))
final_img_bot.paste(img,(x1, y1))
final_img_bot.paste(img2,(x2, y2))
final_img_bot = final_img_bot.crop((left, top, right, bottom))

final_img_bot.save("art-botready-2.png")
