# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:55:21 2019

@author: Yi Bu
"""

import matplotlib
import matplotlib.pyplot as plt
import ast
from collections import Counter
import seaborn as sns
import pandas as pd
import numpy as np

def scatter_pdf (a_list, path_name, file_name, event_name):
    
    plt.subplot(1,2,1)
    bin_1 = 10 ** np.linspace(np.log10(min(a_list)), np.log10(max(a_list)), num = 40)
    plt.hist(np.asarray(a_list), density = None)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("number of repos")
    
    plt.subplot(1,2,2)
    bin_1 = 10 ** np.linspace(np.log10(min(a_list)), np.log10(max(a_list)), num = 40)
    plt.hist(np.asarray(a_list),density = None)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("PDF")
    
    plt.savefig(str(path_name) + "/" + str(file_name) + ".jpg", dpi = 600)
    plt.close()
    
    # Calculating raw distribution
    temp_counter = Counter(a_list)
    temp_dict = {}
    for key, value in temp_counter.items():
        temp_dict[key] = value
    x1, y1 = dic_plot (temp_dict)
        
    # Calculating PDF
    sum_0 = 0.0
    pdf_dict = {}
    for item in temp_dict.keys():
        sum_0 += temp_dict[item]
    for item in temp_dict.keys():
        pdf_dict[item] = float(temp_dict[item]) / float(sum_0)
    x2, y2 = dic_plot (pdf_dict)
    '''    
    plt.subplot(1,2,1)
    plt.plot(x1, y1, "r+", markersize = 1)
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("number of repos")
    plt.xscale("log")
    plt.yscale("log")
    
    plt.subplot(1,2,2)
    plt.plot(x2, y2, "r+", markersize = 1)
    plt.xlabel("number of " + str(event_name))
    plt.ylabel("PDF")
    plt.xscale("log")
    plt.yscale("log")
    '''
    
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
scatter_pdf(repo_userCount, "/kellogg/proj/ybo1623", "user distribution", "users")
                

user_bin = [0, 1, 10, 100, 1000, 10000, 100000]
push_bin = [0, 1, 10, 100, 1000, 10000, 100000]

x1, y1, z1 = np.histogram2d (repo_userCount, repo_pushCount, bins = [user_bin, push_bin])
df_1 = pd.DataFrame({'userCount': repo_userCount, 'pushCount': repo_pushCount})
ax_1 = sns.heatmap(df_1)
ax_1.figure.savefig("/kellogg/proj/ybo1623/user_push.jpg", dpi = 600)
'''
temp_array_1 = map(list,zip(repo_userCount, repo_pushCount))
ax_1 = sns.heatmap(temp_array_1)
ax_1.figure.savefig("/kellogg/proj/ybo1623/user_push.jpg", dpi = 600)


temp_array_2 = map(list,zip(repo_userCount, repo_pullCount))
ax_2 = sns.heatmap(temp_array_2)
ax_2.figure.savefig("/kellogg/proj/ybo1623/user_pull.jpg", dpi = 600)
'''
'''
plt.plot(repo_userCount, repo_pushCount, "r+", markersize = 2)
plt.xlabel("number of users in a repo")
plt.ylabel("number of pushes in a repo")
plt.title("user vs. push")
plt.xscale("log")
plt.yscale("log")
plt.savefig("/kellogg/proj/ybo1623/user_push.jpg", dpi = 600)

plt.plot(repo_userCount, repo_pullCount, "r+", markersize = 2)
plt.xlabel("number of users in a repo")
plt.ylabel("number of pulls in a repo")
plt.title("user vs. pull")
plt.xscale("log")
plt.yscale("log")
plt.savefig("/kellogg/proj/ybo1623/user_pull.jpg", dpi = 600)
'''