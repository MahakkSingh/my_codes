name = input("hey type your name: ")
# print("hello",name,"welcome to my game!")

print("hello "+ name +" welcome to my game!")


should_we_play=  input("do you wanna play? ").lower()
play = should_we_play == "yes" or should_we_play == "y"
# print(play)

if play:
    print("we are gonna play!")

    direction= input("do you wanna go left or right? ") .lower()
    if direction== "left":
        print('you went left and fell off the cliff, game over, try again')
    
    
    elif direction== "right":
        choice= input(
            """okay, now you see a bridge, 
            do you wanna swin under it or cross it? (swim/cross) """
         )

        if choice == "swim":
            print("you got eaten by an alligator, you die, the end")
        
        else:
            print("you found gold and you won")
             
    else:
        print("Sorry, not valid reply, You die!")

else:
    print ("we are not playing...")

 