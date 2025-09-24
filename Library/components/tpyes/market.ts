// types/market.ts
export interface MarketSnapshot {
  price: number;
  volume: number;
  volatility: number;
  trend: number;
  timestamp: number;
}

export interface HarmonyProfile {
  primaryFrequency: number;
  secondaryFrequency: number;
  rhythmPattern: number[];
  intensity: number;
  marketMood: 'calm' | 'volatile' | 'trending' | 'critical';
}

export interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  life: number;
  frequency: number;
}
