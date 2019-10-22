import sys
from PIL import Image,ImageDraw
import glob
import re

def resize_pic(ra,dec):
    extension2 = 'gif'
    poss1_red_filenames = glob.glob('images/poss1_red/%.7f_%.7f.%s' %(ra,dec,extension2))
    print('Resizing image : ',poss1_red_filenames[0])
    im = Image.open(poss1_red_filenames[0]) 
    im.resize((512, 512))
    im.save(poss1_red_filenames[0])
    
def merge_into_pic(ra,dec):
    #Retrieve all jpg files
    
    extension = 'jpg'
    panstarrs1_filenames = glob.glob('images/pan-starrs1/%.7f_%.7f*.%s' %(ra,dec,extension))
    print (panstarrs1_filenames)    
   
    
    #Name of all the filters in those images 
    filters = [re.sub('.jpg','',re.findall('[^_]+.jpg',filt)[0]) for filt in panstarrs1_filenames]

    images_filenames = panstarrs1_filenames

    images = [Image.open(path) for path in images_filenames]
    widths, heights = zip(*(i.size for i in images))
    
    sep=10
    total_width = sum(widths) +len(widths)*sep + 512
    max_height = 2*max(heights) + 2*sep 
    
    new_im = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    d = ImageDraw. Draw(new_im)
    Image_text= ['Source: pan-starrs1 Filter: ' + filt for filt in filters]
    
    
    for im,text in zip(images,Image_text):
      new_im.paste(im, (x_offset,0))
      d. text((x_offset+10,max_height/2 - 20), text, fill=(255,255,0))
      x_offset += (im.size[0] + sep)
      
  #Now we add poss photo
    extension2 = 'gif'
   #Now we add the images from poss1-red
    poss1_red_filenames = glob.glob('images/poss1_red/%.7f_%.7f.%s' %(ra,dec,extension2)) 
    Image_text2='Source: poss1_red'
    images_filenames2 = poss1_red_filenames

    images2 = [Image.open(path) for path in images_filenames2]
    widths, heights = zip(*(i.size for i in images2))
    x_offset = total_width//2 - widths[0]
    y_offset = max_height//2 + sep
    for im,text in zip(images2,Image_text2):
      new_im.paste(im, (x_offset,y_offset))
      d. text((x_offset+10,max_height - 20), text, fill=(255,255,0))
      x_offset += (im.size[0] + sep)
    
    
    
    
    
    
    
    d = ImageDraw. Draw(new_im)

    Im_name = 'images/combined/%f_%f.jpg' % (ra,dec)
    new_im.save(Im_name)
    
if __name__=='__main__':
    resize_pic(0,8)
    merge_into_pic(0,8)