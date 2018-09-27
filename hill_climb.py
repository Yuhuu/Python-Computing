#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 20 15:09:19 2018

@author: yuanxinhuang
"""
import csv
import time
import random
import itertools as itertools


def hillClimbing():
     with open("/Users/yuanxinhuang/Downloads/european_cities.csv", "r") as f:
        distances = list(csv.reader(f, delimiter=';'))
        # Choose cities to swap
        city_names = distances[0]
#        city_total = len(distances[0])
        del distances[0]
        
        # Choose 6 cities to swap city 1 is the random city
        # if the city1 is 1 so the wrap will be from city 1 to city 7 
        # if the city1 is 7 so the wrap will be from city 7 to city 13 
        #  swap two stochastic cities
        # when only choose the first ten city, change the 6 to be 20
        cityOrder = itertools.permutations(range(5))
        cityOrder = random.shuffle(list(cityOrder))

        best_trip = 0
        count = 0
        for perm in cityOrder:
            # Choose 6 cities to swap, stop the loop if the result remain the same after 70 loop
            if count < 190:
                new_best_trip = 0 
                i = 0
                while i < len(perm):
                    verdi = list(perm)
                    verdi_i = verdi[i]
                    verdi_j = verdi[(i+1)%len(perm)]
                    # all the trips add an random city nr
                    new_best_trip += float(distances[verdi_i][verdi_j])
                    i += 1  
    
                if best_trip == 0:
                    best_trip = new_best_trip
                    result_list = list(perm)
                if best_trip > new_best_trip:
                    count = 0
                    best_trip = new_best_trip
                    result_list = list(perm)
                if best_trip != 0 and (best_trip < new_best_trip):
                    count += 1
                print("Best trip in distance: ",best_trip,count)
            else:
                break
        print("==============",best_trip)
        		
        return print_function(city_names,result_list)
    
def print_function(city_names,result_list):
     i = 0
     for name in result_list:
            i += 1 
            print(i,":",city_names[name])
     
    
print("Hill Climbing : ")
start = time.time()
finish = time.time()
print("Finish time for Hill Climbing : ")
print(finish-start)
hillClimbing()
