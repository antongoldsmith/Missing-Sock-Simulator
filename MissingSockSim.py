import random
import matplotlib.pyplot as plt

# variables
number_of_pairs = 10
total_socks = number_of_pairs * 2
socks_lost = 6
number_of_simulations = 1000
four_pairs = 0
five_pairs = 0
six_pairs = 0
seven_pairs = 0

# function
for _ in range(number_of_simulations):
    missing_socks = set(random.sample(range(total_socks), socks_lost)) # generate stacks_lost unique random numbers
    possible_pairs = 0
    # loop through the pairs
    for i in range(0, total_socks, 2):
        # if both socks of a pair aren't missing, increment possible_pairs
        if i not in missing_socks and i + 1 not in missing_socks:
            possible_pairs += 1
    if possible_pairs == 4:
        four_pairs += 1
    elif possible_pairs == 5:
        five_pairs += 1
    elif possible_pairs == 6:
        six_pairs += 1
    elif possible_pairs == 7:
        seven_pairs += 1

# results
print('There were four possible pairs of socks', four_pairs,'times.')
print('There were five possible pairs of socks', five_pairs,'times.')
print('There were six possible pairs of socks', six_pairs,'times.')
print('There were seven possible pairs of socks', seven_pairs,'times.')
print(f'There were four possible pairs of socks {four_pairs / number_of_simulations:.2%} of the times.')
print(f'There were five possible pairs of socks {five_pairs / number_of_simulations:.2%} of the times.')
print(f'There were six possible pairs of socks {six_pairs / number_of_simulations:.2%} of the times.')
print(f'There were seven possible pairs of socks {seven_pairs / number_of_simulations:.2%} of the times.')

# plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
pairs = ['Four Pairs', 'Five Pairs', 'Six Pairs', 'Seven Pairs']
num_of_pairs = [four_pairs, five_pairs, six_pairs, seven_pairs]
ax.bar(pairs,num_of_pairs)
plt.show() # plots the data in a bar graph
