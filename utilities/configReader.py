from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read(r'/home/vipulsai/PycharmProjects/API_Task_Management/Configurations/config.ini')
    return config.get(section, key)