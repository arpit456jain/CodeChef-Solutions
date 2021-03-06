
MAX_SIZE = 1000001

# isPrime[] : isPrime[i] is true if
#             number is prime
# prime[] : stores all prime number
#           less than N
# SPF[] that store smallest prime
# factor of number [for ex : smallest
# prime factor of '8' and '16'
# is '2' so we put SPF[8] = 2 ,
# SPF[16] = 2 ]
isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * (MAX_SIZE)


# function generate all prime number
# less then N in O(n)
def manipulated_seive(N):
    # 0 and 1 are not prime
    isprime[0] = isprime[1] = False

    # Fill rest of the entries
    for i in range(2, N):

        # If isPrime[i] == True then i is
        # prime number
        if isprime[i] == True:
            # put i into prime[] vector
            prime.append(i)

            # A prime number is its own smallest
            # prime factor
            SPF[i] = i

            # Remove all multiples of i*prime[j]
        # which are not prime by making is
        # Prime[i * prime[j]] = false and put
        # smallest prime factor of i*Prime[j]
        # as prime[j] [ for exp :let i = 5 , j = 0 ,
        # prime[j] = 2 [ i*prime[j] = 10 ]
        # so smallest prime factor of '10' is '2'
        # that is prime[j] ] this loop run only one
        # time for number which are not prime
        j = 0
        while (j < len(prime) and
               i * prime[j] < N and
               prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False

            # put smallest prime factor of i*prime[j]
            SPF[i * prime[j]] = prime[j]

            j += 1
manipulated_seive(MAX_SIZE-1)

def count_prime(x):
    i=0
    c=0
    while(i<len(prime)):
        if prime[i]<=x:
            c+=1
        else:
            break
        i+=1
    return c
hash_map={}
print(prime)
for i in range(0,MAX_SIZE):
    hash_map[i] = count_prime(i)
print(hash_map)
t=int(input())
for i in range(t):
    arr = [int(x) for x in input().split()]
    x=arr[0]
    y=arr[1]
    if y==1:
        if x==1 or x==2:
            print("Chef")
        else:
            print("Divyam")
    else:

        add = count_prime(x)
        # print("no of prime no",add)
        if add<=y:
            print("Chef")
        else:
            print("Divyam")
