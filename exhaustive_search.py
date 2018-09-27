# -*- coding: utf-8 -*-
"""
Created on Sep 20 11:09:19 2018

@author: yuanxinhuang
"""
import csv
import itertools as itertools
import time

def sum_function():
    
    with open("/Users/yuanxinhuang/Downloads/european_cities.csv", "r") as f:
        data = list(csv.reader(f, delimiter=';'))
        names = data[0]
        del data[0]
        
    permutation_list = itertools.permutations(range(7))
    
#    if best_trip < new_best_trip then:
    best_trip = 0
    result_list = []
    for perm in permutation_list:
        new_best_trip = 0 
        i = 0
        while i < len(perm):
            verdi = list(perm)
            verdi_i = verdi[i]
            verdi_j = verdi[(i+1)%len(perm)]
            new_best_trip += float(data[verdi_i][verdi_j])
            i += 1  
        if best_trip == 0:
            best_trip = new_best_trip
            result_list = list(perm)
        if best_trip > new_best_trip:
            best_trip = new_best_trip
            result_list = list(perm)
        print("Best trip in distance: ",best_trip)
        print("The best trip permutation is:")
        i = 0
        for name in result_list:
            i += 1 
            print(i,":",names[name])


start = time.time()
sum_function()  
end = time.time()
print("This is the run time:")
print(round(end-start,4))
