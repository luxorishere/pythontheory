while True:
    print("Press Q or q to exit")
    a = input("Enter the number")
    if a == "q" or a == "Q":
        break
    else:
        
        
        try:
            a = int(a)
            print(f"{a} is the number you enter")
        
        except Exception as e:
            print(f"Invalid {e}")
print("Thanks for Playing the game")
