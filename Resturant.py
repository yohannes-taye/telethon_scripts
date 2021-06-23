#!/usr/bin/env python3
class Resturant:
    
    MENU_TYPE_DRINK = 'DRINK'
    MENU_TYPE_FOOD = 'FOOD'
    MENU_TYPE_SWEET = 'SWEET'

    def __init__(self, resturantId, resturantName):
        self.resturantId = resturantId
        self.name = ''
        self.menu = {} 

    def setResturantrId(self, userId):
        self.userId = userId
    def getResturantId(self): 
        return self.resturantId

    def setResturantName(self, name): 
        self.name = name
    def getResturantName(self): 
        return self.name
    
    def getResturantMenu(menu): 
        return self.menu