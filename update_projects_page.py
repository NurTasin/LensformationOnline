from os import path
import os
import html_template

IMG_DIR="./assets/img/lensformation/"
IMG_EXT_JPG='.jpg'
IMG_EXT_PNG=".png"
CAP_EXT='.txt'


Files=[file for file in os.listdir(path.abspath(IMG_DIR))]
Images=[]

for file in Files:
    if file.endswith(IMG_EXT_JPG) or file.endswith(IMG_EXT_PNG):
        Images.append(file)

Images.reverse()

Captions=[]

for file in Files:
    if file.endswith(CAP_EXT):
        Captions.append(file)

def getCaption(img:str):
    fname=img.split('UTC')
    if fname[0]+'UTC.txt' in Captions:
        with open(path.join(IMG_DIR,fname[0]+'UTC.txt'),'r',encoding='utf-8') as handle:
            return handle.read().replace('\n','<br>')
    else:
        raise Exception(f'{fname[0]+"UTC.txt"} not found in {path.abspath(IMG_DIR)}')

if __name__=="__main__":
    img_div=""
    for image in Images:
        path__=path.join(IMG_DIR,image)
        img_div+=html_template.renderImage(href=path__,src=path__,heading="",desc=getCaption(image))
    with open('./projects-compact-grid.html','w+',encoding='utf-8') as handle:
        handle.write(html_template.template(img_div))