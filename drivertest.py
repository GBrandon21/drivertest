
correct_answers = ['B','D','A','A','B','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']

driver_test = open('drivertest.txt', 'r')
 
answer = []
for line in driver_test:
    print(line.rstrip())
    for possible in ["A", "B", "C", "D"]:
        if "[" + possible + "]" in line:
            answer.append(possible)
    
solution = 0
for i in range(len(correct_answers)):
    if answer[i] == correct_answers[i]:
        solution += 1

if solution >= 15:
    print('Passed')
          
else:
    print('Failed')



print('you got',solution,'correct')
print('and',20-solution,'wrong')
print('Thank You')

    
