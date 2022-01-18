# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:00:13 2021

@author: Jennifer
"""

import re, sys, collections
import threadpool
from threading import Lock


class TermFrequency:

    def main(self):
        #read the file and store the words in a set
        stopwords = set(open('stop_words').read().split(',')) #stop_words = set of words that we dont include like "the"
        lock = Lock()
        #this function counts the words in 1 file and add them to our word counter
        def countFile(fileName):
            #finding all the words in this file that are more than 3 character long
            words = re.findall('\w{3,}', open(fileName).read().lower())
            #lock.acquire()
            #adding words that are not in stopwords to the counter
            #collection is built-in in python that contains Counter, Counter is thread-safe
            self.counts += collections.Counter(w for w in words if w not in stopwords)
            #lock.release()
        #counter is a object in python that counts the occurence of each word
        self.counts = collections.Counter() #create a new counter to store the result of our word count
        list_of_files = ['anonymit.txt','cDc-0200.txt','crossbow.txt','gems.txt']
        pool = threadpool.ThreadPool(10)   # define the max size of the pool and create multiple threads
        requests = threadpool.makeRequests(countFile, list_of_files) #make a thread for each of files
        #pool.putRequest throws all requests to run multi-threaded into the thread pool
        [pool.putRequest(req) for req in requests]  # all the reqs are thrown to the pool 
        pool.wait()  # quit after all the threads stop
        for (w, c) in self.counts.most_common(40): #most_common is a Counter built-in function
            print(w, '-', c)



if __name__ == "__main__":
    tf = TermFrequency()
    tf.main()