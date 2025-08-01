# This program generates the multiplication table for a number provided by the user.

def ghadiya_table():
   
    print("---------Table-------")

    try:
        
        number = int(input("As your wish write a table here e number : "))
        print("-" * 35)

       
        print(f" ghdiya number : {number}:\n")
        for i in range(1, 11):
           
            result = number * i
            
            print(f"{number} * {i} = {result}")

    except ValueError: 
        print("\nError: Invalid input. Please enter a whole number.")

    finally:
        
        print("-" * 35)
       



if __name__ == "__main__":
    ghadiya_table()