sum = 0
count = [1,2,3]
quetions = ["Which course does this program (KBC) belongs to ?","Which video on Code-with-harry yt channel is currently (25-Dec-2022) the most popular ?","In which year was the first video on Code-with-harry channel uploaded ?"]
correct_answers = ["Ultimate Python course","Python course for begginers",2018]
not_so_correct_answers = ["Ultimate C programming course","C programming course for begginers",2017,"Ultimate Java programming course","HTML course for begginers",2019,"Ultimate HTML course","Java programming course for begginers",2020]
print("Enter Contestent Info/n")
player_name = Input("Enter Name of the Contestent : /n")
player_gender = Input("Please choose your Gender (Male/Female) : /n")

if(player_gender == Male):
    print(f"Welcome Mr.{player_name.upppercase()} to Kaun Banega Crorepati/n")
elif(player_gender == Female):
    print(f"Welcome Ms.{player_name.upppercase()} to Kaun Banega Crorepati/n")
else:
     print(f"Welcome {player_name.upppercase()} to Kaun Banega Crorepati/n")

for i in count:
    res = input("kya aap tayar hay", count[i], "sawal ka javab dene k liye (yes/no) : /n")
    if(res == yes):
        print("chaliye saru karte hay/n")
        print("Quetion",count[i],"/n",quetions[i],"/n")
        print("javab dene k liye niche diye gai inn 4 options me se ek chuniye/n")
        contestent_choice = input("A.",correct_answers[i],"/t/t/t/tB.",not_so_correct_answers[i],"/nC.",not_so_correct_answers[i+3],"/t/t/tD.",not_so_correct_answers[i+6],"/n")
        if(contestent_choice == A):
            print("aap ka javab sahi hay/n")
            sum = sum + 1000
            print("aap ne ",sum,"ruppe jeete hay/n")
        else:
            print("aap k javab galat hay/n")     
    else:
        print("Hume bahot dukh he ki aap agge nahi khelna chahate/n")
print("apne kul ",sum ,"rakam jitte hay")
