// components/LiveMarketHarmony.tsx
'use client';
import { useEffect, useRef, useState } from 'react';
import { HarmonicMarketEngine } from '../lib/harmonicMarketEngine';

export function LiveMarketHarmony() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [engine, setEngine] = useState<HarmonicMarketEngine | null>(null);
  const [marketData, setMarketData] = useState<MarketSnapshot | null>(null);

  useEffect(() => {
    const harmonicEngine = new HarmonicMarketEngine();
    setEngine(harmonicEngine);
    
    // Simulate real-time market data
    const marketStream = setInterval(() => {
      setMarketData(generateMockMarketData());
    }, 2000);

    return () => {
      clearInterval(marketStream);
      harmonicEngine.cleanup();
    };
  }, []);

  useEffect(() => {
    if (engine && marketData) {
      engine.playMarketHarmony(marketData);
    }
  }, [engine, marketData]);

  return (
    <div className="relative w-full h-screen bg-black overflow-hidden">
      {/* Cymatic Visualization Canvas */}
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full"
        width={1920}
        height={1080}
      />
      
      {/* Market Data Overlay */}
      <div className="absolute top-4 left-4 text-white bg-black/50 p-4 rounded-lg">
        <h3 className="text-xl font-bold mb-2">Market Harmony</h3>
        {marketData && (
          <div className="space-y-1">
            <div>Price: ${marketData.price.toFixed(2)}</div>
            <div>Volatility: {(marketData.volatility * 100).toFixed(1)}%</div>
            <div>Trend: {(marketData.trend * 100).toFixed(1)}%</div>
          </div>
        )}
      </div>

      {/* Harmonic Controls */}
      <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2">
        <button
          onClick={() => engine?.playMarketHarmony(marketData!)}
          className="bg-gradient-to-r from-purple-600 to-blue-600 text-white px-6 py-3 rounded-full font-bold hover:scale-105 transition-transform"
        >
          🎵 Play Market Harmony
        </button>
      </div>
    </div>
  );
}

// Mock data generator
function generateMockMarketData(): MarketSnapshot {
  return {
    price: 50000 + Math.random() * 10000,
    volume: 1000000 + Math.random() * 5000000,
    volatility: Math.random() * 0.1,
    trend: (Math.random() - 0.5) * 0.2,
    timestamp: Date.now()
  };
}
