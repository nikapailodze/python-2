def square_numbers(nums):
    for i in nums:
        yield (i*i) #||
    
a=square_numbers([5,1,2,4])
print(a)
for i in a:
    print(i)