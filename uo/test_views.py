from django.test import TestCase

from uo.models import User


class TestUsersView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.auth_user = User.objects.create(
            username="lola",
            password="rabbit",
        )
        cls.auth_headers = f"Token {cls.auth_user.auth_token}"

    def test_create_user_returns_token(self):
        data = {"username": "test", "password": "testpass",
                "email": "test@foo.ie"}
        create_user_1 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_1.status_code)
        self.assertEqual(data["username"], create_user_1.data["username"])
        headers = "Token {0}".format(create_user_1.data["auth_token"])
        # Assert token can be used to access views
        get_users = self.client.get('/uo/users',
                                    HTTP_AUTHORIZATION=headers)
        self.assertEqual(get_users.status_code, 200)

    def test_users_view(self):
        # Create a user via the POST endpoint, no auth required
        data = {"username": "test", "password": "testpass",
                "email": "test@foo.ie"}
        create_user_1 = self.client.post('/uo/users', data=data)
        self.assertEqual(201, create_user_1.status_code)
        self.assertEqual(data["username"], create_user_1.data["username"])
        self.assertEqual(data["email"], "test@foo.ie")

        # Create a second user
        data = {"username": "test2", "password": "testpass2",
                "email": "test2@foo.ie"}
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

    def test_users_view_permissions(self):
        # No token, can't access view
        get_users = self.client.get('/uo/users')
        self.assertEqual(401, get_users.status_code)

    def test_user_view_permissions(self):
        # invalid token, can't access view
        get_user = self.client.get(f'/uo/users/{self.auth_user.id}',
                                   HTTP_AUTHORIZATION=self.auth_headers + "XX")
        self.assertEqual(401, get_user.status_code)

    def test_obtain_token_view(self):
        # Create a user via the POST endpoint
        data = {"username": "test", "password": "testpass",
                "email": "test@foo.ie"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)

        # Assert token gets auto generated for that user, no auth required
        token_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_response.status_code)
        self.assertIn("token", token_response.data)

        # Create a second user
        data = {"username": "test2", "password": "testpass2",
                "email": "test2@foo.ie"}
        response = self.client.post('/uo/users', data=data)
        self.assertEqual(201, response.status_code)

        # Assert a new different token is auto generated, no auth required
        token_2_response = self.client.post('/uo/api-token-auth', data=data)
        self.assertEqual(200, token_2_response.status_code)
        self.assertNotEqual(token_response.data["token"],
                            token_2_response.data["token"])
