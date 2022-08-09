#!/usr/local/bin/python3

import random

primers = []
strand_len = 1000
primers_base_name = "primers_small_set.txt"

# Function to genrate random DNA strand with givel length
def random_strand(n):
    return "".join(random.choice('ACTG') for _ in range(n))
    
primers_base = open(primers_base_name, "r")

# Prefare primer database (file primer_base_name conraint list of primers) 
for line in primers_base:
    primers.append(line[:-1])
primers_base.close()

# how many primers we have in our database
number_of_primers = len(primers)

# select randomly three primers from our database by its possition
str_pr_nr = random.randint(0,number_of_primers)
mid_pr_nr = random.randint(0,number_of_primers)
end_pr_nr = random.randint(0,number_of_primers)

# 
primer_1 = primers[str_pr_nr]
primer_2 = primers[mid_pr_nr]
primer_3 = primers[end_pr_nr]

# generate DNA fragments to fill the strand 
f1 = random.randrange(100,strand_len//2,50)
f2 = random.randrange(50,strand_len-f1,50)
f3 = strand_len-f1-f2-len(primer_1)-len(primer_2)-len(primer_3)

f1_comp = random_strand(f1)
f2_comp = random_strand(f2)
f3_comp = random_strand(f3)

# strand with the given length composed of primers and fill fragments
strand = primer_1 + f1_comp + primer_2 + f2_comp + primer_3 + f3_comp

print(primer_1+" - " + str(f1) + " - " + primer_2 + " - " + str(f2) + " - " + primer_3 + " - " + str(f3))
print("Verification codes:")
print("1.", f1)
print("2.", f1+f2)
print("3.", f2)