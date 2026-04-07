SVM-> Support Vector machine

best possible line to seperate diffrent groups of data

is a supervised learning algorithm , used for clasification (sorting the data into categories)
reression

the main concept (idea):-
svm tries to find the best boundary (hyperplane)
that seperates data into diffrent clases

ex:-
students are classified as pass(1 or fail (0))
based on study hours
attendance

===============================================================
kernel svm tries 
datsets
student math internal resuly
s1        20   20     +1
s2        25   10     +1
s3        15   25     +1
s4        30   30     -1
s5        35   25     -1
s6        25   35     -1
------------------------------------------------
apply kernel trick
z=x1^2 +x2^2\transform the dataset
student math internal resuly z=x1^2 +x2^2
s1        20   20     +1         800
s2        25   10     +1         850
s3        15   25     +1         850
s4        30   30     -1         1800
s5        35   25     -1         1850
s6        25   35     -1         1850

now it is linear
pass-> 800---850
fail --> 1800---1850

desicion boundary
lets take the mid point 
z=1300

final svm equation:-
f(x)=x1^2 + x2^2 - 1300

predicton=
new student 
maths = 22
internal = 18

final desiscion f(x)<0 ---> pass(+1)
f(x)=-492-->pass(+1)

choose k=3
intialize centroids (trandomly
c1 = (2,3)
c2 = (10,11)
c3 = (25,30)
assign the euclidian du=istance 
d=sqrt((X2-X1)^2+(Y@-Y1)^2)
c1=0
c2=11.31
c3=36.06