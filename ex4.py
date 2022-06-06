# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:08:36 2022

@author: egsra
"""

cycling = int(input("Enter hours cycling:"))
running = int(input("Enter hours running:"))
swimming = int(input("Enter hours swimming:"))

tot_cals_burnt = (cycling*200) + (running*475) + (swimming*275)
pounds_lost = tot_cals_burnt/3500

print("Total pounds lost: {0:.1f}".format(pounds_lost))
