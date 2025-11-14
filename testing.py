import os 
import glob

folder="Agent_Images"
files = glob.glob(os.path.join(folder,"/*"))

for f in files:
    print("file is ",f)
