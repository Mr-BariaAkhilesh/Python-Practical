

def count_case_in_string(input_str):
   
    uppercase_count = 0
    lowercase_count = 0

    for char in input_str:
       
        if char.isupper():
            uppercase_count += 1
      
        elif char.islower():
            lowercase_count += 1
        

    
    print("\n=== I See The code ===")
    print(f"Original String: '{input_str}'")
    print(f"Number of uppercase letters: {uppercase_count}")
    print(f"Number of lowercase letters: {lowercase_count}")
    print("-------------------------")



if __name__ == "__main__":
    
    user_input = input("Enter a string with mixed case letters: ")
    
    
    count_case_in_string(user_input)
