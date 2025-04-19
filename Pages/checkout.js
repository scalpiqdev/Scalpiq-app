export default function handler(req, res) {
  res.status(200).json({ url: 'https://stripe.com/checkout/session/mock' });
}