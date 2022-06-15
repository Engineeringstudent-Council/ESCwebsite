import os
import pandas as pd
import numpy as np

# The following is copied from https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
##### BEGIN COPY #####
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFilesHelper(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles    
    
def getListOfFiles(dirName, filterList=True):
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFilesHelper(dirName)
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
    # Filter the list
    if filterList:
        newList = []
        
        for elem in listOfFiles:
            try:
                if elem[-3:] == '.js':
                    newList.append(elem)
                elif elem[-4:] == '.css':
                    newList.append(elem)
                elif elem[-5:] == '.html':
                    newList.append(elem)
            except:
                print("Name too short: " + elem)
        
        listOfFiles = newList
    
    return [i.split('\\')[-1] for i in listOfFiles]
        
#####  END COPY  #####

def splitByExtension(fileList):
    js = []
    css = []
    html = []
    for elem in fileList:
        if elem[-3:] == '.js':
            js.append(elem)
        elif elem[-4:] == '.css':
            css.append(elem)
        elif elem[-5:] == '.html':
            html.append(elem)
        else:
            raise RuntimeError("Argument to splitExtension contains an unknown extension")
            
    return js, css, html

def filterByContentType(df, content_type):
    path_series = df[df["Content Type"] == content_type]["URL"]
    split_paths = list(path_series.str.split("/"))
    return [l[-1] for l in split_paths]

### UPDATE THESE PATHS
local_path = "../../ESCWebsite"
crawl_data_path = "crawl_data.csv"

local_js, local_css, local_html = splitByExtension(getListOfFiles(local_path))
crawl_data = pd.read_csv(crawl_data_path)
crawl_data = crawl_data[crawl_data["Host"] == "esc.berkeley.edu"]

online_js = filterByContentType(crawl_data, "Javascript")
online_css = filterByContentType(crawl_data, "CSS")
online_html = filterByContentType(crawl_data, "HTML")
