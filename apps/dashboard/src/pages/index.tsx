import { useState } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';

export default function Dashboard() {
  const [token, setToken] = useState('');
  const router = useRouter();

  const login = async () => {
    // Przykład: Fetch token z auth service
    try {
      const response = await fetch('http://localhost:3001/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: 'admin', password: 'pass123' }),
      });
      const data = await response.json();
      setToken(data.token);
      localStorage.setItem('token', data.token);
    } catch (e) {
      console.error('Login failed', e);
    }
  };

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <Head>
        <title>MetaGeniusz Dashboard</title>
      </Head>
      <h1 className="text-2xl font-bold mb-4">MetaGeniusz Ecosystem Dashboard</h1>
      {!token && (
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={login}
        >
          Login
        </button>
      )}
      {token && (
        <nav className="flex gap-4">
          <button
            className="bg-gray-200 px-4 py-2 rounded"
            onClick={() => router.push('/agents/anonymous')}
          >
            Anonymous Agent
          </button>
          <button
            className="bg-gray-200 px-4 py-2 rounded"
            onClick={() => router.push('/agents/pinkman')}
          >
            PinkMan AI
          </button>
        </nav>
      )}
    </div>
  );
}
