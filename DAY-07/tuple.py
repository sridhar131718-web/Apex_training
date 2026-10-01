results = ("PASS", "FAIL", "PASS", "FAIL", "PASS", "PASS")

# Using tuple methods for both operations
pass_count = results.count("PASS")
first_position = results.index("PASS")

print("Number of PASS results:", pass_count)
print("First position of PASS:", first_position)
