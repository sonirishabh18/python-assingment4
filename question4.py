def simple_interest(p, r, t):
    return (p * r * t) / 100

# Positional arguments
print(simple_interest(10000, 5, 2))

# Keyword arguments
print(simple_interest(p=10000, r=5, t=2))
