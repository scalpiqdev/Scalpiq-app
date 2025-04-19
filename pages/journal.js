export default function Journal() {
  const today = new Date().toLocaleDateString();

  return (
    <div className="container">
      <h2>Trade Journal for {today}</h2>
      <p>No trades logged yet. Start your session to begin tracking.</p>
    </div>
  );
}