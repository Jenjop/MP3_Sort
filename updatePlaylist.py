import os
from pathlib import Path
curdir = os.getcwd()

##def findFiles(directory):
##    output = []
##    try:
##        for file in directory.iterdir():
##            if file.is_file():
##                output += [file]
##    except PermissionError:
##        pass
##    return output

def dirFiles (directory: [Path]) -> list:
    '''Finds paths of all files in input directory'''
    output = []
    try:
        for path in directory.iterdir():
            if path.is_file():
                try:
                    output += [path]
                except PermissionError:
                    pass
    except PermissionError:
        pass

    try:
        for path in directory.iterdir():
            if path.is_dir():
                try:
                    output += dirFiles(path)
                except PermissionError:
                    pass
    except PermissionError:
        pass
    return output



def update_playlist(paths):
    with open(os.path.join(curdir, 'a.m3u'),"a", encoding='utf-8') as file:
        for path in paths:
##            pass
            file.write(path + '\n')

if __name__ == '__main__':
    files = dirFiles(Path(curdir))
    paths = []
    for file in files:
        if file.suffix == ".mp3" or file.suffix == ".ogg":
            file = "\\".join(list([file.parts[0][0:-1]]) + list(file.parts[1::]))
            paths += [file]
    update_playlist(paths)
