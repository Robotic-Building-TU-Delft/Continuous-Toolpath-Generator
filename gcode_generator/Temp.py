"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "maxla"
__version__ = "2021.03.18"

import rhinoscriptsyntax as rs
import os

#Global Variables:
gCode = []
startCode = []
endCode = []
ptStart = Pt[0]
ptEnd = Pt[len(Pt)-1]
ptApproach = rs.CreatePoint(0, 0, 400)
curDir = os.getcwd()
print(curDir)
print(ptEnd)


#Printer specific start code:
#if printer == 0:
#     with open('curDir' + '/Start/' + 'Creality_CR-X.txt', 'r') as startFile
#        startContent = startFile.readLines()

