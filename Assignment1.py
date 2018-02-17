# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:58:11 2018

@author: JESSICA
"""

#Converting Temperature in Fehrenheit to Celsius.

Fahrenheit=int(raw_input("Enter a temperature in Fahrenheit:"))

Celsius=(Fahrenheit-32)*5.0/9.0

print"Temperature:", Fahrenheit,"Fahrenheit=", Celsius, "C"


#Converting temperature in Celsius to Fehrenheit.

Celsius=int(raw_input("Enter a temperature in Celsius:"))

Fahrenheit=(Celsius+32)*9.0/5.0

print"Temperature", Celsius,"Celsius=", Fahrenheit, "F"
