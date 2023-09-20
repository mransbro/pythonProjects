import hashlib
import os


def filelist(path):
    files = []
    
    for root, folder, file in os.walk(path):
        for name in file:
            files.append(f"{root}/{name}")
    
    return files

def filehash(text):
    return hashlib.file_digest(text, "md5").hexdigest()





def main(path):

    hashes = {}
    for item in filelist(path):
        with open(item) as f:
            h = filehash(f)
          

if __name__ == "__main__":
    main(".")