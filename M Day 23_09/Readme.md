2= goal
  age = old
  sex = m
  chest pain = typical
  chol  =  high
  
3= class count
  total = 8
  disease = 5
no disease= 3

4=class proba
p(1) =5/8  =v0.625
p(0) = 3/8 = 0.375

5= count
a- for disease (targel =1)
from rows p1mp2,p3,p5,p8

age = old
sex = m
cp = typical
chol = high

6 =apply laplace smoothibg
categories 
age - 3
sex- 2
cp

7
p=0.37*0.33*0.4*0.29
=0.052

8
final
for disease 1 result 0.052
for diseadse 0 result 0.075

9
final 
yes lot of money
otherwise final journey