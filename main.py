# Source from https://learnxinyminutes.com/docs/python/

# a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#pop for deleting last value
#del for deleting by index
#remove for deleting by value

# b, c, *d = a

# for i, value in enumerate(a):
#     print(i, value) # i is index and value is a[i]

# x = 0
# while x <= len(a)-1:
#     print(a[x])
#     x += 1

# exception handling
# python contains try, except, else, finally for exception handling
# else will run every time with exception occur
# finally will run every time in both try and except

# file handling
# contains method called "open"
# open(file_name, open_mode)
# just think variable is file so file.write() or file.read() will used to read or write content from file

# iterable
# filled_dict = {"one": 1, "two": 2, "three": 3}
# our_iterable = filled_dict.keys()
# our_iterator = iter(our_iterable) # this iter will work like a zip function but in very small case
# for i in our_iterator:
#     print(i)
# or we can print our_iterator like :- next(our_iterator)

# args and kwargs
# args are used to take unlimited arguments like :- x = demo(1, 2, 3)
# args will return tuple like :- (1, 2, 3)
# kwargs are used tom take unlimited keyword arguments like :- demo(big=4, small=5)
# kwargs will return dict like :- {"big": 4, "small": 5}

# we can call globle defined variavles by useing goble keyword like :- 
# x = 1
# def demo(number):
#   globle x
#   print(x+n)
# demo(1) it will print 2

# map function
# map is used to call parameteresd functions like demo(a, b)
# so we can call it like map(function_name, parameters)
# example: map(demo, 10, 20)
# example: list(map(demo, 20, 10)

# classmethod and staticmethod
# class abc():
#     name = "Shubham" # class atribute
    
#     @classmethod    # will take cls argument for using class atrubutes
#     def say(cls):   # can not take self argument
#         print(cls.name)
        
#     @staticmethod   # will not take cls or self argument
#     # this method can not use the attrubuts and isinstances of the class
#     def helo():
#         print("Say Hello")

# print("hello" " world") # this is not error but answer will :- hello world means "hello world"

