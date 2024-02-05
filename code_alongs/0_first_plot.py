import matplotlib.pyplot as plt

numbers = list(range(10))

squares = [numbers**2 for numbers in numbers]

print(numbers)
print(squares)

plt.plot(numbers,squares)
plt.show()
plt.title("x^2 for positive integers 0-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


