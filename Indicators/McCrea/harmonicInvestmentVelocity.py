import pywt
import numpy as np

class MathematicalHIV:
    def wavelet_energy_distribution(self, data, wavelet='db4', level=4):
        """Analyze energy distribution across frequency bands using wavelets"""
        coeffs = pywt.wavedec(data, wavelet, level=level)
        
        # Calculate energy in each frequency band
        energy_by_level = [np.sum(np.square(c)) for c in coeffs]
        total_energy = np.sum(energy_by_level)
        
        return [e/total_energy for e in energy_by_level]
    
    def momentum_indicators(self, price_series):
        """Calculate multiple momentum indicators"""
        returns = np.diff(np.log(price_series))
        
        # Rate of Change
        roc_5 = (price_series[-1] / price_series[-5] - 1) * 100
        roc_10 = (price_series[-1] / price_series[-10] - 1) * 100
        
        # Moving average convergence
        ma_short = np.mean(price_series[-5:])
        ma_long = np.mean(price_series[-20:])
        macd = (ma_short - ma_long) / ma_long * 100
        
        return roc_5, roc_10, macd
    
    def harmonic_investment_velocity(self, price_series, volume_series):
        """
        HIV based on wavelet analysis and momentum physics
        Formula: HIV = √(Σ(w_i × E_i) × |∇P| × V_norm)
        """
        returns = np.diff(np.log(price_series))
        
        # Wavelet energy analysis
        energy_dist = self.wavelet_energy_distribution(returns)
        
        # High-frequency energy (represents velocity)
        high_freq_energy = np.sum(energy_dist[:2])  # First two levels
        
        # Price gradient (momentum)
        price_gradient = abs(returns[-1])
        
        # Volume normalization
        volume_norm = volume_series[-1] / np.mean(volume_series[-20:])
        
        # Combined velocity measure
        hiv = 100 * np.sqrt(high_freq_energy * price_gradient * min(volume_norm, 3))
        
        return min(100, max(0, hiv))
