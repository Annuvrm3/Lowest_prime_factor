num = int(input())
i=0


if num > 1:
 

    for i in range(2, num+1):
 

        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        
    if i==num:
      print("prime number",num)
    else:
      print("lowest prime",i)
else:
    print(num, "is not a prime number")
