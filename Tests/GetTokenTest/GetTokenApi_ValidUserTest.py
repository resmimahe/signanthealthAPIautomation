import requests 
from Utility.readConfigData import ReadConfig
import unittest
import json
import jsonpath

class getToken(unittest.TestCase):
        
    def setUp(self):
        self.TokenUrl=ReadConfig.getTokenApi()
        self.userName=ReadConfig.getUsername()
        self.pwd=ReadConfig.getPassword()
        
    def getResponse(self):
        self.response=requests.get(self.TokenUrl, auth=(self.userName, self.pwd))
        return self.response
    
    def test_getToken_ValidUser(self):
        print(json.dumps(self.getResponse().json(),indent=4))
        self.json_format=json.loads(self.getResponse().text)
        token=jsonpath.jsonpath(self.json_format, "token")
        print(token[0])
        
    def test_Verify_Status(self):
        response=self.getResponse()
        response_body = response.json()
        assert response_body["status"] == "SUCCESS"
        
    def test_Verify_Header(self):
        response=self.getResponse()
        assert response.headers["Content-Type"] == "application/json"
        
    def test_Verify_ResponseStatusCode(self):
        response=self.getResponse()
        assert response.status_code== 200
        



if __name__ == '__main__':
    unittest.main()
    
    
        
        