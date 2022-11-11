from os import environ
from pydantic import BaseSettings

class Config(BaseSettings):
    def __init__(self):
        self.path = environ.get("path")

class Person():
    def __init__(self):
        self.age = 30
        self.name = 'John'

# p1 = Person()
# print(p1.age)

conf = Config()
print(conf.path)
