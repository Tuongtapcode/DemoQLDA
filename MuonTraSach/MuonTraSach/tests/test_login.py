import unittest
from MuonTraSach import dao

class TestLogin(unittest.TestCase):
    def test_login_1(self):
        self.assertTrue(dao.auth_user("user1", 1))
    def test_login_2(self):
        self.assertFalse(dao.auth_user("user1", 2))


if __name__ == '__main__':
    unittest.main()