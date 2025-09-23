class AdvancedHarmonicMathematics:
    def __init__(self):
        self.bells = SevenBellHarmonySystem()
        
    def calculate_bell_resonance_matrix(self):
        """Create resonance matrix showing how bells interact"""
        frequencies = self.bells.get_bell_frequencies()
        n = len(frequencies)
        resonance_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                # Calculate resonance based on interval simplicity
                ratio = frequencies[j] / frequencies[i]
                if ratio < 1:
                    ratio = 1/ratio  # Always use ratio >= 1
                
                # Resonance strength: simpler ratios = stronger resonance
                resonance_strength = 1 / (1 + abs(math.log2(ratio) - round(math.log2(ratio))))
                resonance_matrix[i][j] = resonance_strength
        
        return resonance_matrix
    
    def fibonacci_relationship_analysis(self):
        """Analyze Fibonacci relationships between bells"""
        fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        frequencies = self.bells.get_bell_frequencies()
        
        relationships = {}
        for i, freq in enumerate(frequencies, 1):
            # Find closest Fibonacci number relationship
            closest_fib = min(fib_sequence, key=lambda x: abs(x - freq/10))
            ratio = freq / (closest_fib * 10)
            
            relationships[f"bell_{i}"] = {
                "frequency": freq,
                "closest_fibonacci": closest_fib,
                "ratio_to_fib": ratio,
                "fibonacci_derivative": f"{closest_fib} × 10 ≈ {closest_fib * 10}",
                "deviation": abs(ratio - 1)
            }
        
        return relationships
    
    def golden_ratio_optimization(self):
        """Optimize frequencies using Golden Ratio constraints"""
        base_432 = 432.0
        golden_ratio = self.bells.golden_ratio
        
        # Calculate ideal frequencies based on 432Hz baseline
        ideal_frequencies = {
            "bell_1_ideal": base_432 / (golden_ratio ** 3),  # 432 / φ³
            "bell_2_ideal": base_432 / (golden_ratio ** 2),  # 432 / φ²  
            "bell_3_ideal": base_432 / golden_ratio,         # 432 / φ
            "bell_4_ideal": base_432,                        # 432 baseline
            "bell_5_ideal": base_432 * golden_ratio,         # 432 × φ
            "bell_6_ideal": base_432 * (golden_ratio ** 2),  # 432 × φ²
            "bell_7_ideal": base_432 * (golden_ratio ** 3)   # 432 × φ³
        }
        
        return ideal_frequencies
