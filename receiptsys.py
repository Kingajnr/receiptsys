# create a product and price for three items
p1_name, p1_price = 'Books', 49.95
p2_name, p2_price = 'Computer', 579.99
p3_name, p3_price = 'Monitor', 124.89

# create a company name and information
company_name = 'Kingspur Enterprices Ltd.'
company_address = '222, Tom Mboya St.'
company_city = 'Nairobi, Kenya'

# declare ending message
message = 'Thank you for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t\tKShs.{}'.format(p1_name.title(), p1_price))
print('\t{}\t\tKShs.{}'.format(p2_name.title(), p2_price))
print('\t{}\t\t\tKShs.{}'.format(p3_name.title(), p3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = p1_price + p2_price + p3_price
print('\t\t\tKShs.{}'.format(total))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)