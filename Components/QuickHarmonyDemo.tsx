// components/QuickHarmonyDemo.tsx
'use client';
import { useCallback } from 'react';

export function QuickHarmonyDemo() {
  const playBasicHarmony = useCallback(async () => {
    // Simple 432Hz + haptic demo
    const audioContext = new AudioContext();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = 432;
    oscillator.type = 'sine';
    gainNode.gain.value = 0.1;
    
    oscillator.start();
    
    // Sync with haptic vibration
    if (navigator.vibrate) {
      navigator.vibrate([100, 50, 100, 50, 200]);
    }
    
    setTimeout(() => {
      oscillator.stop();
    }, 2000);
  }, []);

  return (
    <button 
      onClick={playBasicHarmony}
      className="bg-gradient-to-r from-orange-500 to-red-500 text-white px-8 py-4 rounded-lg text-xl font-bold animate-pulse"
    >
      🌊 Experience Market Harmony
    </button>
  );
}
