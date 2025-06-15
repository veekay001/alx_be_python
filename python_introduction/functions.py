def greet(name):
    print(f"hello, {name} ")
    
greet("kiki")

def calculate_area(legnth, width):
    area = legnth * width
    return area

print(calculate_area(4,5))

def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is and even number")
    else:
        print(f"{number} is an odd number") 

even_or_odd(5)

for num in range(10):
  if num > 0:
    print (f"current number:{num} previous number :{num-1}, sum : {num + num-1}")
  else:
      print (f"current number:{num} previous number :{num}, sum : {num + num}")