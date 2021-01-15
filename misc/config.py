import os

from kivy.config import ConfigParser

from misc import user_data_dir

Config = ConfigParser()
Config.read(os.path.join(user_data_dir, "config.ini"))


def create():
    """    for section in Config.sections():
        Config.remove_section(section)

    Config.add_section("Misc")
    Config.add_section("Mining")
    Config.add_section("Gui")
    Config.add_section("Memrise_Element")"""

    Config.set("Mining", "mode", "Ghost")
    Config.set("Mining", "url", "https://app.memrise.com/signin")

    Config.set("Gui", "webpage_image_update_interval", 1)
    #Config.set("Gui", "headless", True)

    Config.set("Memrise_Element", "username_input_id", "username")
    Config.set("Memrise_Element", "password_input_id", "password")
    Config.set("Memrise_Element", "login_submit_button_xpath",
               "/html/body/div[2]/div/div[2]/div/form/div[3]/div[1]/button")

    Config.set("Misc", "saveLogins", True)
    #Config.set("Misc", "username", "")#for testing
    #Config.set("Misc", "password", "")


    with open(os.path.join(user_data_dir, "config.ini"), 'w'):
        Config.write()
