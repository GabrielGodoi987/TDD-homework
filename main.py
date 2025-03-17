def prime_number(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1
    return 'prime' if count <= 2 else 'is not prime'



print(prime_number(17))