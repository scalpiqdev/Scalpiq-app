import Link from 'next/link';
export default function Home() {
  return (
    <main style={{ padding: '2rem', background: '#0e0e0e', color: '#fff' }}>
      <h1>ScalpIQ Hub</h1>
      <nav><Link href="/companion">Companion</Link> | <Link href="/trades">Trades</Link> | <Link href="/pulse">Pulse</Link> | <Link href="/dashboard">Dashboard</Link></nav>
    </main>
  );
}