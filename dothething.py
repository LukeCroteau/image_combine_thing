from PIL import Image
import sys
from os import listdir
from os.path import isfile, join
#Read the two images

infolder = sys.argv[1]
outfolder = sys.argv[2]

onlyfiles = [f for f in listdir(infolder) if isfile(join(infolder, f))]

largest = 0
for item in onlyfiles:
    xit = int(item.split('.')[0])
    if xit > largest:
        largest = xit

def combine_image(image1, image2, outname):
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    outimage = Image.new('RGB',(2*img1.size[0], img1.size[1]), (250,250,250))
    outimage.paste(img1, (0, 0))
    outimage.paste(img2, (img1.size[0], 0))
    outimage.save(outname)

i = 0
while i < len(onlyfiles):
    image1 = onlyfiles[i]
    image2 = onlyfiles[i+1]

    largest += 1
    combine_image(join(infolder, image1), join(infolder, image2), join(outfolder, str(largest) + '.jpg'))

    i += 2
