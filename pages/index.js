export default function Home() {
  return (
    <div className="container">
      <header>
        <h1>Welcome to ScalpIQ</h1>
        <p>Your all-in-one trading companion.</p>
        <nav style={{ marginTop: '1.5rem' }}>
          <a href="/pulse" style={{ marginRight: '1rem', color: '#0ef' }}>Pulse</a>
          <a href="/companion" style={{ marginRight: '1rem', color: '#0ef' }}>Companion</a>
          <a href="/journal" style={{ color: '#0ef' }}>Journal</a>
        </nav>
      </header>
    </div>
  );
}