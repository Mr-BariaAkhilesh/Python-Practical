def display_name(name):
 
  if name:
    
    print(f"Hello, {name}!")
  else:
   
    print("No name was provided.")


my_name = "MR:BARIA A.K"
print("Calling function with a name:")
display_name(my_name)

print("\n" + "---------------------------------------------------"* + "\n") # Separator for clarity


print("Calling function with an empty name:")
display_name("")