def wrapper():
  a = 3
  n = int(input("Please enter a number: "))
  sign = 1
  dog = sign * (1/a)

  if n <= a:
    print("Please give a number greater than 3")
    return 0

  return find_dog(a,n,dog,sign)

def find_dog(a,n,dog,sign):
  
  while a < n:
    a += 2
    sign *= -1
    dog += (sign * (1/a))
    print(dog)
    return find_dog(a,n,dog,sign)

  return dog 

def main():
  pi = 4 / (1 + wrapper())
  print(pi)
  return
  
if __name__=="__main__":
    main()
  
  