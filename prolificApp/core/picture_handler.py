import os
from PIL import Image

'''This function saves pictures to the server
Inputs are:
pic_upload - the image
name - the name the image should be saved as on the server
'''
def upload_pic(pic_upload, name):
	filename = pic_upload.filename
	ext_type = filename.split('.')[-1] #get the extension type of the file
	storage_filename = str(name) + '.' + ext_type
	storage_filename_copy = 'copy' + str(name) + '.' + ext_type

	filepath = os.path.join(current_app.root_path,'static/pictures', storage_filename) #renames picture
	filepath_copy = os.path.join(current_app.root_path,'static/pictures', storage_filename_copy)
	#making sure everything is the same size
	#output_size = (1000,1000)
	pic = Image.open(pic_upload)
	#pic.thumbnail(output_size)
	pic.save(filepath)

	#saves a copy of the original image that will not be changed
	pic.save(filepath_copy)
	return storage_filename