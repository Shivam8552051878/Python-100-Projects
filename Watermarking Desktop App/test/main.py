# from PIL import Image
# import glob, os
#
# size = 128, 128
#
# for infile in glob.glob("*.jpg"):
#     print(infile)
#     file, ext = os.path.splitext(infile)
#     with Image.open(infile) as im:
#         im.thumbnail(size)
#         im.save(file + ".thumbnail", "JPEG")
# # im = Image.open("./image.thumbnail")
# # im.save("test.png")
# import glob
# glob.glob('./[0-9].*')
# glob.glob('*.gif')
# glob.glob('?.gif')
# glob.glob('**/*.txt', recursive=True)
# glob.glob('./**/', recursive=True)


#
# import sys
# from PIL import Image, ImageDraw
#
# with Image.open("test.jpg") as im:
#
#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)
#
#     # write to stdout
#     im.save("test2.png")


from PIL import Image, ImageDraw, ImageFont

out = Image.open("test.jpg")
print(out.size[0])
d = ImageDraw.Draw(out)
# use a bitmap font
# font = ImageFont.load("arial.pil")

# draw.text((10, 10), "hello", font=font)
logo = Image.open("free-logoa.jpg")
logo.resize((128, 128))
# use a truetype font
font = ImageFont.truetype("Swis721 Blk BT Black.ttf", size=40)
# draw multiline text
for i in range(50, out.size[0], 400):
    for j in range(50, out.size[1], 400):
        d.multiline_text((i, j), "Hello world", fill=(0, 0, 0), font=font)
out.show()
out.save("watermakr.jpg")

