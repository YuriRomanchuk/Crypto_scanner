import ccxt
import time
from colorama import init, Fore, Back, Style


init(autoreset=True)



def crypto_scanner():
    exchange = ccxt.bybit({'enableRateLimit': True})
    print("Loading crypto markets from Bybit")
    markets = exchange.load_markets()

    usdt_pairs = [symbol for symbol in markets.keys() if symbol.endswith('/USDT')] 
    test__pairs = usdt_pairs[:30]

    print(f"Scanning {len(test__pairs)} on 5 minute frame\n")

    for symbol in test__pairs:
        try:
            ohlv = exchange.fetch_ohlcv(symbol, timeframe='5m', limit=10)
            if len(ohlv) < 10:
                continue
            volumes = [candle[5] for candle in ohlv ]
            current_volume = volumes[-1]

            past_volume = volumes[:-1]
            avg_volume = sum(past_volume) / len(past_volume)

            if avg_volume > 0 and current_volume > (avg_volume* 3):
                ratio = current_volume / avg_volume
                print(Fore.RED + f"FOUND:{symbol}\n")
                print(Fore.GREEN + f"Agarage volume: {avg_volume:.2f} psc\n")
                print(Fore.GREEN + f"Current volume: {current_volume:.2f} psc\n")
                print(Fore.YELLOW + f"Increased by: {ratio:.2f}\n")
            time.sleep(0.2)

        except Exception as e:
            pass
    print("Scanning End!")
if __name__ == '__main__':
    crypto_scanner()        