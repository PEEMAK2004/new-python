# This program calculates sales commissions.
# Create a variable to control the loop.
keep_going = 'y'
# Calculate a series of commissions.
while keep_going == 'y':

    # Get a salesperson's sales and commission rate.
    wholesales = float(input('Enter the item whole sale cost: ')) 
    retailprice = (2.5)

    # Calculate the commission.
    retail = wholesales * retailprice

    # Display the commission.
    print (f'The retail price is ${retail:.2f}')

   # See if the user wants to do another one.
    keep_going = input('Do you want to Keep going' + \
                        'commission (Enter y for yes): ')