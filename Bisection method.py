import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=50):
    """Bisection method for finding roots"""
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        print(f"Iter {i+1}: x = {c:.6f}, f(x) = {fc:.6e}")
        
        if abs(fc) < tol or abs(b - a) < tol:
            print(f"\nRoot found: {c:.8f}")
            return c
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    print("Max iterations reached")
    return c

# Example 1: x² - 4 = 0
print("Example 1: f(x) = x² - 4")
root = bisection(lambda x: x**2 - 4, 0, 3)

print("\n" + "="*40)

# Example 2: x³ - x - 2 = 0
print("Example 2: f(x) = x³ - x - 2")
root = bisection(lambda x: x**3 - x - 2, 1, 2)

print("\n" + "="*40)

# Example 3: cos(x) - x = 0
print("Example 3: f(x) = cos(x) - x")
root = bisection(lambda x: np.cos(x) - x, 0, 1)
