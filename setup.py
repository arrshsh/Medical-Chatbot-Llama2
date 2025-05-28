# this is done to make the local package, so that we can import stuffs from src folder 
# for example, if we wanna do :
# from src.helper import main
# it'll throw an error until we dont make a local package of src

from setuptools import find_packages, setup

setup(
    name = "End-to-end Financial Chatbot",
    version = "0.0.0",
    author= "Mohammad Arsh Vahora",
    author_email= "vahora4@uwindsor.ca",
    packages= find_packages(), # this looks for the constructor file i.e. __init__.py in each folder and wherever it finds that, that folder is made into a package
    install_requires = []
)