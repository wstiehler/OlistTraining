
def Area(Breadth, Length):
    area = breadth * length
    print(f'The area of the lot {breadth} x {length} is {area} meter squares')


print('Informations of the lot')
print('-=' * 20)
breadth = float(input('Report the breadth of the lot: '))
length = float(input('Report the length of the lot: '))
Area(breadth, length)

