def wrapper():
  a = 1
  n = int(input("Please enter the # of interations: "))
  sign = 1
  term = sign * (1/a)

  return find_term(a,n,term,sign)

def find_term(a,n,term,sign):
  
  if a < n:
    a += 2
    sign *= -1
    term += (sign * (1/a))
    print(term)
    return find_term(a,n,term,sign)

  return term 

def main():
  pi = 4 * wrapper()
  print(pi)
  return
  
if __name__=="__main__":
    main()
  
  