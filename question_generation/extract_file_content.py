import os
import pdfplumber
from pathlib import Path


def read_pdf(i):
    
    pdf = pdfplumber.open("input/"+i)
    
    text = ""
    for j in pdf.pages:
        try:
            text = text + j.extract_text().replace('\n', '')
        except AttributeError:
            continue
    pdf.close()

    return text


def read_txt(i):
    with open("input/" + i, 'r', encoding='utf8') as file:
        data = file.read().replace('\n', '')
    return data


def read_files():
    # create directory if it doesn't exist already
    Path("input").mkdir(parents=True, exist_ok=True)
    # list files in directory
    file_dir = os.listdir('input/')

    # create list that includes all files of supported formats
    files = {}
    for i in file_dir:
        if os.path.splitext(i)[1] == ".txt" or os.path.splitext(i)[1] == ".pdf":
            files[i] = ""

    # append contents of these files
    for i in files.keys():
        if os.path.splitext(i)[1] == ".txt":
            files[i] = read_txt(i)

        # currently only .txt and .pdf supported
        else:
            files[i] = read_pdf(i)

    # print dictionary that contains all (filename, content) tuples
    return files


def get_file_names_only():
    # create directory if it doesn't exist already
    Path("input").mkdir(parents=True, exist_ok=True)
    # list files in directory
    file_dir = os.listdir('input/')

    # create list that includes all files of supported formats
    files = {}
    for i in file_dir:
        if os.path.splitext(i)[1] == ".txt" or os.path.splitext(i)[1] == ".pdf":
            files[i] = ""

    # print dictionary that contains all (filename, content) tuples
    return files

