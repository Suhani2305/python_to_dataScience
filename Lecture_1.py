
my_tuple = ("apple", "banana", "cherry")
print("Tuple:", my_tuple)


my_list = [10, 20, 30, 40, 50]
print("List before modification:", my_list)


my_list.append(60)  
print("List after adding 60:", my_list)


def calculate_squares(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)   
    return squares

squared_numbers = calculate_squares(my_list)
print("Squares of the numbers in the list:", squared_numbers)


def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

for num in my_list:
    print(check_even_or_odd(num))

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Dictionary:", my_dict)


my_dict["profession"] = "Engineer"
print("Updated Dictionary:", my_dict)

print("Name from dictionary:", my_dict["name"])


my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)


my_set.add(6)   
my_set.discard(3)   
print("Modified Set:", my_set)

