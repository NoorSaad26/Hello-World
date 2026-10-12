# Noor Saad
# 09/27/2026
# End of week assignment - week 5

# Exercise 5

import string

# The first part opens the raw file and the second half creates a new file for the cleaned up data
with open("raw_reviews.txt", "r") as infile, open("clean_reviews.txt", "w") as outfile:
    # reading the raw reviews
    for reviews in infile:
        lower = reviews.lower()
        no_punct = lower.translates(str.maketrans("", "", string.punctuatuion))
        

print("Done!")