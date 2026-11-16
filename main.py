#there are a couple of different ways you can import a module

#first way is to import it without an alias - import the whole thing
#if the file you want to import is in the same folder you just say import filename..if its not you will have to use slashes to navigate
# import pick_food

# #call the function in pick_food we use the dot notation
# myplace = pick_food.pick()
# print(myplace)

#aliasing - giving the module a different name to avoid name conflicts
# import pick_food as picking
# myplace = picking.pick()
# print(myplace)

#you can also combine aliasing with importing just a specific function
# from pick_food import pick as picking
# myplace = picking()
# print(myplace)

#final (and probably most used or preferred) is to import specific functions/methods you want to use from a module
from pick_food import pick
# #now we do not have to use dot notation
myplace = pick()
print(myplace)



