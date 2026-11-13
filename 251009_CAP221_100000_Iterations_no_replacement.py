import random
import csv
import statistics
import array
#CAP221

def numbers():
    early = 0
    late = 0
    sample = [1, 2]
    output = random.choices(sample, weights=(24, 76), k=50) # percent early, percent late
    for i in output:
        if i == 1:
            early = early + 1
        if i == 2:
            late = late + 1
    a = [early, late] # the number of DNA sequences in each category after each iteration
    rebound_early = []
    rebound_late = []
    weights = [0.24, 0.76]
    seqs = 50
    expected_seqs = []
    expected_early = []
    expected_late = []
    for i in weights:
        expected_seqs.append((round(i * seqs))) #calculate the expected number of sequences in each bin, given the probabilities
        
	# now I need to get it to pick three numbers between 1 and 58 without replacement,
	# and bin the results into "early" or "late" based on the expected_seqs calc.
    available_numbers = list(range(1, 51))  # numbers from 1 to 58 inclusive
    selected_numbers = random.sample(available_numbers, 3)  # sample without replacement
    for number in selected_numbers:
        if number >=13:
            rebound_late.append(number)
        else:
            rebound_early.append(number)
            
    number_late = len(rebound_late)
    
    return(a, expected_seqs, rebound_early, rebound_late, number_late)

print(numbers())

with open('251009_CAP221_Rebound_Probability_No_Replacement.csv', 'w') as f:
    writer = csv.writer(f)
    header = ['Proviral_Distribution', 'Expected_Early_Late_Distribution', 'Rebound_early', 'Rebound_late', 'Number_Late_Rebound']
    writer.writerow(header)
    n = 0
    while n < 100000:
        writer.writerow(numbers())
        n = n + 1 
