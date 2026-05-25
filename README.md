# Crypto Volume Anomaly Scanner

A high-performance, lightweight Python script designed to monitor cryptocurrency markets and detect abnormal trading volume spikes in real-time. By analyzing order flow and volume surges, this tool helps identify potential price breakouts or insider accumulation before major price movements occur.

## ⚙️ Features
* **Real-time Scanning:** Monitors spot pairs (`/USDT`) on the Bybit exchange.
* **Smart Detection:** Calculates the average volume of the previous 9 candles (5-minute timeframe) and triggers an alert if the current candle's volume exceeds the average by 3x or more.
* **No API Keys Required:** Utilizes public exchange data, making it safe and easy to run without exposing personal exchange accounts.
* **Scalable:** Built on top of the industry-standard `ccxt` library, meaning it can be easily expanded to support Binance, OKX, Coinbase, and 100+ other exchanges.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Libraries:** `ccxt` (for exchange API integration)
