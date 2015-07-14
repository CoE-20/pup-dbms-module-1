import sys, operator

"""f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close() """

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[0] in suc:
      suc[row[0]] += 1
    else:
      suc[row[0]] = 1
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print line
  print "1. The region with the most SUC is " + suc_list[0][0]


#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  f = open('suc_ph.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[0] != 'region' and row[2].strip() != '-':
       if row[2].isdigit(): 
        if row[0] in suc:
          suc[row[0]] += int(row[2])
        else:
          suc[row[0]] = int(row[2])
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print "2. The region with the most SUC is " + suc_list[0][0]

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  
  f = open('suc_ph.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[0] != 'region' and row[6].strip() != '-':
      if row[0] in suc:
        suc[row[0]] += int(row[6])
      else:
        suc[row[0]] = int(row[6])
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)

  print "3. The region with the most SUC graduates is " + suc_list[0][0]


#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[1] != 'suc' and row[2].strip() != '-' and row[2].strip() != 'free tuition fee' and row[2].strip() != 'nds' and row[2].strip() != '80 / 120' and row[2].strip() != '550/sem' and row[2].strip() != 'nd' and row[2].strip() != '2500 regardless of the number of units' and row[2].strip() != '142.5' and row[2].strip() != '158.8' and row[2].strip() != 'Business' :
      if row[1] in suc:
        suc[row[1]] += int(row[2])
      else:
        suc[row[1]] = int(row[2])
  f.close()
  suc_list = sorted(suc.items(), key = lambda cheap:cheap[-1])
  print "4. Top 3 cheapest SUC for BS level in school year 2010-2011"
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[1] != 'suc' and row[2].strip() != '-' and row[2].strip() != 'free tuition fee' and row[2].strip() != 'nds' and row[2].strip() != '80 / 120' and row[2].strip() != '550/sem' and row[2].strip() != 'nd' and row[2].strip() != '2500 regardless of the number of units' and row[2].strip() != '142.5' and row[2].strip() != '158.8' and row[2].strip() != 'Business' :
      if row[1] in suc:
        suc[row[1]] += int(row[2])
      else:
        suc[row[1]] = int(row[2])
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  
  print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  suc = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[2] < row[5] or row[5] < row[8]:
      if row[2].isdigit() and row[5].isdigit() and row[8].isdigit():
        if row[1] in suc:
          pass
        else:
          suc[row[1]] = 1
    if row[3] < row[6] or row[6] < row[9]:
      if row[3].isdigit() and row[6].isdigit() and row[9].isdigit():
        if row[1] in suc:
          pass
        else:
          suc[row[1]] = 1
    if row[4] < row[7] or row[7] < row[10]:
      if row[4].isdigit() and row[7].isdigit() and row[10].isdigit():
        if row[1] in suc:
          pass
        else:
          suc[row[1]] = 1
  f.close()
  suc_list = ", ".join(suc)
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print "\" "+ suc_list + " \""

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  print "7. The discipline which has the highest passing rate is " 

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"




def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()