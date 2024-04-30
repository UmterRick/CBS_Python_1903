class BaseLanguage:
    def greeting(self):
        pass


class English(BaseLanguage):

    def greeting(self):
        print("Hello")


class Spanish(BaseLanguage):
    def greeting(self):
        print("Ola")


languages = [English(), Spanish()]


def hello_friend():
    for language in languages:
        language.greeting()
