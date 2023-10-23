#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1. You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two List one 
# which have all the Even Numbers and another List which will have all the ODD numbers in it?

list = [10, 501, 22, 37, 100, 999, 87, 351]

# List containing even numbers
even_numbers = [num for num in list if num % 2 == 0]

# List containing odd numbers
odd_numbers = [num for num in list if num % 2 != 0]

print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)


# In[44]:


# 2. Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count all the Prime Numbers and 
# create a new Python List which will contain all the Prime Numbers in it?

list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Count of prime numbers
count_of_primes = len(prime_numbers)

# List containing prime numbers
prime_numbers = [num for num in list if is_prime(num)]

print("Count of Prime Numbers:", count_of_primes)
print("Prime Numbers List:", prime_numbers)


# In[22]:


# 3. Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] Find out how many numbers are there 
# in the given Python List which are Happy Numbers?

""" Input: n = 10
Output: True
10 is Happy Number,
1^2 + 0^2 = 1
As we reached to 1, 10 is a Happy Number.

n = 100
Output: True
100 is Happy Number,
1^2 + 0^2 + 0^2 = 1
As we reached to 1, 100 is a Happy Number.

Input: n = 501, 22, 37, 999, 87, 351
Output: False """
    
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

list = [10, 501, 22, 37, 100, 999, 87, 351]

# Count of happy numbers
happy_count = 0

# Iterating through the given list to count happy numbers
for num in given_list:
    if is_happy_number(num):
        happy_count += 1

print("Count of Happy Numbers:", happy_count)


# In[31]:


# 4. Write a python program to find the sum of the first and last digit of an integer?

def sum_first_and_last_digit(n):
    # Convert the integer to a string
    num_str = str(n)

    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    # Calculate the sum of the first and last digits
    result = first_digit + last_digit

    return result

integer = 12345
result = sum_first_and_last_digit(integer)
print(f"The sum of the first and last digit of {integer} is: {result}")


# In[32]:


# 5. You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable 
# number of Mangoes. There are M students in a Guvi class, your task is to distribute the Mangoes in such a way that 
# each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with 
# minimum Mangoes given to the student is minimum?

def distribute_mangoes(bags, students):
    bags.sort()  # Sort the bags in ascending order
    n = len(bags)
    result = []

    for i in range(students):
        result.append(bags[i % n])  # Assign bags in a round-robin fashion

    max_mangoes = max(result)
    min_mangoes = min(result)
    difference = max_mangoes - min_mangoes

    return result, difference

N = [15, 10, 8, 19, 11, 13]
M = 4
distribution, min_difference = distribute_mangoes(N, M)
print(f"The distribution of bags: {distribution}")
print(f"The minimum difference in mangoes: {min_difference}")


# In[45]:


# 6. You have been given three lists. Your task is to find the duplicates in the three lists. Write a python program 
# for the same. You can use your own python lists?

# Define three example lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
list3 = [8, 9, 10, 11, 12, 13, 14, 15, 16]

# Find duplicates in the three lists
duplicates = []
for num in list1:
    if num in list2 and num in list3:
        duplicates.append(num)

# Print the duplicates
print("Duplicates in the three lists:", duplicates)


# In[36]:


# 7. Write a python program to find the first non-repeating elements in a given list of integers?

def first_non_repeating(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in nums:
        if freq[num] == 1:
            return num

    return None  # If no non-repeating element is found

my_list = [2, 3, 4, 2, 5, 4, 6, 7, 3]
result = first_non_repeating(my_list)
print(f"The first non-repeating element is: {result}")


# In[37]:


# 8. Write a python program to find the minimum element in a rated and sorted list?

def find_minimum_element(sorted_list):
    if sorted_list:
        return sorted_list[0]
    else:
        return None  # Return None for an empty list

my_sorted_list = [1, 2, 3, 4, 5]
minimum_element = find_minimum_element(my_sorted_list)
print(f"The minimum element in the list is: {minimum_element}")


# In[42]:


# 9. You have been given a Python list [10, 20, 30, 9] and a value of 59. Write a python program to find the triplet
# in the list whose sum is equal to the given value?

def find_triplet(nums, target):
    n = len(nums)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

my_list = [10, 20, 30, 9]
target_value = 59
result = find_triplet(my_list, target_value)
if result:
    print(f"The triplet with sum {target_value} is: {result}")
else:
    print("No such triplet found.")


# In[43]:


# 10. Given a list [4, 2, -3, 1, 6] Wite a python program to find if there is a sub-list with sum equal to Zero?

def sub_list_with_zero_sum(nums):
    prefix_sum = 0
    prefix_sums_set = set()

    for num in nums:
        prefix_sum += num
        if prefix_sum in prefix_sums_set or prefix_sum == 0:
            return True
        prefix_sums_set.add(prefix_sum)

    return False

my_list = [4, 2, -3, 1, 6]
if sub_list_with_zero_sum(my_list):
    print("Sub-list with zero sum exists.")
else:
    print("No sub-list with zero sum.")

