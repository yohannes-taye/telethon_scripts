#!/usr/bin/env python3
class UserState:
    START = 0
    SEND_QR_CODE = 1 
    QR_CODE_SCANED = 2 
    def __init__(self,userId):
        self.userId = userId
        self.page = 0
        self.qrCodeSaveLocation = ''
    def setUserId(self, userId):
        self.userId = userId
    def setPage(self, page): 
        self.page = page
    def getPage(self): 
        return self.page 
    def nextPage(self): 
        self.page += 1
    def prevPage(self): 
        self.page -= 1
    def setQrCodeAdress(self, saveLocation): 
        self.qrCodeSaveLocation = saveLocation