# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:26:07 2021

@author: Jennifer
"""

import LinkedListModule
import BinaryTreeModule
import HashTableModule

import re
import string
import matplotlib
import time

set_object_ll = LinkedListModule.LinkedList()
set_object_bt = BinaryTreeModule.BinaryTreeNode()
set_object_ht = HashTableModule.HashTable()

def experiment(set_object, label): #method to output graphs
    fread = open('pride-and-prejudice.txt') #create a handle to the file
    fsearch = open('words-shuffled.txt')
    
    def read_file (file): #method to add words from the txt file to a list
        wordsRead = [] #create a list to store words read from the text file
        while True:
            line = file.readline() #read a line in the text file
            if not line: #if it is end of file
                break
            line = re.sub('[%s]' % re.escape(string.punctuation), ' ', line) #remove punctuation
            wordsRead.extend(line.split()) #from the list "wordsRead", append the line word by word
        return wordsRead
    
    read_list = read_file(fread) #create a list of words from the txt file
    timing_data = [] #create a list to store words (x value) vs time (y value)
    #initialize time values
    start_time = 0
    end_time = 0
    time_counter = 0
    time_avg_n = 10 #read the time every n words
    for word in read_list: #iterate thru the list that has the words from txt file
        if time_counter == 0:
            start_time = time.perf_counter_ns()
        set_object.add(word) #add words read from txt file to the set (ll,bn or ht set)      
        time_counter += 1
        if time_counter == time_avg_n: #every n nanosecond, end time
            end_time = time.perf_counter_ns()
            x_value = set_object.size() #measure the number of words at the end of the time interval
            y_value = (end_time - start_time)/time_avg_n #time to add each word
            timing_data.append([x_value,y_value]) #store the x value and y value in a list
            time_counter = 0 #reset the time counter
        
    x_values = [pair[0] for pair in timing_data] #create a list of just x values extracting from x,y pairs of time data list
    y_values = [pair[1] for pair in timing_data] #create a list of just y values extracting from x,y pairs of time data list
    matplotlib.pyplot.plot(x_values, y_values, '.', label=label) #scatter plot in matlab
    matplotlib.pyplot.grid(True) 
    
    fout = open(label+'.txt', 'w')
    for pair in timing_data:
        fout.write('{};{}\n'.format(pair[0],pair[1]))
        
    search_list = read_file(fsearch) #create a list to store words that are in 1 text file but not in the other
    
    search_counter = 0
    timing_count = [] #create a list to store how much time it takes for a word to be found that is not in the set
    for word in search_list:
        start_time = time.perf_counter_ns() #read the start time
        if not set_object.contains(word): #if the word is not in the P&P text file
            search_counter += 1
        end_time = time.perf_counter_ns() #read the end time
        timing_count.append(end_time - start_time) #store the time in the list
    
    print(label)
    print("Number of words that are present in the set: ", set_object.size())
    print("How many words do not exist in the set: ", search_counter) 
    print("Average time to search for a word is: ", sum(timing_count)/len(timing_count), "nanosecond")
    print("Worst case average search time is: ", max(timing_count), "nanosecond")
    print("Best case average search time is: ", min(timing_count), "nanosecond")

experiment(set_object_ll, "Linked List Set")

experiment(set_object_bt, "Binary Tree") 

experiment(set_object_ht, "Hash Table")

matplotlib.pyplot.yscale('log') #log scale
matplotlib.pyplot.legend() #add legend
matplotlib.pyplot.xlabel('Number of words in set')
matplotlib.pyplot.ylabel('Time to add word (ns)')
