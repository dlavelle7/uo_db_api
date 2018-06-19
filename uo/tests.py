from django.test import TestCase


class TestUsersView(TestCase):

    def test_users_view_basic(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass"}
        create_user_1 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_1.status_code)
        self.assertEqual(data["username"], create_user_1.data["username"])

        # Make a GET request to retrieve the new user
        get_users = self.client.get('/uo/users')
        self.assertEqual(1, get_users.data["count"])
        self.assertEqual(get_users.data["results"][0]["username"],
                         data["username"])

        # Create a second user
        data = {"username": "test2", "password": "testpass2"}
        create_user_2 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_2.status_code)
        self.assertEqual(data["username"], create_user_2.data["username"])

        # Test detailed user view GET
        get_user_2 = self.client.get(f'/uo/users/{create_user_2.data["id"]}')
        self.assertEqual(200, get_user_2.status_code)
        self.assertEqual(get_user_2.data, create_user_2.data)

        # GET users, 2 now returned
        get_users = self.client.get('/uo/users')
        self.assertEqual(2, get_users.data["count"])
        self.assertEqual(get_users.data["results"][1]["username"],
                         data["username"])

    def test_users_token(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)
        # Assert token gets auto generated for that user
        token_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_response.status_code)
        self.assertIn("token", token_response.data)

        # Create a second user
        data = {"username": "test2", "password": "testpass2"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)
        # Assert a new different token is auto generated
        token_2_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_2_response.status_code)
        self.assertNotEqual(token_response.data["token"],
                            token_2_response.data["token"])
