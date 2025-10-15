import { useState, useEffect } from 'react';
import Head from 'next/head';

export default function PinkManPanel() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch('http://localhost:3000/route', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({ type: 'ai-avatar', data: { query: 'Hello, PinkMan!' } }),
        });
        const result = await response.json();
        setData(result);
      } catch (e) {
        setError('Failed to fetch data');
      }
    };
    fetchData();
  }, []);

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <Head>
        <title>PinkMan AI Panel</title>
      </Head>
      <h1 className="text-xl font-bold mb-4">PinkMan AI Panel</h1>
      {error && <p className="text-red-500">{error}</p>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
