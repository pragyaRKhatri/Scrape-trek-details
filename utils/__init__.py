# Some statistics utilities

def probability(matching_outcomes, total_outcomes):
    """Compute probability of an event when all outcomes are equally likely"""
    return matching_outcomes / total_outcomes

def union_probability(p_a, p_b, p_intersection):
    """Compute the probability of P(A or B) given P(A), P(B) and P(A and B)"""
    return p_a + p_b - p_intersection