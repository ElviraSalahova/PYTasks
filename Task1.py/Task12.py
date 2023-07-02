s = int (input("Enter Number s: "))
p = int (input("Enter Number p: "))
x = (s-int((s**2-4*p)**0.5))//2
y = (s+int((s**2-4*p)**0.5))//2
print(f'Number X is {x}, Number Y is {y}')
