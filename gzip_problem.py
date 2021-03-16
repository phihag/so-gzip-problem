import gzip
import os.path

def gzip_blob(blob_name):
    path = "."
    path_file=path+"/"+blob_name
    path_gzip_file=path+"/"+blob_name+".gz"
    with open(path_file, 'rb') as f_in, gzip.open(path_gzip_file, 'wb',compresslevel=9) as f_out:
        f_out.writelines(f_in)

gzip_blob('sphere.css')
