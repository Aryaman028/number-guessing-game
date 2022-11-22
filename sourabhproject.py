import random
print("<--GAME OF GUESSING A NUMBER -->")
print()
a = int(input("Enter the starting limit"))
b = int(input("Enter the ending limit"))
score = 0



while True :
    c = random.randint(a,b)
    
    print()
    
    print("<--You have three chances to guess the number-->")
    print("Generated a random number")
    print()
    
    
    for i in range(1,4):
        x = int(input("Enter your Answer -->"))
        if x > c:
            print("Have one more try, Your guess was too high")
        elif x < c:
            print("Have one more try, Your guess was too low")
        else:
            score += 1
            print("YOU WON")
            break
    else:
        print("YOU LOSE")
        
        
        
    print("Your score is -->",score)




