# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 20:54:23 2026

@author: LOQ
"""

import json 
import requests

url = " http://127.0.0.1:8000/weather_predict"

input_data  ={
    
    "AWND": 7.3800,
    "PGTM": 1532.0,
    "PRCP": 0.00,
    "SNOW": 0.0,
    "SNWD": 0.0,
    "TMAX": 46.0,
    "TMIN": 31.0,
    "WDF5": 170.0,
    "WSF5": 17.000,
    "U_Component": 0.00,
    "V_Component": 0.0
    
    
    }


resp = requests.post(url, json=input_data)
print(resp.text)