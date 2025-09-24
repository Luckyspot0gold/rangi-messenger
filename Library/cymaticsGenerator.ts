// lib/cymaticsGenerator.ts
export class CymaticsGenerator {
  private canvas: HTMLCanvasElement;
  private ctx: CanvasRenderingContext2D;
  private particles: Particle[] = [];

  constructor() {
    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d')!;
    this.setupCanvas();
  }

  renderCymaticPattern(harmony: HarmonyProfile): void {
    const { primaryFrequency, secondaryFrequency, intensity } = harmony;
    
    this.ctx.fillStyle = 'black';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Chladni plate patterns based on frequency
    this.drawChladniPattern(primaryFrequency, intensity, '#ff6b35');
    this.drawInterferencePattern(secondaryFrequency, intensity * 0.7, '#00aaff');
    this.drawHarmonicRings(primaryFrequency, secondaryFrequency);
    
    this.animateParticles(intensity);
  }

  private drawChladniPattern(freq: number, intensity: number, color: string): void {
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;
    const maxRadius = Math.min(centerX, centerY) * 0.8;

    this.ctx.strokeStyle = color;
    this.ctx.lineWidth = 2 + intensity * 3;
    this.ctx.beginPath();

    // Chladni pattern formula: standing waves
    for (let angle = 0; angle < Math.PI * 2; angle += 0.01) {
      const n = Math.floor(freq / 50); // Mode number based on frequency
      const r = maxRadius * Math.abs(Math.sin(n * angle)) * intensity;
      
      const x = centerX + Math.cos(angle) * r;
      const y = centerY + Math.sin(angle) * r;
      
      if (angle === 0) {
        this.ctx.moveTo(x, y);
      } else {
        this.ctx.lineTo(x, y);
      }
    }
    
    this.ctx.closePath();
    this.ctx.stroke();
  }

  private drawInterferencePattern(freq: number, intensity: number, color: string): void {
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;
    
    this.ctx.strokeStyle = color;
    this.ctx.globalAlpha = 0.6;
    
    // Wave interference pattern
    for (let i = 0; i < 10; i++) {
      const phase = (i / 10) * Math.PI * 2;
      const amplitude = intensity * 50;
      
      this.ctx.beginPath();
      for (let x = 0; x < this.canvas.width; x += 2) {
        const wave1 = Math.sin(x * freq * 0.01 + phase) * amplitude;
        const wave2 = Math.sin((x + 50) * freq * 0.008 + phase) * amplitude * 0.7;
        const y = centerY + wave1 + wave2;
        
        if (x === 0) this.ctx.moveTo(x, y);
        else this.ctx.lineTo(x, y);
      }
      this.ctx.stroke();
    }
    this.ctx.globalAlpha = 1.0;
  }
}
