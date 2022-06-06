from zipfile import ZipFile
import os, inspect, sys,glob

base_dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths 


directory = base_dir + '/media/image/'
list_of_directories = glob.glob(directory+'*')
latest_folder = max(list_of_directories, key=os.path.getctime, default=0)
file_paths = get_all_file_paths(latest_folder)  
print('latest_folder------------', latest_folder)


def MakeZip(file_paths):  
    for file_name in file_paths:
        print('______File Name_____', file_name)

    with ZipFile('my_python_files.zip','w') as zip:
        for file in file_paths:
            print('*******create zip******')
            zip.write(file)


