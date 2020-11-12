import requests
from Utility.readConfigData import ReadConfig
import unittest
import HtmlTestRunner



""" passing the user/pwd as invalid and verifying the behavior"""  
class getToken_InvalidUser(unittest.TestCase):
         
    def setUp(self):
        self.TokenUrl=ReadConfig.getTokenApi()
        self.InvaliduserName=ReadConfig.getInvalidUser()
        self.Invalidpwd=ReadConfig.getInvalidPwd()
        self.username=ReadConfig.getUsername()
         
      
    def getResponse_InvalidUser(self):
        self.response=requests.get(self.TokenUrl, auth=(self.InvaliduserName, self.Invalidpwd))
        return self.response
    
         
    def test_Verify_Status_InvalidUser(self):
        response=self.getResponse_InvalidUser()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
         
    def test_Verify_Header_InvalidUser(self):
        response=self.getResponse_InvalidUser()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify_message_InvalidUser(self):
        response=self.getResponse_InvalidUser()
        response_body = response.json()  
        assert response_body["message"]== "Invalid User"
         
    def test_Verify_ResponseStatusCode_InvalidUser(self):
        response=self.getResponse_InvalidUser()
        assert response.status_code== 401
         
    def getResponse_NoUser(self):
        self.response=requests.get(self.TokenUrl, auth=(None, self.Invalidpwd))
        return self.response
     
    def test_Verify_Status_NoUser(self):
        response=self.getResponse_NoUser()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
         
    def test_Verify_Header_NoUser(self):
        response=self.getResponse_NoUser()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify_message_NoUser(self):
        response=self.getResponse_NoUser()
        response_body = response.json()  
        assert response_body["message"]== "Invalid User"
         
    def test_Verify_ResponseStatusCode_NoUser(self):
        response=self.getResponse_NoUser()
        assert response.status_code== 401
         
    def getResponse_InvalidPwd(self):
        self.response=requests.get(self.TokenUrl, auth=(self.username, self.Invalidpwd))
        return self.response
     
    def test_Verify_Status_InvalidPwd(self):
        response=self.getResponse_InvalidPwd()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
         
    def test_Verify_Header_InvalidPwd(self):
        response=self.getResponse_InvalidPwd()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_Verify_message_InvalidPwd(self):
        response=self.getResponse_InvalidPwd()
        response_body = response.json()  
        assert response_body["message"]== "Invalid Authentication"
         
    def test_Verify_ResponseStatusCode_InvalidPwd(self):
        response=self.getResponse_InvalidPwd()
        assert response.status_code== 401   
        
    """ Validating the response with no authentication """
    
    def getResponse_withOutAuthentication(self):
        self.response=requests.get(self.TokenUrl)
        return self.response
    
    def test_VerifyStatus_withOutAuthentication(self):
        response=self.getResponse_withOutAuthentication()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
         
    def test_VerifyHeader_withOutAuthentication(self):
        response=self.getResponse_withOutAuthentication()
        assert response.headers["Content-Type"] == "application/json"
         
    def test_VerifyMessage_withOutAuthentication(self):
        response=self.getResponse_withOutAuthentication()
        response_body = response.json()  
        assert response_body["message"]== "Invalid User"
         
    def test_Verify_withOutAuthentication(self):
        response=self.getResponse_withOutAuthentication()
        assert response.status_code== 401   
        
    
     
if __name__ == '__main__':
    unittest.main()
     
       
        
        