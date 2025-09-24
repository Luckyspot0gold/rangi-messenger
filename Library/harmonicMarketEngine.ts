// lib/harmonicMarketEngine.ts
import { CymaticsGenerator } from './cymaticsGenerator';
import { HapticPulseEngine } from './hapticEngine';

export class HarmonicMarketEngine {
  private cymatics: CymaticsGenerator;
  private haptics: HapticPulseEngine;
  private audioContext: AudioContext | null = null;
  private isPlaying = false;

  constructor() {
    this.cymatics = new CymaticsGenerator();
    this.haptics = new HapticPulseEngine();
  }

  // Core market harmony mapping
  async playMarketHarmony(marketData: MarketSnapshot): Promise<void> {
    const harmonyProfile = this.analyzeMarketHarmony(marketData);
    
    // Synchronized multi-sensory experience
    await Promise.all([
      this.playHarmonicFrequencies(harmonyProfile),
      this.triggerHapticBeats(harmonyProfile),
      this.renderCymaticPatterns(harmonyProfile)
    ]);
  }

  private analyzeMarketHarmony(data: MarketSnapshot): HarmonyProfile {
    const { price, volume, volatility, trend } = data;
    
    return {
      // 7-Bell frequencies based on market conditions
      primaryFrequency: this.calculatePrimaryFrequency(price, trend),
      secondaryFrequency: this.calculateHarmonicOvertone(volatility),
      rhythmPattern: this.calculateRhythm(volume),
      intensity: Math.min(1.0, volatility * 10),
      marketMood: this.determineMarketMood(trend, volatility)
    };
  }

  private calculatePrimaryFrequency(price: number, trend: number): number {
    // 432Hz base modulated by price and trend
    const base = 432;
    const priceModulation = (price % 1000) / 1000; // Use price decimals for variation
    const trendModulation = trend * 50;
    
    return base + priceModulation * 20 + trendModulation;
  }

  private calculateHarmonicOvertone(volatility: number): number {
    // Fibonacci-based overtones
    const overtones = [86, 111.11, 256, 528, 741, 963];
    const index = Math.min(Math.floor(volatility * 10), overtones.length - 1);
    return overtones[index];
  }

  private calculateRhythm(volume: number): number[] {
    // Convert volume to rhythmic pattern
    const baseBPM = 60 + (volume / 1000000) * 120; // Scale volume to BPM
    return this.generateRhythmPattern(baseBPM);
  }

  private generateRhythmPattern(bpm: number): number[] {
    const beatInterval = 60000 / bpm; // ms per beat
    return [
      beatInterval,       // Main beat
      beatInterval * 0.5, // Half beat
      beatInterval * 0.25 // Quarter beat
    ];
  }
}
