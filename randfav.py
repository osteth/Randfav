import numpy, os
from PIL import Image
 
# where to save the icons
folder = 'C:\\Users\\ostet_000\\Desktop\\icons'
 
# make sure the save folder exists or create it
if not os.path.exists(folder):
        os.makedirs(folder)
 
# register the .ico extension with PIL so we can save to .ico
Image.register_extension("PNG", '.ico')
 
# set range size for the number of files to generate
for n in xrange(1):
    a = numpy.random.rand(16,16,3) * 255 # 16x16 image 3 bit depth
    print a
    im_out = Image.fromarray(a.astype('uint8')).convert('RGBA')
    icon = os.path.join(folder, '%000d.ico' % n) # change the filename here if you want
    im_out.save(icon)
