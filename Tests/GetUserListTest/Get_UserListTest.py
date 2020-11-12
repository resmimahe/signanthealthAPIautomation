import requests 
from Utility.readConfigData import ReadConfig
import unittest
import json
import jsonpath

""" This test suite validate all the expected behavior of getting the values using GetUsersList API with valid token,without token, invalid token"""

""" The setUp() method would get all the test data required for the validation from congig file, which inturn help in managing the test data easily without directly implementing them into the code""" 
class GetUserList(unittest.TestCase):
  
       
    def setUp(self):
        self.TokenUrl=ReadConfig.getTokenApi()
        self.GetUsersUrl=ReadConfig.getUsersApi()
        self.userName=ReadConfig.getUsername()
        self.pwd=ReadConfig.getPassword()
        
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
    
    def getUserList(self):
        self.response=requests.get(self.GetUsersUrl,headers=self.getHeaders())
        return self.response
    
    """ Validating the response """
        
         
    def test_Verify_ResponseStatusCode(self):
        response=self.getUserList()
        assert response.status_code== 200
        
    def test_Verify_Status(self):
        response=self.getUserList()
        response_body = response.json()
        assert response_body["status"] == "SUCCESS"
        
    def test_Verify_Header(self):
        response=self.getUserList()
        assert response.headers["Content-Type"] == "application/json"    
            
        
    """ Validating the behavior with out passing the token""" 
    
    def getUserList_withoutToken(self):
        self.response=requests.get(self.GetUsersUrl)
        return self.response
    
        
    def test_Verify_ResponseStatusCode_WithoutToken(self):
        response=self.getUserList_withoutToken()
        if response.status_code== 401:
            assert True
        if  response.status_code== 200:
            assert False   
    
    
    def test_Verify_Status_WithoutToken(self):
        response=self.getUserList_withoutToken()
        response_body = response.json()
        if  response_body["status"] == "FAILURE":
            assert True
        if  response_body["status"] == "SUCCESS":
            assert True
        
        
            
    def test_Verify_Header_WithoutToken(self):
        response=self.getUserList_withoutToken()
        assert response.headers["Content-Type"] == "application/json"      
        
        
if __name__ == '__main__':
    unittest.main()   