import csv
ACCEPTED_MSG = """
Hi City Employee {}:
On review of your title of {} the dept was {} and type was {}.

We are thrilled to let you know that your annual salary of level remains at {}.
We look forward to seeing you continue your career with the City of Chicago.
Thank you,
The City of Chicago City Council
"""

REJECTED_MSG = """
Hi Employee {}:
On review of your title of {} the dept was {}, your full/partime status was {} and type was {}.
We are sorry to advise you that the salary level of {} is too far above recommended level and will be decreased 1%.  
Thank you for your understanding.
The City Council


"""

csv_file = open('newChicagoSal.csv')
csv_reader =csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    Name, Title, Depart, ForP, Salary = row
    msg = ACCEPTED_MSG.format(Name,Title,Depart,ForP,Salary)
    print("E-mail content:")
    print(msg)

csv_file.close()
