# Create a List ---

fruits = ["apple", "banana", "cherry", "date"]

print(f"Our starting list of fruits: {fruits}")
print("--------------------------------------------------------")




for fruit in fruits:

  print(f"- {fruit.capitalize()}")
print("-----------------------------------------------------")


# Functions and Methods
print("--- List Functions & Methods ---")

#  len() 
print(f"1 Length of the list: {len(fruits)}")

#  append() 
print("\n2) Appending 'elderberry'...")
fruits.append("elderberry")
print(f"   List is now: {fruits}")

#  insert() 
print("\n3) Inserting 'apricot' at index 1...")
fruits.insert(1, "apricot")
print(f"   List is now: {fruits}")

#  remove()
print("\n4) Removing 'cherry'...")
fruits.remove("cherry")
print(f"   List is now: {fruits}")

#  pop()

print("\n5) Popping the item at index 2...")
removed_fruit = fruits.pop(2)
print(f"   Removed fruit was: '{removed_fruit}'")
print(f"   List is now: {fruits}")

# sort()
print("\n6) Sorting the list...")
fruits.sort()
print(f"   List is now: {fruits}")

