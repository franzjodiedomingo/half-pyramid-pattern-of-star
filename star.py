# Count down from 6 rows
# Print stars for each row
# Move to the next line

for rows in range(6, 0, -1):
    for stars in range(rows - 1):
        print("*", end=" ")
    print()   