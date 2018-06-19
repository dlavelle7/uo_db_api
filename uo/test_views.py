from django.test import TestCase

from uo.models import User


class TestUsersView(TestCase):

    @classmethod
    def setUpTestData(cls):
        auth_user = User.objects.create(
            username="lola",
            password="rabbit",
        )
        cls.auth_headers = f"Token {auth_user.auth_token}"

    def test_users_view(self):
        # Create a user via the POST endpoint, no auth required
        data = {"username": "test", "password": "testpass"}
        create_user_1 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_1.status_code)
        self.assertEqual(data["username"], create_user_1.data["username"])

        # Create a second user
        data = {"username": "test2", "password": "testpass2"}
        create_user_2 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_2.status_code)
        self.assertEqual(data["username"], create_user_2.data["username"])

        # Test detailed user view, auth required
        get_user_2 = self.client.get(f'/uo/users/{create_user_2.data["id"]}',
                                     HTTP_AUTHORIZATION=self.auth_headers)
        self.assertEqual(200, get_user_2.status_code)
        self.assertEqual(get_user_2.data, create_user_2.data)

        # Test list users view, 3 now returned, auth required
        get_users = self.client.get('/uo/users',
                                    HTTP_AUTHORIZATION=self.auth_headers)
        self.assertEqual(3, get_users.data["count"])
        self.assertEqual(get_users.data["results"][-1]["username"],
                         data["username"])

    def test_obtain_token_view(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)

        # Assert token gets auto generated for that user, no auth required
        token_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_response.status_code)
        self.assertIn("token", token_response.data)

        # Create a second user
        data = {"username": "test2", "password": "testpass2"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)

        # Assert a new different token is auto generated, no auth required
        token_2_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_2_response.status_code)
        self.assertNotEqual(token_response.data["token"],
                            token_2_response.data["token"])
