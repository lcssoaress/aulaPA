n1=int(input('f1:'))
n2=int(input('f2:'))

if n1==n2:
    print('iguais')
    
if n1<n2:
    n1=n1*10
if n2<n1:
    n2=n2*10
    
if n1>n2:
    n1=n1/2
if n2>n1:
    n2=n2/2
    
    
n3=n1+n2


if n3%2 == 0:
    print('par')
       

else:
    print('impar')



    
