import numpy as np
from scipy.signal import find_peaks
import math

class SevenBellHarmonySystem:
    def __init__(self):
        # Define the complete 7-bell system with 432Hz as Bell #4 (Baseline)
        self.bells = {
            1: {"frequency": 86.0, "name": "Foundation Bell", "purpose": "Market Grounding"},
            2: {"frequency": 111.11, "name": "Llama Return Bell", "purpose": "Cycle Completion"}, 
            3: {"frequency": 256.0, "name": "Middle C Resonance", "purpose": "Structural Harmony"},
            4: {"frequency": 432.0, "name": "Universal Heartbeat", "purpose": "Baseline Reality"},
            5: {"frequency": 528.0, "name": "Love Frequency", "purpose": "Positive Momentum"},
            6: {"frequency": 741.0, "name": "Awakening Bell", "purpose": "Market Awareness"},
            7: {"frequency": 963.0, "name": "Crown Connection", "purpose": "Higher Perspective"}
        }
        
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        self.pythagorean_comma = 1.01364326477  # Musical mathematical constant
        
    def get_bell_frequencies(self):
        """Return all 7 frequencies in harmonic order"""
        return [self.bells[i]["frequency"] for i in range(1, 8)]
    
    def calculate_harmonic_relationships(self):
        """Calculate mathematical relationships between bells"""
        frequencies = self.get_bell_frequencies()
        relationships = {}
        
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies)):
                ratio = frequencies[j] / frequencies[i]
                relationship = self.classify_interval(ratio)
                relationships[f"Bell_{i+1}_to_{j+1}"] = {
                    "ratio": round(ratio, 4),
                    "interval": relationship,
                    "freq_pair": (frequencies[i], frequencies[j])
                }
        
        return relationships
    
    def classify_interval(self, ratio):
        """Classify the musical interval based on frequency ratio"""
        interval_map = {
            1.0: "Unison",
            1.059: "Minor Second",
            1.122: "Major Second", 
            1.189: "Minor Third",
            1.26: "Major Third",
            1.335: "Perfect Fourth",
            1.414: "Tritone",
            1.5: "Perfect Fifth",
            1.587: "Minor Sixth",
            1.682: "Major Sixth",
            1.782: "Minor Seventh",
            1.888: "Major Seventh",
            2.0: "Octave"
        }
        
        # Find closest standard interval
        closest_interval = min(interval_map.keys(), key=lambda x: abs(x - ratio))
        return interval_map[closest_interval] if abs(closest_interval - ratio) < 0.05 else "Unique Interval"
