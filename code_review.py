def average(numbers):
    #Error Handling: Check if numbers is a list
    if not isinstance(numbers, list):
        return "numbers given is not a list to compute. Input a number list."

    total = 0
    for n in numbers:
        #Error Handling: Check if n is not an int or float
        if not isinstance(n,int) and not isinstance(n, float):
            return "List includes a non integer or float."
        else: 
            total += n
    return total / len(numbers)

#Test
print(average([65, 34, 21, 67, 89]))
print(average("Biruk Strikes Again"))
print(average(['Biruk','Bianca','Angel','Marcus']))