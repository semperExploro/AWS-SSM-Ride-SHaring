# Python3 code to demonstrate working of
# Horizontal Concatenation of Multiline Strings
# Using zip() + split() + join() + list comprehension
  
# initializing strings
test_str1 = '''
geeks 4
geeks'''
  
test_str2 = '''
is
best'''
  
# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))
  
# split lines
splt_lines = zip(test_str1.split('\n'), test_str2.split('\n'))
  
# horizontal join
res = '\n'.join([x + y for x, y in splt_lines])
  
# printing result
print("After String Horizontal Concatenation : " + str(res))