"""
User
Admin
Manager
...
"""
import datetime


class BaseUser:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.permission = ["auth", "read"]
        self.created_at = datetime.datetime.now()

    def log_in(self, password):
        if password == self.password:
            print("Success")
        else:
            print("Incorrect Password")

    def log_out(self):
        print("Log out success")


class Manager(BaseUser):

    def __init__(self, email, password):
        # self.email = email
        # self.password = password
        # self.permission = ["auth", "read", "write_article", "delete_artice"]
        super().__init__(email, password)
        self.created_at = None
        self.permission.extend(["write_article", "delete_artice"])


    def create_article(self, text, title, date):
        article = {"text": text, "title": title, "date": date}


class SuperManager(Manager):

    def create_article(self, text, title, article_date):
        pass