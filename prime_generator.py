# listing number of primes as a function

prime_list=[]
def prime_generator(num,start):
    ''' Here's my Docstring and contribution
    to Guido Van Rossum and the PEP 8
    '''

    while True:
        if start > 1:
            for i in range(2,start):
                if start % i == 0:
                    break
            else:
                prime_list.append(start)

        if len(prime_list) == num:
            return prime_list

        else:
            start+=1
            continue

print(prime_generator(10,2))
