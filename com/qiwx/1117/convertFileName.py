from PIL import Image
from glob import glob
import os
def image2webp(inputFile,outputFile):
    try:
        img=Image.open(inputFile)
        if img.mode!='RGBA'and img.mode!='RGB':
            img=img.convert('RGBA')

        img.save(outputFile,'WEBP')
        print(inputFile+'has converted to'+outputFile)
    except Exception:
        print('error:'+inputFile+"converted failed to"+outputFile)

matchFileList=glob("*png")
if(len(matchFileList)<0):
    print("there are no *.png file on this directory")
    exit(-1)

outputDir=os.getcwd()+'/output'

for pngFile in matchFileList:
    fileName=pngFile[0:pngFile.index('.')]
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    image2webp(pngFile,outputDir+'/'+fileName+'.webp')

print('converted done! all webp file in the output directory!')










