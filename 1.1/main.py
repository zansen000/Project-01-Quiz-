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
      if g_2 == "Asia" or g_2 == "asia" :
        print("Genius!")
        next_2 = input("Next? (y/n) : ")
        if next_2 == "y" :
          print("===========")
          print("Question 03")
          print("===========")
          print("Indonesia is ... Country with over 17.000+ islands!")
          g_3 = input("Answer Here : ")
          if g_3 == "Island" or g_3 == "island":
            print("3 in a row!")
            next_3 = input("Next, genius? (y/n) : ")
            if next_3 == "y" :
              print("===========")
              print("Question 04")
              print("===========")
              print("What is company behind Visual Studio Code?")
              g_4 = input("Enter Here : ")
              if g_4 == "Microsoft" or g_4 == "microsoft" :
                print("Sheess! You're master!")
                next_4 = input("Next? (y/n) : ")
                if next_4 == "y" :
                  print("===========")
                  print("Question 05")
                  print("===========")
                  print("What is the most phone in the world?")
                  g_5 = input("Enter Here : ")
                  if g_5 == "Samsung" or g_5 == "samsung" :
                    print("Omo omo omo You genius!")
                    next_5 = input("Next? (y/n) : ")
                    if next_5 == "y" :
                      print("===========")
                      print("Question 06")
                      print("===========")
                      print("How many country at Europe?")
                      g_6 = input("Enter Here : ")
                      if g_6 == "45" :
                        print("That's correct mate! Good Job!")
                        next_6 = input("Next? (y/n) : ")
                        if next_6 == "y" :
                          print("===========")
                          print("Question 07")
                          print("===========")
                          print("What country is the most people lived in?")
                          g_7 = input("Enter Here : ")
                          if g_7 == "India" or g_7 == "india" :
                            print("You are corred!")
                            next_7 = input("Next? (y/n) : ")
                            if next_7 == "y" :
                              print("===========")
                              print("Question 08")
                              print("You very close to finish! Keep Spirit!")
                              print("===========")
                              print("What is number one food in the world?")
                              g_8 = input("Enter Here : ")
                              if g_8 == "Pizza" or g_8 == "pizza" :
                                print("Mama Mia you are correta!")
                                next_8 = input("Next? (y/n) : ")
                                if next_8 == "y" :
                                  print("===========")
                                  print("Question 09")
                                  print("===========")
                                  print("what is the 18th letter in this word?")
                                  ready_1 = input("ready? (y/n) : ") 
                                  if ready_1 == "y" or "n" :
                                    print("if you choose n, I sorry! :)")
                                    print("Here you go!")
                                    print("Pneumonoultramicroscopicsilicovolcanoconiosis")
                                    g_9 = input("Enter Here : ")
                                    if g_9 == "o" or g_9 == "O":
                                      print("Youarecorrectyey!")
                                      next_9 = input("Just one step! are you ready? (y/n) : ")
                                      if next_9 == "y" :
                                        print("And this is : ")
                                        print("===============")
                                        print("Question 10")
                                        print("===============")
                                        print("What is the definition of word above?")
                                        g_10 = input("Enter Here : ")
                                        if g_10 == "A lung disease caused by the inhalation of silica or quartz dust" or g_10 == "a lung disease caused by the inhalation of silica or quartz dust" :
                                          print("Don't press 'n' in there!")
                                          sure_1 = input("Are you sure ? (y)")
                                          if sure_1 == "y" :
                                            print("And your answer : ", g_10 , "is!")
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print("RIGHT!!!")
                                            print("Congrast you just finish General Question!")
                                            
                                        else : 
                                          print("And you answer : ", g_10 , "is!")
                                          print("Wronggg")
                                          
                                      else : 
                                        print("Well see you again!")
                                        quit
                                        
                                    else : 
                                      print("YOU ARE WRONG!")
                                      quit
                                      
                                else :
                                  print("Well, ciao!")
                                  quit
                                  
                              else :
                                "AMAREGGIATO!!!!"
                                quit
                                
                            else : 
                              print("well, see you again mate!")
                              quit
                              
                          else : 
                            print("It's very very wrong!")
                            quit
                            
                        else : 
                          print("Well see you again mate!")
                          quit
                          
                      else : 
                        print("You wrong mate!")
                        quit
                        
                    else :
                      print("Well Have an nice day! Anyeong!")
                      quit
                      
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
#end here : General Question
