import hashlib
from datetime import datetime

def generateFilename(filename):
    f_name = filename.rsplit('.', 1)
    f_name[0] = hashlib.md5((f_name[0] + datetime.now().strftime("%d-%m-%y_%H-%M")).encode('utf-8')).hexdigest()
    return '.'.join(f_name)