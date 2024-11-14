#Luhn Algorithm
a = int(input('enter a 10 digit number'))
running_total = 0
count =0
while a>0:
    digit = a %10
    a = a//10
    count = count + 1
    if count %2==1:#odd position number
      running_total = running_total + digit
      print(digit)

    else:#even position number 
        num = digit * 2 
        if num>9:
             ans = num//10 + num%10
             running_total = ans + running_total
             print('->',ans)#
        else:
            running_total = running_total + num
print(running_total)            

 
        
   