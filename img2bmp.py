##########################
# How to use this script #
##########################
#
# Run without arguments or:
#
# General:
# img2bmp.py "filename or path" "number of colors"
#
# For Example:
#
# Linux:
# python3 img2bmp.py "/path/to/file/image.jpg" 26
#
# Windows:
# py img2bmp.py "C:/path/to/file/image.jpg" 26

from PIL import Image
import sys
loop = True

while loop == True:

    print ("""
================================================
mmmmm  m    m   mmm   mmmm  mmmmm  m    m mmmmm
  #    ##  ## m"   " "   "# #    # ##  ## #   "#
  #    # ## # #   mm     m" #mmmm" # ## # #mmm#"
  #    # "" # #    #   m"   #    # # "" # #
mm#mm  #    #  "mmm" m#mmmm #mmmm" #    # #
================================================
    """)

    # ask for filename/path if not provided
    if len(sys.argv) == 1:
        print ("Enter filename or path:")
        filename = input()
    else:
        filename = str(sys.argv[1])
        print ("Filename: " + filename)

    # Import file
    img = Image.open(filename)

    # Ask for colors if not provided
    if len(sys.argv) == 3:
        colors = str(sys.argv[2])
        print ("Amount of colors: " + colors)
    else:
        print ("Amount of colors:")
        colors = input()

    newname = filename.split('.')[0] + ".bmp"
    img = img.convert("RGB", palette = Image.ADAPTIVE, colors = int(colors))
    img = img.convert("P", palette = Image.ADAPTIVE, colors = int(colors))
    img.save(newname)

    print ("Image converted to: " + newname)

    # Don't loop if arguments are given
    if len(sys.argv) > 1:
        loop = False