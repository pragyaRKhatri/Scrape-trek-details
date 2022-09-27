# Solving problems in statistics

import math
from utils import probability
from utils.testing import test_equal, test_close
import utils.counting as C

print("\nSOME PROBABILITY PROBLEMS\n")

# Question 1
print("Q: Find the probability of getting a head when you toss a fair coin?")
p_head = probability(1, 2)
print(p_head)
print("A: The probability is {}".format(p_head) )
expected_p_head = 0.5
test_equal(p_head, expected_p_head)
print("")

# Question 2
print("Q: Find the probability of getting 3 heads when you toss 10 fair coins.")
p_3_heads = C.combinations(10, 2) / 2**10
print("A: The probability is {}".format(p_3_heads))
expected_p_3_heads = 0.1171875
test_close(p_3_heads, expected_p_3_heads)
print("")