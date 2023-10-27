# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct 25 15:24:07 2023

# @author: monika
# """

# # pylab

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    

# # first trial of graph plotting: all graphs plotted into one

# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)
# plt.show()

# # second trial: generating individual graphs with file names associated

# plt.figure('lin')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)
# plt.show()

# # third trial: labelling the axes

#plt.figure('lin')
#plt.xlabel('sample points')
#plt.ylabel('linear function')
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
#plt.figure('quad')
#plt.ylabel('quadratic function')

# fourth trial: adding titles to graphs
#plt.figure('lin')
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')


# # fifth trial: clearing previously opened graph windows

#plt.figure('lin')
#plt.clf()
#plt.plot(mySamples, myLinear)
#plt.figure('quad')
#plt.clf()
#plt.plot(mySamples, myQuadratic)
#plt.figure('cube')
#plt.clf()
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.clf()
#plt.plot(mySamples, myExponential)
#plt.figure('lin')
#plt.title('Linear')
#plt.figure('quad')
#plt.title('Quadratic')
#plt.figure('cube')
#plt.title('Cubic')
#plt.figure('expo')
#plt.title('Exponential')

# # fifth trial: changing limits on axes

# plt.figure('lin')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.clf()
# plt.ylim(0,1000)
# plt.plot(mySamples, myQuadratic)
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')


# # sixth trial: overlaying plots 

# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)

# plt.figure('cube expo')
# plt.clf()
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)
# plt.figure('lin quad')
# plt.title('Linear vs. Quadratic')
# plt.figure('cube expo')
# plt.title('Cubic vs. Exponential')


# # seventh trial: adding more documentation: 
# # by adding a legend that identifies each plot

# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear, label='linear')
# plt.plot(mySamples, myQuadratic, label='quadratic')
# plt.legend(loc='upper right')

# plt.figure('cube expo')
# plt.clf()
# plt.plot(mySamples, myCubic, label='cubic')
# plt.plot(mySamples, myExponential, label='exponential')
# plt.legend()
# plt.title('Cubic vs. Exponential')


# # eighth trial: adding data display styles: 
# # by adding color and plot styles like: dashed, dotted, lined, triangular
# # to identify each plot                                        #k= black

# plt.figure('lin quad')
# plt.clf()
# plt.plot(mySamples, myLinear, 'b-', label='linear') # 'b'=blue, '-'=lined plot
# plt.plot(mySamples, myQuadratic, 'ro', label='quadratic') # 'r'=red, 'o'=circular
# plt.legend(loc='upper right')
# plt.title('Linear vs. Quadratic')

# plt.figure('cube expo')
# plt.clf()
# plt.plot(mySamples, myCubic, 'g^', label='cubic') # g=green, ^=triangle
# plt.plot(mySamples, myExponential, 'r--', label='exponential') # r=red, -- = dashed
# plt.legend()
# plt.title('Cubic vs. Exponential')


# # ninth trial: adding display styles: 
# # by adding subplots: graphs next to each other for comparison
# # sublot takes 3 digit integers as parameters: eg, 211 & 212, where
# # 211 = 2 rows, 1 column, location 1 
# # 212 = 2 rows, 1 column, location 2
# # 121 = 1 row, 2 columns, location 1 
# # 122 = 1 row, 2 columns, location 2

# plt.figure('lin quad')
# plt.clf()
# plt.subplot(211)
# plt.ylim(0,900)
# plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0) # 'b'=blue, '-'=lined plot
# plt.subplot(212)
# plt.ylim(0, 900)
# plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0) # 'r'=red, 'o'=circular
# plt.legend(loc='upper right')
# plt.title('Linear vs. Quadratic')

# plt.figure('cube expo')
# plt.clf()
# plt.subplot(121)
# plt.ylim(0,140000)
# plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0) # g=green, ^=triangle
# plt.subplot(122)
# plt.ylim(0,140000)
# plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0) # r=red, -- = dashed
# plt.legend()
# plt.title('Cubic vs. Exponential')


# # tenth trial: adding log scale to display styles: 
# # by adding color and plot styles like: dashed, dotted, lined, triangular
# # to identify each plot                                        #k= black

plt.figure('cube expo log scale')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic') # g=green, ^=triangle
plt.plot(mySamples, myExponential, 'r', label='exponential') # r=red, -- = dashed
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('cube expo linear scale')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic') # g=green, ^=triangle
plt.plot(mySamples, myExponential, 'r', label='exponential') # r=red, -- = dashed
plt.legend()
plt.title('Cubic vs. Exponential')

plt.show()




