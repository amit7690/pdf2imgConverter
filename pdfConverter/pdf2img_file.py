import os,inspect,glob
import sys
import time
from datetime import datetime
from pdf2image import convert_from_path
import ntpath
from zipfile import ZipFile
# import wget
import socket


def convert(latest_file):
	base_dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
	outputDir =  base_dir + '/media/image/'
	now = datetime.now().strftime("%H:%M")
	d = datetime.strptime(str(now), "%H:%M")
	current_time = d.strftime("%I:%M %p")
	current_time = current_time.replace(':','-').replace(' ','_')
	outputDir = outputDir + str(current_time) + '/'
	if not os.path.exists(outputDir):
		os.makedirs(outputDir)
	pages = convert_from_path(latest_file, 500)
	counter = 1
	file_name = ntpath.basename(latest_file)
	file_name = file_name.split('.')[0]
	file_paths = []
	zip_create = False

	for page in pages:
		myfile = outputDir + str(file_name) +'_'+ str(counter) + '.jpg'
		counter = counter + 1
		page.save(myfile, "JPEG")
		file_paths.append(myfile)
	zip_path = base_dir + '/media/zip/'+ str(current_time) +'.zip'

	with ZipFile(zip_path,'w') as zipObj:
		for file in file_paths:
			print('____File___---->>', file)
			print('----file basename--', ntpath.basename(file))
			filebasename = ntpath.basename(file)
			zipObj.write(file, filebasename)
			zip_create = True
	print('---------Zip created successfully--------')
	
	# ------------Delete image folder ------
	# if os.path.exists(outputDir):
	# 	outputDir = outputDir + str(current_time) 
	# 	os.remove(outputDir)
	
	directory = base_dir + '/media/zip/'
	list_of_directories = glob.glob(directory+'*')
	latest_folder = max(list_of_directories, key=os.path.getctime, default=0)

	print('----latest folder -->>>>>', latest_folder)
	localhost = 'http://127.0.0.1:8000/'
	if '/media' in latest_folder:
		latest_folder = latest_folder.split('/media')[1]
		zip_download_path = localhost+ 'media' + latest_folder

	return zip_download_path, zip_create


	