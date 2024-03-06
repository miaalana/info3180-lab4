import os

def get_uploaded_images():
    upimgs = []
    rootdir = os.getcwd()
    ufldr = os.path.join(rootdir, 'uploads')
    
    for subdir, dirs, files in os.walk(ufldr):
        for file in files:
            if file.lower().endswith(('.png','.jpg','.jpeg')):
                fpath = os.path.join(subdir,file)
                upimgs.append(file)
    return upimgs
