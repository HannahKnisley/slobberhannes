class AccountManager:
    def __init__(self):
        self.users = {}

    def addUser(self, username, password):
        """
        Add a new user to the account database. 
        If duplicate usernameL return False
        Usernmae and password must both be strings: if not:
            throw exeption
        If only parameter is given, then Python throws an exception.
        If it's a Joe account: Reject

        Content of usernam (all letters<---)
        No empty username of password
        length issue: max length of 32
        Password: max length of 100
        """

        #if not username.isalpha(): error
        if username in self.users:
            #already exist, so fail
            return False 
        else:
            self.users[username] = password
            return True


    def verifyUser(self,username,password):
        """username, password are strings
        Returns true if credentials match
        an existing account
        Returns false if not
        If non-string: Return false
        If username is empty or password is empty: Return false
        """
        if type(username) != str or type(password) != str:
            return False 
        if len(username) == 0 or len(password) == 0:
            return False
        return password == self.users.get(username)
