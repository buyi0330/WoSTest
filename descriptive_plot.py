# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:55:21 2019

@author: Yi Bu
"""
import json
import matplotlib.pyplot as plt
import ast
from collections import Counter

def scatter_pdf (a_list, path_name, file_name, event_name):
    
    # Calculating raw distribution
    temp_counter = Counter(a_list)
    temp_dict = {}
    for key, value in temp_counter.items():
        temp_dict[key] = value
    x1, y1 = dic_plot (temp_dict)
    
    # Calculating PDF
    sum = 0
    for item in temp_dict.keys():
        sum += temp_dict[item]
    for item in temp_dict.keys():
        pdf_dict[key] = float(temp_dict[key]) / float(sum)
    x2, y2 = dic_plot (pdf_dict)
    
    plt.figure(figsize=(10,5))
    matplotlib.rcParams['agg.path.chunksize'] = 10000
    
    plt.subplot(1,2,1)
    plt.plot(x1, y1, "r+", markersize = 1)
    plt.title("Raw distribution: Number of " + str(event_name) + " in a repo")
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("number of repos")
    plt.xscale("log")
    plt.yscale("log")
    
    plt.subplot(1,2,2)
    plt.plot(x2, y2, "r+", markersize = 1)
    plt.title("PDF: Number of " + str(event_name) + " in a repo")
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("PDF")
    plt.xscale("log")
    plt.yscale("log")
    
    plt.subplots_adjust (left = 2, right = 4, top = 4, bottom = 2, wspace = 0.5, hspace = 0.5)
    plt.savefig(str(path_name) + "/" + str(file_name) + ".jpg", dpi = 600)
    
# Given a dictionary, return x_list as its key list, and y_list as its value list (correspondingly)
def dic_plot (dic):
    x_list = []
    y_list = []
    for item in dic.keys():
        x_list.append(item)
        y_list.append(dic[item])
    return x_list, y_list

# main function starts here...
    
inFile = open("/kellogg/proj/ybo1623/temp_descriptive.txt", "r")
inFile.readline()
inFile.readline()

date_pushCount = {}
date_pullCount = {}
date_forkCount = {}
repo_pushCount = []
repo_pullCount = []
repo_forkCount = []
repo_userCount = []

count = 3
for line in inFile:
    print count
    if count == 3:
        line.replace("'", "\"")
        date_pushCount = ast.literal_eval(line)
    elif count == 4:
        line.replace("'", "\"")
        date_pullCount = ast.literal_eval(line)
    elif count == 5:
        line.replace("'", "\"")
        date_forkCount = ast.literal_eval(line)
    elif count == 7:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_pushCount.append(int(line[index]))
        for index in range(100):
            print repo_pushCount[index]
    elif count == 8:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_pullCount.append(int(line[index]))
    elif count == 9:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_forkCount.append(int(line[index]))
    elif count == 10:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_userCount.append(int(line[index]))
    count += 1

scatter_pdf(repo_pushCount, "/kellogg/proj/ybo1623", "push distribution", "pushes")
scatter_pdf(repo_pullCount, "/kellogg/proj/ybo1623", "pull distribution", "pulls")
scatter_pdf(repo_forkCount, "/kellogg/proj/ybo1623", "fork distribution", "forks")
scatter_pdf(repo_forkCount, "/kellogg/proj/ybo1623", "user distribution", "users")