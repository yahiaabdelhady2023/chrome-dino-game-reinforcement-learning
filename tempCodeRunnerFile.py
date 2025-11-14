import os
import shutil

folder="Agent_Images"

for filename in os.listdir(folder):
    print("filename",filename)
    shutil.rmtree(os.path.join(folder,filename))