import numpy as np

def majority_3(a, b, c):
    """Basic 3-input majority logic gate"""
    return (a + b + c) >= 2

def recursive_majority(bits, level):
    """Recursive cascade for the 3D Bojan architecture"""
    if level == 0:
        return bits[0]
    
    next_level_bits = []
    # Group elements by 3 for the next level
    for i in range(0, len(bits), 3):
        maj = majority_3(bits[i], bits[i+1], bits[i+2])
        next_level_bits.append(maj)
        
    return recursive_majority(next_level_bits, level - 1)

def simulate_3d_bojan(noise_rate, num_trials=10000):
    """
    Monte Carlo simulation for the 729-element (3^6) architecture.
    Injecting noise and verifying signal survival.
    """
    elements = 3**6  # 729 elements
    levels = 6       # 6 cascade levels
    errors_escaped = 0
    
    for _ in range(num_trials):
        # 0 represents a clean signal, 1 represents an error (noise)
        noise = np.random.choice([0, 1], size=elements, p=[1-noise_rate, noise_rate])
        
        final_output = recursive_majority(noise, levels)
        
        if final_output == 1:
            errors_escaped += 1
            
    fidelity = 100.0 * (1 - (errors_escaped / num_trials))
    return fidelity

if __name__ == "__main__":
    print("=== 3D Bojan Architecture Simulation ===")
    print("Elements: 729 (3^6) | Logic: Recursive Majority Cascade\n")
    
    # Testing noise thresholds from 10% to 50%
    test_rates = [0.10, 0.20, 0.30, 0.40, 0.45, 0.50]
    
    for rate in test_rates:
        fid = simulate_3d_bojan(rate, num_trials=10000)
        print(f"Noise Rate: {rate*100:2.0f}% -> Signal Fidelity: {fid:.2f}%")
