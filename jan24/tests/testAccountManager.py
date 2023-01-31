import AccountManager
from unittest import TestCase

class Tester(TestCase):
    def test_verifyUser(self):
        A = AccountManager.AccountManager()
        self.assertFalse( A.verifyUser( "bob", "s3cr3t"),
            "should return false if user doesn't exist")

    def test_verifyUser2(self):
        A = AccountManager.AccountManager()
        A.addUser("alice","qwerty")
        self.assertTrue( A.verifyUser( "alice", "qwerty"),
            "should return True if user does exist and password does match")

    def test_verifyUser3(self):
        A = AccountManager.AccountManager()
        self.assertTrue( A.verifyUser( "alice", "s3cr3t"),
            "should return false if password doesn't match")

    def test_verifyUser4(self):
        A = AccountManager.AccountManager()
        self.assertTrue( A.verifyUser( "bob", "qwerty"),
            "should return false if user doesn't exist and password does match")

    def test_verifyUser5(self):
        A = AccountManager.AccountManager()
        #test for missing parameters
        self.assertRaises( Exception, A.verifyUser )

    def test_addUser(self):
        A = AccountManager.AccountManager()
        self.assertFalse( A.verifyUser( "bob", "s3cr3t") )
        self.assertTrue( A.addUser("bob","s3cr3t") )
        self.assertTrue( A.verifyUser( "bob", "s3cr3t") )

    def test_add2(self):
        #see if adding duplicate returns false
        A = AccountManager.AccountManager()
        self.assertTrue( A.addUser("alice","qwerty") )
        self.assertFalse( A.addUser("alice","qwerty") )
        self.assertFalse( A.addUser("alice","secret") )

    def test_add(self):
        A = AccountManager.AccountManager()
        self.assertFalse(A.addUser("bprob34", "secret"))