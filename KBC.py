sum = 0
quetions = [
  "Which course does this program (KBC) belongs to ?",
  "Which video on Code-with-harry yt channel is currently (25-Dec-2022) the most popular ?",
  "In which year was the first video on Code-with-harry channel uploaded ?"
]
correct_answers = [
  "Ultimate Python course", "Python course for begginers", 2018
]
not_so_correct_answers = [
  "Ultimate C programming course", "C programming course for begginers", 2017,
  "Ultimate Java programming course", "HTML course for begginers", 2019,
  "Ultimate HTML course", "Java programming course for begginers", 2020
]
print("Enter Contestent Info\n")
player_name = input("Enter Name of the Contestent : \n")
player_gender = input("Please choose your Gender (Male/Female) : \n")
if (player_gender == "Male"):
  print(f"Welcome Mr.{player_name.upper()} to Kaun Banega Crorepati\n")
elif (player_gender == "Female"):
  print(f"Welcome Ms.{player_name.upper()} to Kaun Banega Crorepati\n")
else:
  print(f"Welcome {player_name.upper()} to Kaun Banega Crorepati\n")
for i in range(0,3):
  print("kya aap tayar hay", i+1 , "sawal ka javab dene k liye : \n")
  res = input("Yes/No : ")
  if (res == "yes"):
    print("chaliye saru karte hay\n")
    print("Quetion", i+1, "/n", quetions[i], "\n")
    print("javab dene k liye niche diye gai inn 4 options me se ek chuniye\n")
    print("A.", correct_answers[i], "\t\t\t\tB.", not_so_correct_answers[i],
          "\nC.", not_so_correct_answers[i + 3], "\t\t\tD.",
          not_so_correct_answers[i + 6], "\n")
    contestent_choice = input("A/B/C/D")
    if (contestent_choice == "A"):
      print("aap ka javab sahi hay\n")
      sum = sum + 1000
      print("aap ne ", sum, "ruppe jeete hay\n")
    else:
      print("aap k javab galat hay\n")
  else:
    print("Hume bahot dukh he ki aap agge nahi khelna chahate\n")
print("hamare sath khelne k liye abhar, apne kul ", sum, "rakam jitte hay")
