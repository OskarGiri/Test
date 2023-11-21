name=input('Enter your name:')
print('\n\nWelcome',name,)
print('\n\nQuzi Start Now')
score=0
a1='A.From which direction sune rise?\n\t1.East\n\t2.West\n\t3.North\n\t4.South'
print(a1)
s1=input('Enter your answer:')
w1='1'
a2='B.which country have largest population?\n\t1.India\n\t2.China\n\t3.USA\n\t4.Russia'
print(a2)
s2=input('Enter your answer:')
w2='1'
a3='C.Who is main character in one piece?\n\t1.Oskar\n\t2.Luffy\n\t3.Zoro\n\t3.Sanks'
print(a3)
s3=input('Enter your answer:')
w3='2'
a4='D.Which is the largest animal in the world?\n\t1.Elephent\n\t2.Shark\n\t3.Blue Whale\n\t4.Mouse'
print(a4)
s4=input('Enter your answer:')
w4='3'
a5='E.What is the chemical name of water?\n\t1.H2O\n\t2.O2\n\t3.CO3\n\t4.CKL'
print(a5)
s5=input('Enter your answer:')
w5='1'
if(s1==w1):
  score=score+1 
if(s2==w2):
 score=score+1
if(s3==w3):
  score=score+1 
if(s4==w4):
   score=score+1
if(s5==w5):
  score=score+1
  print("your score is",score,'/5')
  print("\n\n\nQuiz is Ended!!!")