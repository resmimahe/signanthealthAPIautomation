import requests 
from Utility.readConfigData import ReadConfig
import unittest
import json
import jsonpath

""" This test suite validate all the expected behavior of updating the values using Userinfo API
     with valid token and username,Invalid token and invalid username"""


class UpdateUserInfo(unittest.TestCase):
    """ The setUp() method would get all the test data required for the validation from congig file,
     which inturn help in managing the test data easily without directly implementing them into the
      code""" 
       
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
        """ This method would return the token """ 
        self.response=requests.get(self.TokenUrl, auth=(self.userName, self.pwd))
        self.json_format=json.loads(self.response.text)
        token=jsonpath.jsonpath(self.json_format, "token")
        return (token[0])
    
    def getHeaders(self):
        """ This method would return the header with updated token value from the above method"""
        self.headers = {
             'Content-Type' : 'application/json',
            'Token': self.getToken()
          }
        return  self.headers 
    
    def putData(self):
        """This method would return the new data to be updated """
        self.payload={'firstname': 'testfirstname',
                      'lastname': 'testlastname',
                      'phone': 'testphone'}
        return self.payload
    
    
    
    def putUserDetails(self):
        """ putUserDetails() will return the update response"""
        self.response=requests.put(self.UserDetailsUrl, data=self.putData(),headers=self.getHeaders())
        return self.response
    
    """ Validating the response above response""" 
        
         
    def test_Verify_ResponseStatusCode(self):
        """ Verifying the update by checking the status code"""
        response=self.putUserDetails()
        if(response.status_code== 201):
            assert True
            print("Successfully updated")
        elif(response.status_code== 400):
            assert False 
            print("Updation failed")
        else:
            raise Exception
    
            
    """ User trying to update field other than firstname,lastname and phone"""  
      
    def putData_OtherFields(self):
        """This method would return the new data to be updated """
        self.payload={"username":"newuser", "password":"Demo123"}
        return self.payload
    
    
    
    def putUserDetails_OtherFields(self):
        """ putUserDetails() will return the update response"""
        self.response=requests.put(self.UserDetailsUrl, data=self.putData_OtherFields(),headers=self.getHeaders())
        return self.response
    
    """ Validating the response of trying to update other fields""" 
    
    def test_Verify_ResponseStatusCode_OtherFields(self):
        """ Verifying the update by checking the status code"""
        response=self.putUserDetails_OtherFields()
        if(response.status_code== 403):
            assert True
        if(response.status_code== 400):
            assert False 
        
    
#     def test_Verify_Status_OtherFields(self):
#         response=self.putUserDetails_OtherFields()
#         response_body = response.json()
#         if(response_body["status"] == "FAILURE"):
#             assert True
#         else:
#             assert False
#         
#     def test_Verify_message_OtherFields(self):
#         response=self.putUserDetails()
#         response_body = response.json()
#         if(response_body["message"] == "Field update not allowed"):
#             assert True
#         else:
#             assert False 
      
        
    """ Validating the behavior after trying to update the value with out passing the token""" 
    
    def putUserDetail_withoutToken(self):
        self.response=requests.put(self.UserDetailsUrl, data=self.putData())
        return self.response
        
    def test_Verify_ResponseStatusCode_WithoutToken(self):
        response=self.putUserDetail_withoutToken()
        assert response.status_code== 401
    
    def test_Verify_Status_WithoutToken(self):
        response=self.putUserDetail_withoutToken()
        response_body = response.json()
        assert response_body["status"] == "FAILURE"
        
    def test_Verify_message_WithoutToken(self):
        response=self.putUserDetail_withoutToken()
        response_body = response.json()
        assert response_body["message"] == "Token authentication required"
            
    def test_Verify_Header_WithoutToken(self):
        response=self.putUserDetail_withoutToken()
        assert response.headers["Content-Type"] == "application/json"      
        
        
if __name__ == '__main__':
    unittest.main()   