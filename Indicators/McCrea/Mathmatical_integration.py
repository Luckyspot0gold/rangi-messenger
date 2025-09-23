class McCreaMarketIndicators:
    def __init__(self):
        self.hri_calculator = MathematicalHRI()
        self.sss_calculator = MathematicalSSS()
        self.hiv_calculator = MathematicalHIV()
        
    def calculate_all_indicators(self, price_data, volume_data, timestamp_data):
        """
        Comprehensive indicator calculation with mathematical rigor
        """
        # Convert to numpy arrays for mathematical operations
        prices = np.array(price_data)
        volumes = np.array(volume_data)
        
        # Calculate each indicator with proper error handling
        try:
            hri = self.hri_calculator.harmonic_resonance_index(prices, volumes)
            sss = self.sss_calculator.sonic_stability_score(prices)
            hiv = self.hiv_calculator.harmonic_investment_velocity(prices, volumes)
            
            # Additional mathematically sound indicators
            hrs = self.harmonic_risk_score(prices, hri, sss)
            iss = self.investment_sonic_signature(prices, volumes)
            
        except Exception as e:
            # Fallback to robust calculations
            print(f"Indicator calculation error: {e}")
            hri, sss, hiv, hrs, iss = self.robust_calculations(prices, volumes)
        
        return {
            'HRI': round(hri, 2),
            'SSS': round(sss, 2),
            'HIV': round(hiv, 2),
            'HRS': round(hrs, 2),
            'ISS': round(iss, 2),
            'timestamp': timestamp_data[-1]
        }
    
    def harmonic_risk_score(self, prices, hri, sss):
        """HRS based on volatility, correlation, and stability metrics"""
        returns = np.diff(np.log(prices))
        volatility = np.std(returns) * np.sqrt(252)  # Annualized
        drawdown = self.max_drawdown(prices)
        
        # Combine risk factors
        risk_score = (volatility * 10) + (drawdown * 100) + ((100 - sss) * 0.5)
        return min(100, risk_score)
    
    def investment_sonic_signature(self, prices, volumes):
        """ISS as a unique fingerprint of market state"""
        # Use multiple timeframes and frequencies
        short_term = prices[-50:]
        medium_term = prices[-200:]
        
        # Multi-scale analysis
        st_vol = np.std(np.diff(np.log(short_term)))
        mt_vol = np.std(np.diff(np.log(medium_term)))
        volume_ratio = volumes[-1] / np.mean(volumes[-20:])
        
        # Create unique signature
        iss = 50 + (st_vol * 1000) + (mt_vol * 500) + (volume_ratio * 10)
        return min(100, max(0, iss % 100))
    
    def max_drawdown(self, prices):
        """Calculate maximum drawdown for risk assessment"""
        peak = prices[0]
        max_dd = 0
        
        for price in prices:
            if price > peak:
                peak = price
            dd = (peak - price) / peak
            if dd > max_dd:
                max_dd = dd
                
        return max_dd
