class McCreaHarmonicTradingSystem:
    def __init__(self):
        self.bells = SevenBellHarmonySystem()
        self.mapper = MarketBellMapper()
        self.math = AdvancedHarmonicMathematics()
        
    def real_time_market_analysis(self, market_data):
        """Complete real-time analysis using 7-bell system"""
        # Get active bells for current market condition
        bell_analysis = self.mapper.map_market_condition_to_bells(market_data)
        
        # Calculate harmonic indicators
        composite_freq = bell_analysis["composite_frequency"]
        active_bell_count = len(bell_analysis["active_bells"])
        harmonic_intensity = sum(bell_analysis["intensities"].values())
        
        # Market state classification based on bell activity
        if active_bell_count <= 2:
            market_state = "CALM"
            risk_level = "LOW"
        elif active_bell_count <= 4:
            market_state = "ACTIVE" 
            risk_level = "MEDIUM"
        else:
            market_state = "VOLATILE"
            risk_level = "HIGH"
        
        return {
            "market_state": market_state,
            "risk_level": risk_level,
            "composite_frequency": composite_freq,
            "active_bells": bell_analysis["active_bells"],
            "bell_intensities": bell_analysis["intensities"],
            "harmonic_power": harmonic_intensity,
            "trading_signal": self.generate_trading_signal(bell_analysis)
        }
    
    def generate_trading_signal(self, bell_analysis):
        """Generate buy/sell/hold signals based on bell configuration"""
        active_bells = set(bell_analysis["active_bells"])
        intensities = bell_analysis["intensities"]
        
        # Bullish signals (Bells 4, 5 active)
        if 4 in active_bells and 5 in active_bells and intensities[5] > 0.7:
            return "STRONG_BUY"
        elif 4 in active_bells and 5 in active_bells:
            return "BUY"
        
        # Bearish signals (Bells 2, 6, 7 active with high intensity)
        if 2 in active_bells and 6 in active_bells and intensities[6] > 0.8:
            return "STRONG_SELL" 
        elif 2 in active_bells and 7 in active_bells:
            return "SELL"
        
        # Neutral/Ranging signals (Bells 1, 3 dominant)
        if 1 in active_bells and 3 in active_bells and intensities[1] > 0.5:
            return "HOLD"
        
        return "NEUTRAL"
