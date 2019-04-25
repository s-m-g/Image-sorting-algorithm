from PIL import Image
import os
import shutil
import time
import psutil
#start is the starting location of the folder where the images are stored
source = os.path.join(os.getcwd(),"start")
#type_1 , type_2 and type_3 are the destination folders where the images will go after sorting
destination_1=os.path.join(os.getcwd(),"type_1")
destination_2= os.path.join(os.getcwd(),"type_2")
list2=os.listdir(source)
for files in list2:
       img_path=source+"\\"+files
# open and show images
      
       im = Image.open(source+"\\"+files)
       

       im.show()
# display image for 10 seconds
       time.sleep(0.1)
# hide image
       for proc in psutil.process_iter():

              if proc.name() == "Microsoft.Photos.exe":
                     # "Microsoft.Photos.exe" is the background process selectively for Windows OS

                     proc.kill()


       name = input("y for yes or n for no-  ")
       
       if(name=="l"):
              shutil.copy(img_path,destination_1)
       elif(name=="r"):
              shutil.copy(img_path,destination_2)
       else:
              shutil.copy(img_path,os.path.join(os.getcwd(),"type_3"))       