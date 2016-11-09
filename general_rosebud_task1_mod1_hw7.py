#!/usr/bin/env python3
'''
Module 1 of assignment 7
'''
import sys


def options():
    '''
    Prints options for input
    '''
    print('Left dashboard switch (LD)\nRight dashboard switch(RD)\nChild lock switch (CL)\nMaster unlock switch (ML)\nLeft inside handle (LI)\nLeft outside handle (LO)\nRight inside handle (RI)\nRight outside handle (RO)\nGear shift position (GS): valid Fields: P, N, D, 1, 2, 3, or R')
    

def getInput():
    '''
    gets the input values for all the different doors, switches, handles, 
    and Gear positions
    '''
    value = {}
    value['left dash']=getLD()
    value['right dash']=getRD()
    value['child lock']=getCL()
    value['master lock']=getML()
    value['left inner']=getLI()
    value['left outer']=getLO()
    value['right inner']=getRI()
    value['right outer']=getRO()
    value['gear status']=getGS()
    return value


def getInputOverload(ld,rd,cl,ml,li,lo,ri,ro,gs):
    '''
    overloaded method for getInput that allows all values to be set at the 
    same time
    '''
    value = {} 
    value['left dash']=ld
    value['right dash']=rd
    value['child lock']=cl
    value['master unlock']=ml
    value['left inner']=li
    value['left outer']=lo
    value['right inner']=ri
    value['right outer']=ro
    value['gear status']=gs
    return value


def checkDoors(doors):
    '''
    checks to see if the doors of a vehicle can open depending on switches
    Args:
        doors is a dict storing switch values
    '''
    if doors['gear status'] == 'P' and doors['master unlock'] == 1:
        if doors['child lock'] == 0:
            pass
   



def getLD():
    '''
    gets left dashboard switch with error handling
    '''
    while True:
        try:
            LD = int(input('Left dashboard switch (0 or 1):'))
            if LD == 0 or LD == 1:
                return LD
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')

def getRD():
    '''
    gets right dashboard switch with error handling
    '''
    while True:
        try:
            RD = int(input('Right dashboard switch (0 or 1:'))
            if RD == 0 or RD == 1:
                return RD
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')

def getCL():
    '''
    gets child lock switch with error handling
    '''
    while True:
        try:
            CL = int(input('Child lock switch (0 or 1):'))
            if CL == 0 or CL == 1:
                return CL
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')


def getML():
    '''
    gets master unlock switch with error handling
    '''
    while True:
        try:
            ML = int(input('Master lock switch (0 or 1):'))
            if ML == 0 or ML == 1:
                return ML
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')

def getLI():
    '''
    gets left inside handle with error handling
    '''
    while True:
        try:
            LI = int(input('Left inside handle (0 or 1):'))
            if LI == 0 or LI == 1:
                return LI
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')



def getLO():
    '''
    gets left outside handle with error handling
    '''
    while True:
        try:
            LO = int(input('Left outside handle (0 or 1):'))
            if LO == 0 or LO == 1:
                return LO
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')

def getRI():
    '''
    gets right inside handle with error handling
    '''
    while True:
        try:
            RI = int(input('Right inside handle (0 or 1):'))
            if RI == 0 or RI == 1:
                return RI
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')


def getRO():
    '''
    gets right inside handle with error handling
    '''
    while True:
        try:
            RO = int(input('Right outside handle (0 or 1):'))
            if RO == 0 or RO == 1:
                return RO
        except (TypeError,ValueError):
            print('Input must be a 0 or 1')
    

def getGS():
    '''
    gets the state of the gear position
    '''
    while True:
        GS = input('Gear shift position (P, N, D, 1, 2, 3, or R):')
        GS = GS.capitalize()
        if GS == 'P' or GS == 'N' or GS == 'D' or GS == '1' or GS == '2' or         GS == '3' or GS == 'R':
            return GS
    
    



# Main Function
def main():
    options()
    print(getInput())
    return

if __name__ == '__main__':
    #Call Main
    main()
    
    exit(0)
