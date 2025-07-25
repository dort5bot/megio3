import asyncio
import random
from datetime import datetime, time, timedelta
import aiohttp
import os
import csv

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

STABLE_COINS = ["USDT", "BUSD", "FDUSD", "USDC", "TUSD"]

async def fetch_binance_24h_tickers():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as resp:
            return await resp.json()

async def get_io_report():
    # Gerçek veriler Binance API ile çekilecek
    tickers = await fetch_binance_24h_tickers()
    total_volume = 0
    stable_volume = 0
    top_inflows = []

    for t in tickers:
        volume = float(t.get("quoteVolume", 0))
        total_volume += volume
        symbol = t.get("symbol", "")
        # Stabil coin için parite USDT ile olanları kontrol et
        if any(sc in symbol for sc in STABLE_COINS):
            stable_volume += volume

    # Önceki kaydı oku
    filepath = f"{DATA_DIR}/io_history.csv"
    prev_total = 0
    prev_stable = 0
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            rows = list(csv.reader(f))
            if len(rows) > 1:
                last = rows[-1]
                prev_total = float(last[1])
                prev_stable = float(last[2])

    # Değişim hesapla
    total_change_pct = ((total_volume - prev_total) / prev_total * 100) if prev_total > 0 else 0
    stable_change_val = stable_volume - prev_stable

    # CSV'ye kaydet
    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)
        if os.path.getsize(filepath) == 0:
            writer.writerow(["timestamp", "total_volume", "stable_volume"])
        writer.writerow([datetime.utcnow().isoformat(), total_volume, stable_volume])

    # Rapor formatı
    report = (
        f"📊 IO Raporu
"
        f"Market Hacmi: {total_volume / 1e9:.2f}B$
"
        f"Marketteki Hacim Payı: %{random.uniform(80, 85):.1f}
"
        f"Kısa Vadeli Alım Gücü: {random.uniform(0.5, 0.7):.2f}X

"
        f"🌐 Genel Nakit Değişimi: {total_change_pct:+.1f}% {'🔼' if total_change_pct >= 0 else '🔻'}
"
        f"💵 Stabil Coin Net Akışı (24h): {stable_change_val/1e6:+.0f}M$ {'🔼' if stable_change_val >= 0 else '🔻'}
"
        f"
💰 En Çok Nakit Girişi Raporu:
"
    )

    # En çok nakit girişi simülasyonu - gerçek değil, demo amaçlı 5 coin
    top_coins = [("ETH", 21.1, 54, 1.3), ("BAKE", 19.5, 47, 1.0), ("BNB", 15.2, 50, 1.1)]
    for coin, perc, m15, mts in top_coins:
        arrows = "".join("🔼" if i%2==0 else "🔻" for i in range(5))
        report += f"{coin}: %{perc} | 15m: {m15}% | Mts: {mts} {arrows}
"

    return report, {"total_volume": total_volume, "stable_volume": stable_volume}

async def get_nls_signal(pattern):
    return f"🔔 NLS Sinyali | Pattern: {pattern or 'GENEL'} | RSI:{random.uniform(20,70):.2f}"

async def get_npr_signal(days=None, coins=[]):
    # Simüle edilmiş veri
    base_score = 58.2
    trend_change = 2.1
    output = "📈 NPR Pazar Raporu

"
    if days:
        output += f"(Son {days} gün ortalaması ile karşılaştırma)

"
    output += f"Genel NPR: {base_score:.1f}% ({trend_change:+.1f}%) {'🔼' if trend_change>=0 else '🔻'}

"
    for t in ["15m", "1h", "4h", "12h", "1d"]:
        output += f"{t}: {random.uniform(40, 60):.2f}% {'🔻' if random.random() > 0.5 else '🔼'}
"
    output += "
Trend: Orta vadede toparlanma sinyali, kısa vadede zayıflama devam ediyor.

"

    if coins:
        output = f"📈 NPR Coin Raporu ({', '.join(coins)})

"
        for coin in coins:
            vals = [random.uniform(40,60) for _ in range(5)]
            arrows = ["🔼" if v >= 50 else "🔻" for v in vals]
            output += f"{coin} → " + " | ".join(f"{v:.1f}% {a}" for v,a in zip(vals, arrows)) + "
"
    return output

async def get_etf_report(args):
    # demo veri
    return "📊 ETF Raporu (demo)
BTC: 123M$ (+1.2%)
ETH: 98M$ (-0.5%)"

