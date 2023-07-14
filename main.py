import random
import time
import matplotlib.pyplot as pt
import csv
import pandas as pd

runs = ["0run", "1run", "2run", "3run", "4run", "6run", "out", "1run(wide)"]
score = 0
team1score = 0
team2score = 0
team1finished = 0
next_team = 0
team = 1
wicket = 0
w = 0
team1wickets = []
team2wickets = []
listofwickets = []
listofwickets = team1wickets
dictionary_team1runsperover = {}
dictionary_team2runsperover = {}
dictionary_team1wicketsperover = {}
dictionary_team2wicketsperover = {}
team1name = input("Enter Team-1 name: ")
team2name = input("Enter Team-2 name: ")
team1runs = []
team2runs = []
listofruns = []
listofruns = team1runs
team1overs = []
team2overs = []
listofovers = []
listofovers = team1overs
teamname = team1name
while 1:
    for y in range(20):
        for x in range(6):  # 6balls
            time.sleep(0.5)
            each_ball_run = runs[random.randint(0, 7)]
            if x == 0:
                ball = "1st ball"
            elif x == 1:
                ball = "2nd ball"
            elif x == 2:
                ball = "3rd ball"
            elif x == 3:
                ball = "4th ball"
            elif x == 4:
                ball = "5th ball"
            elif x == 5:
                ball = "6th ball"
            if each_ball_run == "1run(wide)":
                while each_ball_run == "1run(wide)":
                    print(ball, ":", each_ball_run)
                    score = score + int(each_ball_run[0])
                    if team1finished == 1:
                        if team1score < score:
                            next_team = 2
                            break
                    each_ball_run = runs[random.randint(0, 7)]
                    if each_ball_run == "1run(wide)":
                        continue
                    else:
                        break
            if each_ball_run == "out":
                print(ball, ":", each_ball_run)
                wicket = wicket + 1
                w = w + 1
                if wicket >= 10:  # all wickets gone
                    next_team = 2
                    break  # quit balls (exit from this for loop)
            elif next_team == 2:
                break
            else:
                print(ball, ":", each_ball_run)
                score = score + int(each_ball_run[0])
                if team1finished == 1:
                    if team1score < score:
                        next_team = 2
                        break

        print(teamname, "details after", y + 1, ".", 0 if int(ball[0]) == 6 else int(ball[0]), "overs")
        print("score", score, "runs")
        listofruns.append(score)
        listofovers.append(y + 1)
        listofwickets.append(w)
        w = 0
        print("Wickets gone: ", wicket)
        if next_team == 2:
            wicket = 0
            next_team = 0
            break
    if team == 1:
        print(team1name, "score is: ", score)
        time.sleep(2)
        team1score = score
        score = 0
        wicket = 0
        team = team + 1
        teamname = team2name
        listofruns = team2runs
        listofovers = team2overs
        listofwickets = team2wickets
        team1finished = 1
    else:
        print(team2name, "score is: ", score)
        time.sleep(2)
        team2score = score
        break  # quit from while
print("===================")
if team1score > team2score:
    print("", 9team1name, "won the match")
elif team1score == team2score:
    print("draw the match")
else:
    print("", team2name, "won the match")
print("===================")
time.sleep(1)
# line chart
pt.plot(team1overs, team1runs, color='y', label=team1name)
pt.plot(team2overs, team2runs, color='b', label=team2name)
pt.legend()  # which line belongs to which team
pt.title(team1name + " vs " + team2name)
pt.show()

# bar chart
pt.bar(team1overs, team1runs, color='y', label=team1name)
pt.bar(team2overs, team2runs, color='b', label=team2name)
pt.legend()  # which bar belongs to which team
pt.title(team1name + " vs " + team2name)
pt.show()
# mapping list to dictionary
dictionary_team1runsperover = dict(zip(team1overs, team1runs))
dictionary_team2runsperover = dict(zip(team2overs, team2runs))
dictionary_team1wicketsperover = dict(zip(team1overs, team1wickets))
dictionary_team2wicketsperover = dict(zip(team2overs, team2wickets))
with open('/Users/agathiyann/PycharmProjects/pythonProject3/main.csv', 'w') as f:
    fieldnames = team1overs if len(team1overs) > len(team2overs) else team2overs
    mywriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',')
    mywriter.writeheader()
    mywriter.writerow(dictionary_team1runsperover)
    mywriter.writerow(dictionary_team2runsperover)
    mywriter.writerow(dictionary_team1wicketsperover)
    mywriter.writerow(dictionary_team2wicketsperover)
