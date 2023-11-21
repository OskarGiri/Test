name=input("Enter your name:")
print('Wlecome',name,'!!!')
print("\n\nStart the quize")  
score=0
Q1='1.Which is the largest country ?\n\ta.India\n\tb.Russia\n\tc.China'
print(Q1)
vi1=input("Enter your answer(a/b/c):")
k1='b'
Q2='2.What is the chemaical name of potassium?\n\ta.O\n\tb.K\n\tc.H'
print(Q2)
vi2=input("Enter your answer(a/b/c):")
k2='b'
Q3='3.Who is the most loyal character in one piece on luffy crew?\n\ta.Zoro\a\tb.sanji\n\tc.Both'
print(Q3)
vi3=input("Enter your answer(a/b/c):")
k3='c'
print('\n\n Quzi is Ended')
if(vi1==k1):
  score=score+1
if(vi2==k2): 
   score=score+1
if(vi3==k3):
   score=score+1
print('your score is',score,'/3')
