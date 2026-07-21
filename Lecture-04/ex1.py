print('---------------------------------')
print('MPH\tKPH')
print('---------------------------------')
for kph in range(60, 140, 10):
    mph = kph / 1.609
    print(f'{mph:.1f}\t{kph}')

'''print('---------------------------------')
print('MPH\tKPH')
print('---------------------------------')
for kph in range(60, 140, 10):
    mph = kph / 1.609
    print(f'{kph}\t{mph:.1f}')''' 
