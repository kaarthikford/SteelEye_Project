#Unzip the download file
from zipfile import ZipFile
# Create a ZipFile Object and load sample.zip in it
with ZipFile('DLTINS_20210117_01of01.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()