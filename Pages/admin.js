import { useEffect, useState } from 'react';
export default function Admin() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetch('/api/users').then(res => res.json()).then(setUsers);
  }, []);
  return (
    <div style={{ padding: 20, background: '#0e0e0e', color: '#fff' }}>
      <h2>Admin Dashboard</h2>
      <ul>{users.map((u, i) => <li key={i}>{u.email} — {u.role}</li>)}</ul>
    </div>
  );
}