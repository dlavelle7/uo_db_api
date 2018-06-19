from uo.permissions import UsersAccessPermission

from django.test import TestCase
from unittest.mock import Mock


class TestUsersAccessPermission(TestCase):

    def setUp(self):
        self.users_perm = UsersAccessPermission()

    def test_user_access_permission_post(self):
        """Allow post request for annonymouse unauthenticated user."""
        mock_request = Mock(method='POST', user=Mock(is_authenticated=False))
        self.assertTrue(self.users_perm.has_permission(mock_request, Mock()))

    def test_user_access_permission_get(self):
        """Allow get request for authenticated user."""
        mock_request = Mock(method='GET', user=Mock(is_authenticated=True))
        self.assertTrue(self.users_perm.has_permission(mock_request, Mock()))

    def test_user_access_permission_get_2(self):
        """Prohibit get request for unauthenticated user."""
        mock_request = Mock(method='GET', user=Mock(is_authenticated=False))
        self.assertFalse(self.users_perm.has_permission(mock_request, Mock()))
