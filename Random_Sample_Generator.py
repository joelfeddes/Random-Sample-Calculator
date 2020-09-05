#Joel Feddes
'''
First, I want the ability to find a randomized sample for studying.
Example: I want a sample of 20 people from a population of 40 people.
However, I dont want to use the same person twice.
'''

import random
import math

go_again = input("Yo! I'm a pretty cool random generator. Wanna see? (Y or N) ").upper()


while go_again == "Y":
    
    sample_count = int(input("So, you chose wisely! Well, how many random samples do you want? "))
    print("Heads up! Your count cannot exceed the unique available numbers between your range.\nFor example, you cannot have a count of 50 numbers in a range of 1-10.")
    lower_bound = int(input("I'm gonna need a range to choose these numbers from. So, what do you want your lower bound to be? "))
    upper_bound = int(input("Upper bound: "))
    
    random_sample_list = []
    
    for i in range(sample_count):
        x = random.randint(lower_bound,upper_bound) #generate the specified number of random numbers
        while x in random_sample_list:                 #I want to avoid duplicate numbers.
            x = random.randint(lower_bound,upper_bound)
        random_sample_list.append(x)            #Otherwise, add it to my sample list
    
    
    print("Here's your sample: %s" % random_sample_list)
            
    go_again = input("again? (Y or N)").upper()             
