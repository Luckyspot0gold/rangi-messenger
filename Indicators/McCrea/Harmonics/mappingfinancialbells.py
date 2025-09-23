class MarketBellMapper:
    def __init__(self):
        self.bell_system = SevenBellHarmonySystem()
        self.indicators = {}
        
    def map_market_condition_to_bells(self, market_data):
        """
        Map real-time market conditions to specific bell activations
        """
        price = market_data['price']
        volume = market_data['volume'] 
        volatility = market_data['volatility']
        trend = market_data['trend']
        
        active_bells = []
        intensities = {}
        
        # Bell 1: Foundation - Always active as grounding
        active_bells.append(1)
        intensities[1] = 0.3  # Base level
        
        # Bell 2: Llama Return - Activates on mean reversion
        if abs(trend) < 0.1 and volatility > 0.05:  # Sideways with volatility
            active_bells.append(2)
            intensities[2] = min(1.0, volatility * 10)
        
        # Bell 3: Structural Harmony - Strong trends
        if abs(trend) > 0.2:
            active_bells.append(3)
            intensities[3] = min(1.0, abs(trend) * 2)
        
        # Bell 4: Universal Heartbeat - Baseline (always active)
        active_bells.append(4)
        intensities[4] = 0.5 + (volume / max(volume, 1)) * 0.5
        
        # Bell 5: Love Frequency - Bull markets
        if trend > 0.1:
            active_bells.append(5)
            intensities[5] = min(1.0, trend * 3)
        
        # Bell 6: Awakening - High volatility/breakouts
        if volatility > 0.08:
            active_bells.append(6) 
            intensities[6] = min(1.0, volatility * 8)
        
        # Bell 7: Crown Connection - Market extremes/trend changes
        if abs(trend) > 0.3 or volatility > 0.12:
            active_bells.append(7)
            intensities[7] = min(1.0, (abs(trend) + volatility) * 2)
        
        return {
            "active_bells": active_bells,
            "intensities": intensities,
            "composite_frequency": self.calculate_composite_frequency(active_bells, intensities)
        }
    
    def calculate_composite_frequency(self, active_bells, intensities):
        """Calculate weighted composite frequency from active bells"""
        if not active_bells:
            return self.bell_system.bells[4]["frequency"]  # Default to baseline
        
        weighted_sum = 0
        total_intensity = 0
        
        for bell in active_bells:
            freq = self.bell_system.bells[bell]["frequency"]
            intensity = intensities.get(bell, 0)
            weighted_sum += freq * intensity
            total_intensity += intensity
        
        return weighted_sum / max(total_intensity, 0.001)
