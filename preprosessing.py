import wget
import os
from zipfile import ZipFile


EXTRACT_PATH = 'data/cornell_movie_dialogs_corpus.zip'


def download_dataset(url, out):
    if not os.path.exists(out):
        os.mkdir(out)

    if not os.path.exists(EXTRACT_PATH): 
        file_name = wget.download(url, out)
        extract_path = file_name
    else:
        extract_path = EXTRACT_PATH
    with ZipFile(extract_path, 'r') as zipObj:
        zipObj.extractall('data')


print(download_dataset('http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip',
    out='data'))
