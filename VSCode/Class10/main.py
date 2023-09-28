import my_print3
import matplotlib.pyplot as plt

for i in range(5):
    print(f'Trial {i+1}:')
    my_print3.my_print3(1, 2, i)

plt.plot([x**2 for x in range(200)])
plt.show()

