import requests 
from Utility.readConfigData import ReadConfig
import unittest
import json
import jsonpath

""" This test suite validate all the expected behavior of Userinfo API with invalid token and ,or invalid username"""

class getUserInfo_InvalidData(unittest.TestCase):
        
    def setUp(self):
        """ This method get all the testdata required from config file"""
        self.TokenUrl=ReadConfig.getTokenApi()
        self.userName=ReadConfig.getUsername()
        self.pwd=ReadConfig.getPassword()
        self.InvaliduserName=ReadConfig.getInvalidUser()
        self.UserInfoUrl=ReadConfig.getUserDetailsApi()
        self.UserDetailsUrl_Invalid=self.UserInfoUrl+self.InvaliduserName
        self.UserDetailsUrl=self.UserInfoUrl+self.userName
        
        
    def getToken(self):
        """ This method return token"""
        self.response=requests.get(self.TokenUrl, auth=(self.userName, self.pwd))
        self.json_format=json.loads(self.response.text)
        token=jsonpath.jsonpath(self.json_format, "token")
        return (token[0])
    
    def getHeaders_invalidUser(self):
        """ This method return the header created for sending in User details API"""
        self.headers = {
             'Content-Type' : 'application/json',
            'Token': self.getToken()
          }
        return  self.headers 
    
    def getUserDetails_invalidUser(self):
        """ This method return the response of invalid user passed in the Url"""
        self.response=requests.get(self.UserDetailsUrl_Invalid, headers=self.getHeaders_invalidUser())
        return self.response
       
    def test_Verify__invalidUser_ResponseStatusCode(self):
        """This method validating whether the status code is 404 as expected """
        response=self.getUserDetails_invalidUser()
        if(response.status_code== 500):
            assert False
        elif(response.status_code== 404):
            assert True
            
        
    """ Verifying the below scenarios by passing invalid token as a header to the userinfo api with valid userId"""
    
    def getHeaders_invalidToken(self):
        self.headers = {
             'Content-Type' : 'application/json',
            'Token': "dummyToken"
          }
        return  self.headers 
    
    def getUserDetails_invalidToken(self):
        self.response=requests.get(self.UserDetailsUrl, headers=self.getHeaders_invalidToken())
        return self.response
   
    
    def test_Verify__invalidToken_Status(self):
        response=self.getUserDetails_invalidToken()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
    
    def test_Verify__invalidToken_message(self):
        response=self.getUserDetails_invalidToken()
        response_body = response.json()
        assert response_body["message"] == "Invalid Token"    
        
    def test_Verify_Header_InvalidToken(self):
        response=self.getUserDetails_invalidToken()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify__invalidToken_ResponseStatusCode(self):
        response=self.getUserDetails_invalidToken()
        assert response.status_code== 401
        
    """Verifying the behavior of sending the request with no token in the header """
        
    def getUserDetails_NoToken(self):
        self.response=requests.get(self.UserDetailsUrl)
        return self.response
    
    def test_Verify__withNoToken_Status(self):
        response=self.getUserDetails_invalidToken()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
    
    def test_Verify__withNoToken_message(self):
        response=self.getUserDetails_invalidToken()
        response_body = response.json()
        assert response_body["message"] == "Token authentication required"    
        
    def test_Verify_Header_withNoToken_message(self):
        response=self.getUserDetails_invalidToken()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify__withNoToken_message_ResponseStatusCode(self):
        response=self.getUserDetails_invalidToken()
        assert response.status_code== 401
if __name__ == '__main__':
    unittest.main()   