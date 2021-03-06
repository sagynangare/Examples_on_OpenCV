import urllib
import cv2
import numpy as np
import os

def store_raw_images():
    neg_image_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.urlopen(neg_image_link).read().decode()
    pic_num =917

    if not os.path.exists('neg'):
        os.makedirs('neg')
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i,"neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg", resized_image)
            pic_num +=1
        except Exception as e:
            print(str(e))
        
            
def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))





        
cv2.destroyAllWindows()        
#store_raw_images()

find_uglies()
