import numpy as np
from scipy.fft import fft, fftfreq
import pandas as pd

class MathematicalHRI:
    def __init__(self, base_frequencies=[86, 111.11, 432, 753, 1074, 1395, 1618]):
        self.base_frequencies = base_frequencies
        self.golden_ratio = (1 + np.sqrt(5)) / 2
        
    def calculate_spectral_power(self, price_series):
        """Calculate power spectrum using Fourier analysis"""
        n = len(price_series)
        yf = fft(price_series)
        xf = fftfreq(n, 1)
        
        # Get power spectral density
        power_spectrum = np.abs(yf[:n//2])**2
        frequencies = xf[:n//2]
        
        return frequencies, power_spectrum
    
    def harmonic_resonance_index(self, price_data, volume_data, time_period=24):
        """
        HRI based on Fourier analysis and energy distribution
        Formula: HRI = Σ(P(f_i) × exp(-|f_i - f_base|/σ)) / Σ(P(f_i))
        """
        # Normalize price and volume data
        price_returns = np.diff(np.log(price_data))
        volume_normalized = volume_data / np.max(volume_data)
        
        # Combined signal for analysis
        combined_signal = price_returns * volume_normalized[1:]
        
        # Fourier analysis
        freqs, power = self.calculate_spectral_power(combined_signal)
        
        # Calculate resonance with your 7 bells
        resonance_scores = []
        for base_freq in self.base_frequencies:
            # Gaussian weighting around each base frequency
            weights = np.exp(-((freqs - base_freq/1000)**2) / (2*0.1**2))
            resonance = np.sum(power * weights) / np.sum(power)
            resonance_scores.append(resonance)
        
        # Final HRI (0-100 scale)
        hri = 100 * (np.sum(resonance_scores) / len(self.base_frequencies))
        return min(100, max(0, hri))
