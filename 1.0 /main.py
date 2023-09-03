#title of quiz
print("==========================")
print("Welcome to NaoQuiz Project")
print("==========================")
print()

#dashboard
print("Let's start")
print("1. General Question")
print("2. Numeric Question")
print("3. Computer Question")
print("4. Language Code Question")
print("=====================")
print("which one?")
print("=====================")

A = input("enter here : ")

#general question
if A == "1" :
  print("There are 10 question, Answer Correctly!")
  print("=============")
  print("Question 01")
  print("=============")
  print("How many letters are there in the English alphabet?")
  g_1 = input("Enter Here : ")
  if g_1 == "26" :
    print("You are correct!")
    next_1 = input("Next? (y/n) : ")
    if next_1 == "y" :
      print("=============")
      print("Question 02")
      print("=============")
      print("What the biggest continent?")
      g_2 = input("Enter Here : ")
      if g_2 == "Asia" :
        print("Genius!")
        next_2 = input("Next? (y/n) : ")
        if next_2 == "y" :
          print("===========")
          print("Question 03")
          print("===========")
          print("Indonesia is ... Country with over 17.000+ islands!")
          g_3 = input("Answer Here : ")
          if g_3 == "Island" :
            print("3 in a row!")
            next_3 = ("Next, genius? (y/n)")
            if next_3 == "y" :
              print("===========")
              print("Question 04")
              print("===========")
              print("What is company behind Visual Studio Code?")
              g_4 = input("Enter Here : ")
              if g_4 == "Microsoft" :
                print("Sheess! You're master!")
                next_4 = input("Next? (y/n)")
                if next_4 == "y" :
                  print("==========")
                  print("Question 5")
                  print("==========")
                  print("What is the most phone in the world?")
                  g_5 = input("Enter Here : ")
                  if g_5 == "Samsung" :
                    print("Omo omo omo You genius!")
                    next_5 = input("Next? (y/n)")
                    if next_5 == "y" :
                      print()
                      
                  else :
                    print("Haiya, Why you hate asian? Ofc you wrong!")
                    quit
                    
                else :
                  print("No? ahh well see you again! Bill Gates proud of you!")
                  quit
                  
              else : 
                print("Bill Gates will mad at you!")
                quit
                
            else :
              print("Alright genius! See you soon!")
              quit
              
          else :
            print("Pfft! you wrong")
            quit
             
        else :
          print("Well, See you again!")
          quit
          
      else :
        print("ah.. You wrong!")
        quit
        
    else :
      print("Well, See you again!")
      quit
      
  else :
    print("You wrong!")
    quit
