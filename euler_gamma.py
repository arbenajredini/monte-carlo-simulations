import math

def euler_gamma(n):
    """
    Calculate the Euler-Mascheroni constant using the formula:
    γ = lim (n -> ∞) (H_n - ln(n))
    where H_n is the nth harmonic number.
    
    Parameters:
    n (int): The number of terms to use in the approximation.
    
    Returns:
    float: The approximate value of the Euler-Mascheroni constant.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    H_n = sum(1 / k for k in range(1, n + 1))
    
    ln_n = math.log(n)
    
    gamma = H_n - ln_n
    
    return gamma