'''
Get all the tiles from https://www.raremaps.com/gallery/detail/66146/birds-eye-view-of-the-life-of-christ-chronological-geogra-larkin
'''

from PIL import Image
import requests
import os

IMG_DIR = "Bird's Eye View of the Life of Christ/tiles/"
TILESZ=256
# For LEFT MAP:
#XMIN=1
#XMAX=10
#YMIN=5
#YMAX=33
# For MID MAP:
#XMIN=46
#XMAX=60
#YMIN=5
#YMAX=18
# For everything:
XMIN=1
XMAX=66
YMIN=1
YMAX=50

def download_tiles():
    URL_BASE = 'https://storage.googleapis.com/raremaps/img/dzi/img_66146_files/15/'

    for x in range(XMIN,XMAX+1):
        for y in range(YMIN,YMAX+1):
            fname = f'{x}_{y}.jpg'
            print(fname)
            destfile = f'{IMG_DIR}{fname}'
            if not os.path.isfile(destfile):
                url = URL_BASE + fname
                r = requests.get(url, allow_redirects=True)
                open(f'{IMG_DIR}{fname}','wb').write(r.content)

def stitch_tiles():
    stitched_img = Image.new('RGB',(TILESZ*(XMAX-XMIN+1),TILESZ*(YMAX-YMIN+1)))
    for x in range(XMIN,XMAX+1):
        for y in range(YMIN,YMAX+1):
            fname = f'{x}_{y}.jpg'
            img = Image.open(f'{IMG_DIR}{fname}')
            stitched_img.paste(img,(TILESZ*(x-XMIN),TILESZ*(y-YMIN)))
    outfile = f'{IMG_DIR}merged_{XMIN}-{XMAX}_{YMIN}-{YMAX}.jpg'
    print(f"Writing {outfile}")
    stitched_img.save(outfile,'JPEG')

if __name__=='__main__':
    download_tiles()
    stitch_tiles()