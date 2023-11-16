def months():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    number = int(input("Enter month number: "))
    number_month = months[number-1]
    return number_month, number
