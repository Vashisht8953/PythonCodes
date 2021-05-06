minimum = int(input("Enter the minimum  number:"))
maximum = int(input("Enter the maximum  number:"))

even_total = 0
odd_total = 0
for number in range(minimum, maximum+1):
    if(number % 2==0):
        even_total +=number
    else:
        odd_total +=number
print("The sum of even numbers from minimum {} to maximum {} ".format(number,even_total))
print("The sum of odd numbers from minimum {} to maximum {}".format(number,odd_total))

        
