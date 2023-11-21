name=input("Enter your name:")
print('Hello',name,'!')
print('\n\n---Start of the Quiz')
score=0
q1='1.what is the capatial city  nepal?\n\ta.Kathamandu\n\tb.Bhakatapur\n\tc.Hetauda'
print(q1)
ui1=input("Input your answer(a/b/c):")
a1='a'
q2='2.what is the traslator for c programming called?\n\ta.Iretepter\n\tb.Compiler\n\tc.Translator'
print(q2)
ui2=input("Input your answer(a/b/c):")
a2='b'
q3='3.what is the national animal of the nepal?\n\ta.Cow\n\tb.Dog\n\tc.Tiger'
print(q3)
ui3=input("Input your answer(a/b/c):")
a3='a'
print('\n\n---End of the Quiz----')
if(ui1==a1):
    score=score+1
    if(ui1==a2):
     score=score+1
    if(ui1==a3):
     score=score+1
     print('Your score is:',score,'/3')