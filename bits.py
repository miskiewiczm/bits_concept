#!/usr/local/bin/python3
# scheme:
# S_1 - s_1 - B_1 - s_2 - ... - s_n - B_n - s_{n+1} - E_1
# example (4 bits):
# S_1 - s_1 - B_1 - s_2 - B_2 - s_3 - B_3 - s_4 - B_4 - s_5 - E_1


import random

data = "01100101001010101101010101010101010"
primers = []

primers_base = open("primers_small_set.txt", "r")

for line in primers_base:
    primers.append(line[:-1])
primers_base.close()

substrand_size = 8
number_of_bits = len(data)
number_of_primers = len(primers)
number_of_substrands = (number_of_bits // substrand_size) + 1*(number_of_bits % substrand_size != 0)
number_of_start = number_of_substrands
number_of_ends = number_of_substrands - 1
number_of_binds = number_of_bits
number_of_binds_per_strand = substrand_size + 1
number_of_missing_bits = substrand_size - number_of_binds % substrand_size

print("Bits:", number_of_bits)
print("Sub len:", substrand_size)
print("Number of sub:", number_of_substrands)
print(number_of_missing_bits)

# how many primers we need
max_primers = number_of_start + number_of_ends + number_of_substrands * number_of_binds_per_strand + 2 + 1


start_nr = random.randint(0,number_of_primers - max_primers)

S_primers = []
for _ in range(number_of_substrands):
    S_primers.append(primers[start_nr])
    start_nr += 1

E_primers = []
for _ in range(number_of_substrands):
    E_primers.append(primers[start_nr])
    start_nr += 1

B_primers = [
    primers[start_nr],
    primers[start_nr + 1]
]

start_nr += 2

bind_primers = []
for _ in range(number_of_bits+1):
    bind_primers.append(primers[start_nr])
    start_nr += 1

pos = 0
substrand = []
temp_strtand = []

for i in range(number_of_substrands-1):
    temp_strand = [S_primers[i]] + [bind_primers[pos]]
    for _ in range(substrand_size):
        temp_strand += [B_primers[int(data[pos])]] + [bind_primers[pos+1]]
        pos += 1
    temp_strand += [E_primers[i]]
    substrand.append(temp_strand)
temp_strand = [S_primers[number_of_substrands-1]] + [bind_primers[pos]]

# Last strand composition
for _ in range(len(data)-pos):
    temp_strand += [B_primers[int(data[pos])]] + [bind_primers[pos+1]]
    pos += 1
temp_strand += [E_primers[number_of_substrands-1]]
substrand.append(temp_strand)

# Last strand filling with random data
#...

for i in substrand:
    print("Sub:",i)