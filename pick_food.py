#modules help break our program into pieces so that we can form another layer of abstraction or separate out our program to collaborate and better organize/troubleshoot

#Python calls these modules, but they can also be known as libraries, packages, dependecies
#there are 3 types of modules we work with
# 1 - modules built into python that we import to add functionality - like the random module
# 2 - custom modules that we make ourselves
# 3 - third party modules that we use a package manager like pip in order to use them

#we are going to make a program that helps randomly pick from a list of restaurant choices
#we will both be importing a package from Python and creating one ourselves

#to import a module we use the keyword import 
#we are going to import the random module from the standard python library
#This library can do a bunch of things with randomness - generate random numbers, randomly choose items from a list, etc...
#we can also import just the functions we want from the random library for use to use
#random documentation - https://docs.python.org/3/library/random.html

#syntax is from module/library import function
from random import choice

#list of restaurants
places = ["McDonalds","KFC","Taco Bell","Chilis"]

#to create our module we often need to tie a function
def pick():
    return choice(places)