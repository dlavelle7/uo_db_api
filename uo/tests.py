from django.test import TestCase


class TestUsersView(TestCase):

    def test_users_view_basic(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(data["username"], response.data["username"])

        # Make a GET request to retrieve the new user
        response = self.client.get('/uo/users')
        self.assertEqual(1, response.data["count"])
        self.assertEqual(response.data["results"][0]["username"],
                         data["username"])

        # Create a second user
        data = {"username": "test2", "password": "testpass2"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(data["username"], response.data["username"])

        # GET users, 2 now returned
        response = self.client.get('/uo/users')
        self.assertEqual(2, response.data["count"])
        self.assertEqual(response.data["results"][1]["username"],
                         data["username"])

    def test_users_token(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(data["username"], response.data["username"])
        # Assert token gets auto generated for that user
        response = self.client.post('/uo/api-token-auth', data=data)
        # TODO:
