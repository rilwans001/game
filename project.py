print("THIS GAME WAS CREATED BY OJO RIDWANULLAH OKIKIOLA")
play = input("Are you ready for it?: ")
if play.lower()!="yes" :
    quit()
name = input("What is your name?: ")    
print(f"Okay let's play {name}! ")
score = 0
option = input("Choose between: Education, Politics, Sport: ")
if option.lower() =="education":
    rid = input("Choose between: Mathematics, Current Affairs, General studies:  ")
    print(rid)
    if rid.lower()=="mathematics":
        print("CHOOSE THE CORRECT OPTION AND INSERT CORRECT ANSWERS WHERE THERE IS NO OPTION")
        ans=input("The equation of the line through the points (4,2) and (-8,2) is 3y=px+q, where p and q are constants. Find the value of p; (a)1 (b)2 (c)3 (d)9 :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("There are 250 boys and 150 girls in a class. If 60percentage of the boysand 40percentages of the girls play football, what percentages of the school play football?: (a)40% (b)42.2% (c)50% (d)52.5% :  ")  
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("How many minutes makes 24 hours?: (a)1400 (b)1404 (c)1440 (d)1044:   ")
        if ans.lower()=="c":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")    
        ans=input("If 2X+4=10, find X   ")
        if ans.lower()=="3" :
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")    
        ans=input("Twice a certain whole number subtracted from 3 times the square of the number leaves 133. Find the number.: ")
        if ans.lower()=="7":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")     
    elif rid.lower()=="current affairs":
        print("CHOOSE THE CORRECT OPTION AND INSERT CORRECT ANSWERS WHERE THERE IS NO OPTION")
        ans=input("Who was the first president of Nigeria?: (a)Tafawa Balewa (b)Nnamdi Azikwe (c)Obafemi Awolowo (d)Yahya Bello :  ")
        if ans.lower()=="b":
            print("Correct!")
            score += 1
        else:
            ("Incorrect!")
        ans=input("Who was the first prime minister of Nigeria?: (a)Tafawa Balewa (b)Nnamdi Azikwe (c)Obafemi Awolowo (d)Yahya Bello :  ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("who was the Nigeria's only military president?: (a)Aguiyi-ironsi (b)Muritala Muhammed (c) Ibrahim Babangida (d)Muhannadu Buhari :   ")
        if ans.lower()=="c":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("Who is the youngest president of Nigeria?: (a)Muritala Muhammed (b)Olusegun Obasanjo (c)Muhammadu Buhari (d)Yakubu Gowon :   ")    
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("The eagle in the Nigeria coat of arm stands for? :   ")
        if ans.lower()=="strength":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    elif rid.lower()== "general studies":
        print("CHOOSE THE CORRECT OPTION AND INSERT CORRECT ANSWERS WHERE THERE IS NO OPTION")
        ans=input("The tense of a sentence is manifested on___ (a)Nominal element (b)Verbal Structure (c)Adjectival element (d)Verbal element :   ")
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else :
            print("Incorrect!")    
        ans=input("Scientific writings involving relating hypothesis usually make use of___  (a)Simple present tense (b)Simple future tense (c)Present perfect tense (d)Present progressive tense :   ")
        if ans.lower()=="b":
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        ans=input("The word 'Photograph'writing or drawing with night;The coted verb in the sentence is expressed in the ___ (a)Simple present tense (b)Future tense (c)Present perfect progressive tense (d)c$d :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")         
        ans=input("A major quality of definition by synonyms is ___ (a)Brevity (b)Verbosity (c)Repetition (d)emphasis :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("When words are reported within the paragraph,there is_____")
        if ans.lower()=="repetition":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")    
    else:
        print("Invalid Option!!!")     
elif option.lower()=="politics" :
    print("CHOOSE THE CORRECT OPTION AND INSERT CORRECT ANSWERS WHERE THERE IS NO OPTION")
    ans=input("The first political party in Nigeria was___ (a)ANPP (b)NNDP (c)SDP (d)APGA :   ")
    if ans.lower()=="b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans=input("How many registered politial parties are in Nigeria? :  ")
    if ans =="18":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")  
    ans = input("The following are 2023 presidential candidate except (a)Kolawole Abisola (b)Dumebi Kachikwu (c)Hamza Almustafa (d)Mamman Dantalle :   ")
    if ans== "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans=input("Choose the incorrect option: (a)Sowore-AAC (b)Yabagi-ADP (c)Osita-AAP (d)Chukwudi-APGA :   ")
    if ans.lower()=="c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    ans=input("Which one is odd? (a)Olusegun Obasanjo (b)Ibrahim Babangida (c)Muhammadu Buhari (d)Nnamdi Azikwe :   ")
    if ans.lower()=="b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")        
elif option.lower()=="sport":
    rid = input("Choose between: Football, Athletics, Basketball:  ")
    print(rid)
    if rid.lower()== "football":
        print("CHOOSE THE CORRECT OPTION")
        ans=input("Who have the most ballon d'or award? : (a)Ronaldinho (b)Messi (c)C.Ronaldo (d)Ronaldo Nazario :   ")
        if ans.lower()=="b":
            print("Correct!")  
            score += 1  
        else:
            print("Incorrect")
        ans=input("Who has the most UEFA Team Of The Year Appearance? (a)L.Messi (b)Ramos (c)C.Ronaldo (d)Xavi :   ")
        if ans.lower()=="c":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("Who won the UEFA best coach most? (a)Mourinho (b)Ferguson (c)Anceloti (d)guardiola :   ")
        if ans.lower()=="a":
            print("Correct")
            score += 1
        else:
            print("Incorrect!")
        ans=input("The first official football game was played in which year? (a)1880 (b)1896 (c) 1887 (d)1869 :   ")
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("Which one is odd? (a)Real Madrid (b)Inter Milan (c)Arsenal (d)Benfica :   ")
        if ans.lower()=="c":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    elif rid.lower()== "athletics":
        print("CHOOSE THE CORRECT OPTION")
        ans=input("When did Usain Bolt became the Fastest runner in the world?  (a)2009 (b)2008 (c)2010 (d)2007 :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("The Record of the fastest runner is  (a)10secs (b)9.69secs (c)9secs (d)9.58secs :   ")
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        ans=input("At the which age did fauja singh broke 8 records? (a)98years (b)100years (c)101years (d)99years :   ")
        if ans.lower()=="b":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")  
        ans=input("Who ha the longest world records in athletics?  (a)Usain Bolt (b)Fauja Singh (c)Sergei Bubka (d)Jarmila Kratochvilova :   ")
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")       
        ans=input("The most popular Sport is____ (a)Football (b)Athletics (c)Basketball (d)Baseball :   ")      
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!") 
    elif rid.lower()== "basketball":
        print("CHOOSE THE CORRECT OPTION")
        ans=input("Who invented basketball? (a)James Naismith (b)Massachusetts (c)Magic Johnson (d)None :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")   
        ans=input("The first official basketball tournament was played in which year? (a)1977 (b)1940 (c)1979 (d)1937 :   ") 
        if ans.lower()=="d":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")     
        ans=input("The first official basketball game was played in which year? (a)1937 (b)1979 (c)1892 (d)1837 :   ") 
        if ans.lower()=="c":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")    
        ans=input("Where was the first basketball game held? (a)Springfield, Massachusetts (b)Evanston,Illiniois (c)I don't know (d)None :   ")
        if ans.lower()=="a":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!") 
        ans=input("Which one is the oldest? (a)Football (b)Wrestling (c)Boxing (d)Swimming :   ")
        if ans.lower()=="b":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!") 
    else:
        print("Invalid option!!!")                
else:
    print("Invalid option!!!")
point =(score/5)*100    
print(f'{name}, Your point is {point}%')    
if point >=80:
    print("Excellent Result!!!")
elif point >=50:
    print("Good Result")
elif point >=20:
    print("Fair")    
else:
    print(f"{name}, you are a dullard")    
# g=input("Did you want to play again?    ")
# if g.lower=="yes":
#     play
# else:
#     quit()                