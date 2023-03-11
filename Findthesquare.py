lst = list(map(int, input("Enter a list of numbers separated by space: ").split()))
squared_lst = list(map(lambda x: x**2, lst))
print(squared_lst)
