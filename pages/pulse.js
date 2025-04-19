export default function Pulse() {
  const topTickers = ['META', 'TSLA', 'NVDA', 'SPY', 'AAPL'];

  return (
    <div className="container">
      <h2>ScalpIQ Pulse</h2>
      <p>Today's Top 5 Watchlist Tickers:</p>
      <ul>
        {topTickers.map((ticker, i) => (
          <li key={i}>{ticker}</li>
        ))}
      </ul>
    </div>
  );
}