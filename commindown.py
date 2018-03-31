import random
"""
program that takes a list of numbers (random) and
makes a new list of only the first and last elements of the given list.
"""
def demo_print(text,a):
    print( '{0}={1}'.format(text, a))
    
def start_new_list():
    a=[number_list_rand[0]]
    b=[number_list_rand[-1]]
    c=list((a+b))
    return c 

text1="The first list "
text2="The second list have a first index and end index "
number_list_rand=random.sample(range(30),10)
demo_print(text1,number_list_rand)
creat_new=start_new_list()
demo_print(text2, creat_new)




