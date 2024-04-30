import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod  # so that we can call this method using class name instead of object
    def getApplicstionURL():
        url=config.get("Login Info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        username=config.get("Login Info", "username")
        return username

    @staticmethod
    def getPassword():
        password=config.get("Login Info", "password")
        return password
