graph TD
    A[External Data Sources<br>(Market APIs: CoinGecko, Coinbase;<br>User Intent Signals; Sensor Data)]
    B[AETHER NET<br>(Real-time Data Mesh)]
    C[UNIFIED ENERGY<br>(Data Normalization & Sonification Engine)]
    D[CHRONOS ENGINE<br>(State-Space Simulation & Timeline Database)]
    E[User Interfaces<br>(Web/Mobile: Sonic/Haptic Outputs;<br>AI Agent Responses)]

    A -->|Ingest Market Data, Sensors, Intents| B
    B -->|Raw Data Streams| C
    C -->|Normalized Amplitudes & Sensory Signatures| D
    D -->|Simulated Scenarios & Temporal States| E
    C -->|Direct Sensory Feedback| E
    B <-->|Bidirectional Sync| D
graph TD
    A[User Input<br>(Holdings Symbols: e.g., AAPL, MSFT, VTI;<br>Preferences: Thresholds, Email/Phone)]
    B[External Data Sources<br>(Market APIs: Finnhub/Alpha Vantage for Stock/Bond Data;<br>News APIs: SSA RSS, Economic Indicators via FRED API)]
    C[AETHER NET<br>(Real-time Data Mesh: Ingest Holdings Data, Bond Volatility, SS News)]
    D[UNIFIED ENERGY<br>(Data Normalization & Sonification: Compute Stress/Health/Security Scores;<br>Generate Tones, Colors, Haptics)]
    E[CHRONOS ENGINE<br>(State-Space Simulation: Weekly Reports, What-If Scenarios for SS Changes)]
    F[Notification Outputs<br>(AWS SNS: Haptic Pulses, Audio Tones via Mobile Push;<br>Email/Text Reports)]

    A -->|Onboarding Symbols & Settings| C
    B -->|Ingest Market/Economic/SS Data| C
    C -->|Raw Streams| D
    D -->|Normalized Scores & Sensory Data| E
    E -->|Simulated States & Reports| F
    D -->|Threshold-Based Alerts| F
    C <-->|Sync for Temporal Analysis| E
