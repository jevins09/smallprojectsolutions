digit= []
card = input("Enter a credit card number: ")

def even():
    #for loop to multiply and return twice the value of the digits of even places
    for i in range(0,(len(card)),2):
        if ((int(card[i])*2)>9):
            digit.append(((int(card[i])*2)//10)+((int(card[i])*2)%10))
        else:
            digit.append(int(card[i])*2)
    #for loop to return the digits of odd places
    for i in range(1,(len(card)),2):
        digit.append(int(card[i]))
    #if statement to check the validity of a card
    if(((sum(digit))%10)==0):
        print("The given crdit card is valid!!")
    else:
        print("The given credit card is not valid!!")

def odd():
    #for loop to multiply and return twice the value of the digits of even places
    for i in range(1,(len(card)),2):
        if ((int(card[i])*2)>9):
            digit.append(((int(card[i])*2)//10)+((int(card[i])*2)%10))
        else:
            digit.append(int(card[i])*2)
    #for loop to return the digits of odd places
    for i in range(0,(len(card)),2):
        digit.append(int(card[i]))
    #if statement to check the validity of a card
    if(((sum(digit))%10)==0):
        print("The given crdit card is valid!!")
    else:
        print("The given credit card is not valid!!")

if (len(card)%2==0):
    even()
else:
    odd()
