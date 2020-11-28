import csv

f = open("questions.txt", 'r').readlines()

with open("newquestions.csv", 'w') as questionfile:
    question_writer = csv.writer(questionfile)
    for line in f:
        newline = line.replace("–", ",", 1).strip()
        newline = newline.split(".",1)
        newline = newline[0]+"."
        newline = newline.split(",",1)

        if any(newline) and not(len(newline)==1):
            question_writer.writerow(newline)
