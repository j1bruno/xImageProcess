from PIL import Image
import sys
import os

def main():
    if len(sys.argv) > 0:
        imgName = raw_input("Name processed art: ")

        stdImage = Image.open(str(sys.argv[1]))
        stdImageHighlighted = Image.open(str(sys.argv[1]))
        retinaImage = Image.open(str(sys.argv[1]))
        retinaImageHighlighted = Image.open(str(sys.argv[1]))

        # Resize the images
        stdImage = stdImage.resize((32, 36), Image.BILINEAR)
        stdImageHighlighted = stdImageHighlighted.resize((32, 36), Image.BILINEAR)
        retinaImage = retinaImage.resize((64, 72), Image.BILINEAR)
        retinaImageHighlighted = retinaImageHighlighted.resize((64, 72), Image.BILINEAR)

        # Save the correct files
        stdImage.save(sys.argv[2] + "/" + imgName + ".png")
        stdImageHighlighted.save(sys.argv[2] + "/" + imgName + "-Highlighted.png")
        retinaImage.save(sys.argv[2] + "/" + imgName + "@2x.png")
        retinaImageHighlighted.save(sys.argv[2] + "/" + imgName + "@2x-Highlighted.png")

        print "All images processed!"
    else:
        print 'Usage: xImageProcess.py PNGLocation SaveDirectory'

main()