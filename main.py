def add_dog(n,dog):
  pi = 1
  
  if n > 1000: 
      pi = 4 / 1 + dog
      return pi
  else:
    dog += dog / (2 + n^2)
    n += 2
    add_dog(n,a)
    
def main():
  n = 3
  dog = 1/(2+3^2)
  result = add_dog(n,dog)
  print(result)

if __name__=="__main__":
  main()
  
  