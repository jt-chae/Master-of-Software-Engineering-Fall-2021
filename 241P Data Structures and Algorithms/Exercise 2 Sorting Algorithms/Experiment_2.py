# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:26:07 2021

@author: Jennifer
"""

import SelectionSortModule
import InsertionSortModule
import HeapSortModule
import MergeSortModule
import QuickSortModule

import re
import string
import time

sort_object_ss = SelectionSortModule.SelectionSort()
sort_object_is = InsertionSortModule.InsertionSort()
sort_object_hs = HeapSortModule.HeapSort()
sort_object_ms = MergeSortModule.MergeSort()
sort_object_qs = QuickSortModule.QuickSort()


def experiment(sort_object, label): #method to output graphs
    fread = open('pride-and-prejudice.txt') #create a handle to the file
    
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

    
    #initialize time values
    start_time = 0
    end_time = 0
    total_time = 0
    #time_counter = 0
    #time_avg_n = 10 #read the time every n words

    timing_results = []
    for i in range(10):
        read_list_copy = read_list.copy()
        start_time = time.perf_counter_ns()
        sort_object.sort(read_list_copy) #add words read from txt file to the set (ll,bn or ht set)      
            #time_counter += 1
            #if time_counter == time_avg_n: #every n nanosecond, end time
        end_time = time.perf_counter_ns()
        total_time = end_time - start_time
        timing_results.append(total_time)
        print("{}: {}".format(label, total_time))
    
    fout = open(label+'.txt', 'w')
    for result in timing_results:
        fout.write('{}\n'.format(result))
        
          
experiment(sort_object_qs, "Quick")
experiment(sort_object_hs, "Heap")
experiment(sort_object_ms, "Merge") 
experiment(sort_object_ss, "Selection") 
experiment(sort_object_is, "Insertion")




