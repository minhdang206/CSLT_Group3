n=input('Nhap chu cai: ')
n=n.lower()
if n in ('a','e','i','o','u'):
    print(f'{n} la nguyen am')
elif n=='y':
    print(f'y la nguyen am hoac phu am')
else:
    print(f'{n} la phu am')
