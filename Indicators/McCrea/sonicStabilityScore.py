import numpy as np
from scipy import stats

class MathematicalSSS:
    def shannon_entropy(self, data):
        """Calculate Shannon entropy of price movements"""
        # Bin data into discrete states
        hist, bin_edges = np.histogram(data, bins=20, density=True)
        hist = hist[hist > 0]  # Remove zero bins
        return -np.sum(hist * np.log2(hist))
    
    def hurst_exponent(self, data):
        """Calculate Hurst exponent for market persistence"""
        n = len(data)
        max_lag = min(100, n//4)
        
        lags = range(2, max_lag)
        tau = [np.std(np.subtract(data[lag:], data[:-lag])) for lag in lags]
        
        # Calculate Hurst exponent
        hurst = np.polyfit(np.log(lags), np.log(tau), 1)[0]
        return hurst
    
    def sonic_stability_score(self, price_series, window=50):
        """
        SSS based on entropy, volatility, and market efficiency
        Formula: SSS = 100 × exp(-(H_entropy + |H_hurst - 0.5| + σ_normalized))
        """
        returns = np.diff(np.log(price_series))
        
        # Recent window for calculation
        recent_returns = returns[-window:]
        
        # Components of stability
        entropy = self.shannon_entropy(recent_returns)
        hurst = self.hurst_exponent(recent_returns)
        volatility = np.std(recent_returns)
        
        # Normalize components
        entropy_norm = entropy / np.log2(20)  # Max entropy for 20 bins
        hurst_deviation = abs(hurst - 0.5)   # 0.5 = random walk
        vol_norm = volatility / 0.02         # Normalize to 2% daily vol
        
        # Combined stability score
        instability = entropy_norm + hurst_deviation + vol_norm
        sss = 100 * np.exp(-instability)
        
        return min(100, max(0, sss))
