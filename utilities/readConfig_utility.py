#write function for each data

import configparser

config = configparser.RawConfigParser()  #create object

config.read(".\\Configurations\\config.ini") #give path of the config file

class readconfig_class:       #create readconfig class using static methods for importing data from config.ini file
    @staticmethod
    def username_data():
        username = config.get("login data","username")
        return username

    @staticmethod
    def password_data():
        password = config.get("login data","password")
        return password

    @staticmethod
    def base_url():
        base_url = config.get("Application url","base_url")
        return base_url

    @staticmethod
    def login_url():
        login_url = config.get("Application url","login_url")
        return login_url

    @staticmethod
    def signup_url():
        signup_url = config.get("Application url","signup_url")
        return signup_url
