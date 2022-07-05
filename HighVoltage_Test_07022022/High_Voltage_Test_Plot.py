#!/bin/env python3

######################################
#    HELIX High Voltage Test Plot    #
#        Dennis H. Calderon          #
#    calderon-madera.1@osu.edu       #
######################################

#######################################################
"""
=======================
##High_Voltage_Test_Plot.py##
======================
Author: Dennis H. Calderon
Email: calderon-madera.1@osu.edu
Date: July 03, 2022
Modified: July 04, 2022
=======================
Descripiton: 
This PYTHON script will take in 2 csv files of data from the High Voltage 
testing done at Indiana Universiry on July 02, 2022. The test was done for 
both supply 1 (under load) and supply 2 (under load and no load).
Data was taken by hand (Me) for given DAC and voltage reading.
Data was saved from serial output of DAC and ADC_Voltage and ADC_Current 
for POTENTIAL supply and CATHODE supply.

The script will create plots for DAC vs other variables when it can and 
also fit a line and label the paramers when appropiate.

Note:
The files should be prepped using,
 grep | sed > filename.txt
=======================
Usage:
python High_Voltage_Test_Plot.py <filename1> <filename2>

=======================
Options:

=======================
example:
python High_Voltage_Test_Plot.py Supply_1_Load_36M_Ohm.csv large_load_HVSupply1.txt
=======================
"""

#######################################################
import timeit
start = timeit.default_timer()
#######################################################
print("\n")
print('\033[1;37m#\033[0;0m'*50)
print("Now running \033[1;4;5;31mHigh_Voltage_Test_Plot.py\033[0;0m!")
print('\033[1;37m#\033[0;0m'*50)
print('\n')
##########################################
print("\033[1;37mPlease wait patiently...\033[0;0m")
print('Importing libraries...')

##########################################
#System libraries
#import sys
import argparse
#import csv
#import types
#import os
#import warnings
#warnings.filterwarnings("ignore")
#print('...')

#Python libraries
import matplotlib.pyplot as plt
#from matplotlib.lines import Line2D
import numpy as np
#import pandas as pd
print('...')
##########################################

###
parser = argparse.ArgumentParser(
        description='Read filename with list of effective volume errors.')
parser.add_argument("filename", help = "Path to the file you want to use.")
# parser.add_argument("--filename2", "-f2", help = "Path to another file you want to use.")
parser.add_argument("filename2", help = "Path to another file you want to use.")
g = parser.parse_args()

#filename = '/users/PAS0654/dcalderon/Research/GENETIS_Project/Curved_Sides/Effective_Volume_Error_Curved_08.txt'
filename = g.filename
filename2 = g.filename2

#making cleaner name from given filename
name = filename.split('/')[-1].split('.')[0]
name2 = filename2.split('/')[-1].split('.')[0]
#vprint(name)
#vprint(name2)

#exit()
# plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True

##Getting Data##
# columns = ["DAC", "Voltage"]
# df = pd.read_csv(filename, usecols=columns, header=2)
# df = df.astype({"DAC": int, "Voltage": float})
# #print(df.DAC)
# #print(df.Voltage)
# #print(df[0][:])
# #print(df[1][:])
# #exit()

# theta = np.polyfit(df.DAC, df.Voltage, 1)

# print(f'The parameters of the line: {theta}')


# filename = g.filename

# errors = []
# with open(filename) as f:
#     for line in f:
#         errors.append(line.split()[-1])


# var_dict['{0}'.format(var[k])].append(all_var[k])
#         data_dict['{0}'.format(source_names[i])] = var_dict
#                 var_dict['{0}'.format(x)] = []
#data_dict = {'P': [], 'C': []}

#Creates a dictionary of all the data
data_dict = {'P': {'DAC': [], 'ADC_Voltage': [], 'ADC_Current': []},
                  'C': {'DAC': [], 'ADC_Voltage': [], 'ADC_Current': []},
                  'HV': {'DAC': [], 'Voltage': []}}
#P = []
#C = []

#print(data_dict['P']['DAC'])
#print(data_dict)
#exit() 

# with open(filename) as f:
#     a = [f.readline() for i in range(3,)]
#     print(a)
#     #next(f)
#     #next(f)
#     #print(f)
#     exit()
#     for i, line in enumerate(f,3):
#         #print(line)
#         print(i)
#         print(line)
#         #exit()
#         #data_dict['HV']['DAC'].append(line.split(',')[0])
#         #data_dict['HV']['Voltage'].append(line.split(',')[1])

# print(data_dict)
# exit()

#Reads data from first file and appends to dictionary
with open(filename) as f:
    for line in f:
        HV = [float(value) for value in line.split(',')]
        data_dict['HV']['DAC'].append(HV[0])
        data_dict['HV']['Voltage'].append(HV[1])
        # print(HV)
        # print(HV[0])
        # print(type(HV[0]))
        # print(HV[1])
        # print(type(HV[1]))
        # print(type(HV))

# x = data_dict['HV']['DAC']
# y = data_dict['HV']['Voltage']

# # x = np.array(HV[0])
# # y = np.array(HV[1])
# print(data_dict['HV']['Voltage'])
# z = np.polyfit(x, y, 1)

#print(type(HV[0]))
#z = np.polyfit(HV[0], HV[1], 1)
# print(z)
# exit()
#        data_dict['HV']['DAC'].append(float(line.split(',')[0]))
#        data_dict['HV']['Voltage'].append(float(line.split(',')[1]))

#Reads data from second file and appends to dictionary        
with open(filename2) as f2:
    for line in f2:
        P = [float(value) for value in line.split()[1].split(',')]
        C = [float(value) for value in line.split()[3].split(',')]
        #print(P)
        #print(C)
        #exit()
        data_dict['P']['DAC'].append(P[0]) 
        data_dict['P']['ADC_Voltage'].append(P[1]) 
        data_dict['P']['ADC_Current'].append(P[2]) 
        data_dict['C']['DAC'].append(C[0]) 
        data_dict['C']['ADC_Voltage'].append(C[1]) 
        data_dict['C']['ADC_Current'].append(C[2]) 
        #data_dict['C'].append(C)#line.split()[3])
        #print(type(data_dict['P']['DAC'][0]))
        #exit()
#print(data_dict)
# print(data_dict['P']['DAC'])

#print(pd.DataFrame.from_dict(data_dict))

#exit()
# Now, calculating the y-axis values against x-values according to
# the parameters theta0, theta1 and theta2

#Define a plotting function to make scatter plot and fit a line to it
def plotter(x, y, name, xlabel='x_val', ylabel='y_val', supply='HV'):
    '''
    Simple plot maker. Will make a scatter plot and 
    fit the data with numpy.polyfit()
    '''
    print("Plotting...")
    print(x)
    print(y)
    print(type(x))
    print(type(y))
    theta = np.polyfit(x, y, 1)
    y_line = theta[1] + theta[0] * np.array(x)
    
    plt.figure(1, figsize = (8,6))
    plt.scatter(x,y)
    plt.plot(x,y_line,'r')
    
    plt.title("{0}".format(name))
    plt.xlabel(xlabel, labelpad = 0.5, fontsize = 10)
    plt.ylabel(ylabel, labelpad = 0.5, fontsize = 10)
    plt.grid(visible=True, which='both', axis='both',linestyle='--', linewidth=0.5)
    # plt.grid(linestyle='--', linewidth=0.5)

    ax = plt.gca()
    plt.text(0.1,0.8, "y = {0:5.3f} x + {1:5.3f}".format(theta[0],theta[1]),
             transform = ax.transAxes, size=10, color="red")
    plt.savefig("test_plots/{0}_{1}_{2}_{3}.png".format(name,supply,xlabel,ylabel),dpi=300)
    plt.clf()
    print("Done!")

    return
#exit()    

theta = np.polyfit(data_dict['HV']['DAC'], data_dict['HV']['Voltage'], 1)
print(theta)
print(theta[1])
#exit()

# plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Voltage'], 
#         name, xlabel='DAC', ylabel='ADC_Voltage', supply='P')
# plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Current'], 
#         name, xlabel='DAC', ylabel='ADC_Current', supply='P')
#########
##Plots##
#########

#Makes plot from 'HV' (data taken by hand)    
plotter(data_dict['HV']['DAC'], data_dict['HV']['Voltage'], 
        name, xlabel='DAC', ylabel='Voltage', supply='HV')

#Need a try and except block because it can't fit a line if data is 0
#Will be 0 if we weren't recording for correct supply
#Supply1 = POTENTIAL & Supply2 = CATHODE
try:
    plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Voltage'], 
            name, xlabel='DAC', ylabel='ADC_Voltage', supply='P')
    plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Current'], 
            name, xlabel='DAC', ylabel='ADC_Current', supply='P')
    
    plotter(data_dict['C']['DAC'], data_dict['C']['ADC_Voltage'], 
            name, xlabel='DAC', ylabel='ADC_Voltage', supply='C')
    plotter(data_dict['C']['DAC'], data_dict['C']['ADC_Current'], 
            name, xlabel='DAC', ylabel='ADC_Current', supply='C')
    
except ValueError:
    try:
        plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Voltage'], 
                name, xlabel='DAC', ylabel='ADC_Voltage', supply='P')
        plotter(data_dict['P']['DAC'], data_dict['P']['ADC_Current'], 
                name, xlabel='DAC', ylabel='ADC_Current', supply='P')
    except ValueError:
        try:
            plotter(data_dict['C']['DAC'], data_dict['C']['ADC_Voltage'], 
                    name, xlabel='DAC', ylabel='ADC_Voltage', supply='C')
            plotter(data_dict['C']['DAC'], data_dict['C']['ADC_Current'], 
                    name, xlabel='DAC', ylabel='ADC_Current', supply='C')
        except IndexError:
            print("Event")
            #exit()
    #continue
        # except ValueError:
        #     continue    
    

# theta = np.polyfit(data_dict['HV']['DAC'], data_dict['HV']['Voltage'], 1)
# y_line = theta[1] + theta[0] * np.array(data_dict['HV']['DAC'])

# # Plotting the data points and the best fit line
# # plt.scatter(X, y)
# plt.plot(data_dict['HV']['DAC'], y_line, 'r')
# # plt.title('Best fit line using numpy.polyfit()')
# # plt.xlabel('x-axis')
# # plt.ylabel('y-axis')

# # plt.show()
# #from matplotlib import rcParams

# #plt.rcParams['text.usetex'] = True
# #:,.0f
# # print("Contents in csv file:\n", df)
# ##Plotting##
# plt.figure(1, figsize=(8,6))
# plt.scatter(data_dict['HV']['DAC'],data_dict['HV']['Voltage'])
# plt.xlabel('DAC', labelpad = 0.5, fontsize = 10)
# plt.ylabel('Voltage', labelpad = 0.5, fontsize = 10)
# plt.grid(visible=True, which='both', axis='both',linestyle='--', linewidth=0.5)
# #plt.grid(linestyle='--', linewidth=0.5)
# plt.title("{0}.png".format(name))
# ax = plt.gca()
# plt.text(0.1,0.8, "y = {0:5.3f} x + {1:5.3f}".format(theta[0],theta[1]),
#          transform = ax.transAxes, size=10, color="red")
# #plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
# # plt.savefig("{0}.png".format(name),dpi=300)
# # plt.show()



##End of script##
stop = timeit.default_timer()
print('Time: \033[1;31m{0}\033[0;0m'.format(stop - start))
exit()
