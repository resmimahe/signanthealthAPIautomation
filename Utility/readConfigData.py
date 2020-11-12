import configparser
from builtins import staticmethod

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

""" This methods are for reading the API urls,username,password,firstname,lastname,phone from config file """

class ReadConfig:
    @staticmethod
    def getTokenApi():
        getToken=config.get("Common Info","getToken_Api")
        return getToken
    
    @staticmethod
    def getUsersApi():
        getUsers=config.get("Common Info","getUsers_Api")
        return getUsers
    
    
    @staticmethod
    def getUserDetailsApi():
        getUserDetails=config.get("Common Info","getUserDetails_Api")
        return getUserDetails 
    
    @staticmethod
    def getUsername():
        Username=config.get("Common Info","username")
        return Username 
    
    @staticmethod
    def getPassword():
        Password=config.get("Common Info","passwod")
        return Password
     
    @staticmethod
    def getInvalidUser():
        InvalidUser=config.get("Common Info","Invaliduser")
        return InvalidUser 
    
    @staticmethod
    def getInvalidPwd():
        InvalidPwd=config.get("Common Info","InvalidPwd")
        return InvalidPwd 
    
    @staticmethod
    def getfirstname():
        firstname=config.get("Common Info","firstname")
        return firstname
    
    @staticmethod
    def getLastName():
        lastname=config.get("Common Info","lastname")
        return lastname
    @staticmethod
    def getPhoneNumber():
        phone=config.get("Common Info","phone")
        return phone
   