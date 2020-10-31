num = input("Enter a numeric value ")
    
def numeric(num):
    if num.isdigit():
        return int(num)
    else: 
        print("You entered a non numeric value")

def findSum(num):
    num = numeric(num)
    total = 0
    if isinstance(num,int):
        print("Sum of the numbers in the range of 1 to", num),
    #actual passed arguments begin from 1 and not 0
        for i in range(1,num+1):
        #total.append(i)
            total += int(i)
    return total


print(findSum(num))


