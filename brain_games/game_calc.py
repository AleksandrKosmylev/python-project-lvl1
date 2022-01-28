import random
import prompt
   
       
name = prompt.string('May I have your name? ')
rules = 'Answer "yes" if the number is even, otherwise answer "no".'
num = random.randint(0, 1000000)
task = "Question: " + str(num)
if num % 2 == 0:
#yes = even, no = odd
	answer = "yes"
else:
	answer = "no"	
user_answer = input("Your answer:")
