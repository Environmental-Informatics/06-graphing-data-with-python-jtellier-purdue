#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:21:07 2020

@author: jtellier
"""

""" Created by Joshua Tellier on 2/21/2020.
This script is designed for Lab 6 of the ABE65100 Class at Purdue University.
It has several functions. First, it imports the appropriate data sets if they
 are named correctly, then makes three plots associated with the streamflow data,
 and finally exports them to a PDF file."""
 
"""For this program to work, the user must specify the name of the input .txt file with
the appropriate variable names (7 in total) as the first argument (and must be a string).
Second argument must also be a string and is the na,e of the output file for the figure (PDF)."""

import numpy #necessary module
import matplotlib.pyplot as pt #necessary module
#this code uses NumPy ndarray objects, powerful data handling structures that are easily
#graphed because one can reference each array by name and look through the data effortlessly
def streamflow_eval(xx,yy):
    Wildcat = numpy.genfromtxt(xx, names=True) #importing data from text as a NumPy ndarray

    pt.subplot(311) #subplot allows us to generate multiple plots in one window
    pt.plot(Wildcat['Year'], Wildcat['Mean'], 'black', label='Mean') #plot line for mean, standard matplotlib plotting function
    pt.plot(Wildcat['Year'], Wildcat['Max'], 'red', label='Max') #and max
    pt.plot(Wildcat['Year'], Wildcat['Min'], 'blue', label='Min') #and min
    pt.xlabel('Year')
    pt.ylabel("Streamflow (cfs)")
    pt.legend(loc='upper right', frameon=True)

    pt.subplot(312) #3 subplots, 1 column, this is number 2 (middle)
    pt.plot(Wildcat['Year'], Wildcat['Tqmean']*100, '^') #the carat represents the triangle symbol
    pt.xlabel('Year')
    pt.ylabel('Tqmean (%)')

    pt.subplot(313) #subplot number three
    pt.bar(Wildcat['Year'], Wildcat['RBindex']) #different kind of plot -> bar plot instead of line or scatter
    pt.xlabel('Year')
    pt.ylabel('R-B Index (Ratio)')

    pt.savefig(yy) #savefig takes the current figure and saves it, input is a string with file extension type

streamflow_eval('Wildcat_Creek_at_Lafayette.Annual_Metrics.txt', "Wildcatfig.pdf")
# close out of interactive window between each use of this function, otherwise
#there is a risk of over-writing the old image and getting a weird result.
streamflow_eval('Tippecanoe_River_at_Ora.Annual_Metrics.txt', "Tippecanoefig.pdf")

