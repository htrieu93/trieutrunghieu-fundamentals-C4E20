bacteria = int(input('How many B bacterias are there? '))
time = int(input('How much time in minutes will we wait? '))

total_bacteria = bacteria * (2 ** (time // 2))

print('After {} minutes, we would have {} bacterias'.format(time, total_bacteria))
