import json
from rest_framework.test import APITestCase
from rest_framework import status



class UsersTestCase(APITestCase):
    
    fixtures = ["test_users"]
    
    def test_user_list(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    
    def test_user_retrieve(self):
        response = self.client.get("/api/users/1/")
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tuple(data.keys()), ("id", "email", "first_name", "last_name"))
        
    
    def test_user_retrieve_404(self):
        response = self.client.get("/api/users/777/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    
    def test_user_create(self):
        user_data = {
            "email": "some@insane.email",
            "password": "some.insane.password",
            "first_name": "Dummy",
            "last_name": "Fake",
        }
        response = self.client.post("/api/users/", user_data)
        data = json.loads(response.content)
        del user_data["password"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tuple(data.keys()), tuple(["id", *user_data.keys()]))
        