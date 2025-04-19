export default function handler(req, res) {
  res.status(200).json([
    { email: 'user1@example.com', role: 'subscriber' },
    { email: 'admin@example.com', role: 'admin' }
  ]);
}