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
    value[1]=getLD()
    value[2]=getRD()
    value[3]=getCL()
    value[4]=getML()
    value[5]=getLI()
    value[6]=getLO()
    value[7]=getRI()
    value[8]=getRO()
    value[9]=getGS()
    return value


def getInputOverload(ld,rd,cl,ml,li,lo,ri,ro,gs):
    '''
    overloaded method for getInput that allows all values to be set at the 
    same time
    '''
    value = {}
    print('Left dashboard switch (0 or 1):',ld)
    value[1]=ld
    print('Right dashboard switch (0 or 1):',rd)
    value[2]=rd
    print('child lock switch (0 or 1):',cl)
    value[3]=cl
    print('Master unlock switch (0 or 1):',ml)
    value[4]=ml
    print('Left inner switch (0 or 1):',li)
    value[5]=li
    print('Left outer switch (0 or 1):',lo)
    value[6]=lo
    print('Right inner switch (0 or 1):',ri)
    value[7]=ri
    print('Right outer switch (0 or 1):',ro)
    value[8]=ro
    print('Gear shift position (P, N, D, 1, 2, 3, or R):',gs)
    value[9]=gs
    return value


def checkDoors(doors):
    '''
    checks to see if the doors of a vehicle can open depending on switches
    Args:
        doors is a dict or list storing switch values
    '''
    if doors[3] == 0 and doors[4] == 1 and doors[9] == 'P':
        print('Both doors open')
    elif doors[9] != 'P':
        print('Both doors stay closed')
    elif doors[4] == 0:
        if doors[2] == 1:
            print('left door opens')
        elif doors[3] == 1:
            print('right door opens')
        else:
            print('Both doors stay closed')
    else:
        print('Both doors stay closed')
        



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
            ML = int(input('Master unlock switch (0 or 1):'))
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
    GS = input('Gear shift position (P, N, D, 1, 2, 3, or R):')
    GS = GS.capitalize()
    if GS == 'P' or GS == 'N' or GS == 'D' or GS == '1' or GS == '2' or GS == '3' or GS == 'R':
        return GS
    else:
        print('Invalid Record: ')
        return GS
    



# Main Function
def main():
    #options()
    checkDoors(getInput())
    return

if __name__ == '__main__':
    #Call Main
    main()
    exit(0)
