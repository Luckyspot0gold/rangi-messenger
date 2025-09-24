// lib/hapticEngine.ts
export class HapticPulseEngine {
  private vibrationSupported = false;

  constructor() {
    this.vibrationSupported = 'vibrate' in navigator;
  }

  async triggerMarketBeat(harmony: HarmonyProfile): Promise<void> {
    if (!this.vibrationSupported) return;

    const pattern = this.createHapticPattern(harmony);
    
    try {
      // Multi-layered haptic experience
      await this.executeHapticPattern(pattern);
      await this.addHapticTexture(harmony.intensity);
    } catch (error) {
      console.warn('Haptic feedback not supported:', error);
    }
  }

  private createHapticPattern(harmony: HarmonyProfile): number[] {
    const { rhythmPattern, intensity, marketMood } = harmony;
    
    let pattern: number[] = [];
    
    switch (marketMood) {
      case 'calm':
        pattern = this.createCalmPattern(rhythmPattern, intensity);
        break;
      case 'volatile':
        pattern = this.createVolatilePattern(rhythmPattern, intensity);
        break;
      case 'trending':
        pattern = this.createTrendingPattern(rhythmPattern, intensity);
        break;
      case 'critical':
        pattern = this.createCriticalPattern(rhythmPattern, intensity);
        break;
    }
    
    return pattern;
  }

  private createCalmPattern(rhythm: number[], intensity: number): number[] {
    // Gentle, rhythmic pulses
    return [
      rhythm[0] * intensity, // vibration
      rhythm[1] * 0.5,       // pause
      rhythm[0] * intensity * 0.7
    ];
  }

  private createVolatilePattern(rhythm: number[], intensity: number): number[] {
    // Rapid, irregular pulses
    return [
      rhythm[2] * intensity * 2, // quick vibration
      rhythm[2] * 0.3,           // short pause
      rhythm[2] * intensity * 1.5,
      rhythm[1] * 0.5,
      rhythm[2] * intensity * 2
    ];
  }
}
