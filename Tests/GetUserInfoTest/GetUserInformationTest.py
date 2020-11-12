import requests 
from Utility.readConfigData import ReadConfig
import unittest
import json
import jsonpath

""" This test suite validate all the expected behavior of Userinfo API with valid token and username"""

""" The setUp() method would get all the test data required for the validation from congig file, which inturn help in managing the test data easily without directly implementing them into the code""" 
class getUserInfo(unittest.TestCase):
  
       
    def setUp(self):
        self.TokenUrl=ReadConfig.getTokenApi()
        self.UserInfoUrl=ReadConfig.getUserDetailsApi()
        self.userName=ReadConfig.getUsername()
        self.pwd=ReadConfig.getPassword()
        self.UserDetailsUrl=self.UserInfoUrl+self.userName
        self.FirstName=ReadConfig.getfirstname()
        self.LastName=ReadConfig.getLastName()
        self.Phone=ReadConfig.getPhoneNumber()
        
    def getToken(self):
        self.response=requests.get(self.TokenUrl, auth=(self.userName, self.pwd))
        self.json_format=json.loads(self.response.text)
        token=jsonpath.jsonpath(self.json_format, "token")
        return (token[0])
    
    def getHeaders(self):
        self.headers = {
             'Content-Type' : 'application/json',
            'Token': self.getToken()
          }
        return  self.headers 
    
    """ getUserDetails() will return the user details"""
    
    def getUserDetails(self):
        self.response=requests.get(self.UserDetailsUrl, headers=self.getHeaders())
        return self.response
    
    """ Validating the json response """
        
    def test_Verify_Status(self):
        response=self.getUserDetails()
        response_body = response.json()
        assert response_body["status"] == "SUCCESS"
        
    def test_Verify_message(self):
        response=self.getUserDetails()
        response_body = response.json()
        assert response_body["message"] == "retrieval succesful"
        
        
    def test_Verify_the_User_Firstname(self):
        response=self.getUserDetails()
        response_body = response.json()
        assert response_body["payload"]["firstname"] == self.FirstName
        
    def test_Verify_the_User_Lastname(self):
        response=self.getUserDetails()
        response_body = response.json()
        assert response_body["payload"]["lastname"] == self.LastName
          
    def test_Verify_the_User_Phone(self):
        response=self.getUserDetails()
        response_body = response.json()
        assert response_body["payload"]["phone"] == self.Phone   
        
    def test_Verify_Header(self):
        response=self.getUserDetails()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify_ResponseStatusCode(self):
        response=self.getUserDetails()
        assert response.status_code== 200
        
if __name__ == '__main__':
    unittest.main()   