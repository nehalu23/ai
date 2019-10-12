import numpy as np
from PIL import Image

def image(path,get="img",width=200,height=200):
    #original image
    img = Image.open(path)

    # resized image
    cropped_img = img.resize((width,height))

    #converting image to array
    np_img = np.array(cropped_img)

    new_im = Image.fromarray(np_img)
    
    #returning manupilated image
    #def getarray():
     #   return np_img
    #def getimg():
    if get == "img":
        return new_im  
    elif get == "array":
        return np_img
    
    
def info(a="all"):
    
    if a == "image":
        print('''
        ------------------------------------------------------------------------------
        | image function:                                                            |
        ------------------------------------------------------------------------------
        | image function contains 4 parameters                                       |
        | 1 is required                                                              |
        | 3 are optional                                                             |
        |                                                                            |
        | 1 parameter :- image path & name.                                          |
        | 2 parameter :- img or array (ask return result in form of image or array). |
        | 3 parameter :- height of an image.                                         |
        | 4 parameter :- width of an image                                           |
        ------------------------------------------------------------------------------

        ''')