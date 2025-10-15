import React, { useState, useEffect } from 'react';
import { useGoogleLogin } from '@react-oauth/google';

const App = () => {
    const [task, setTask] = useState('');
    const [result, setResult] = useState(null);
    const [migiResult, setMigiResult] = useState(null);
    const [error, setError] = useState(null);
    const [user, setUser] = useState(null);

    const login = useGoogleLogin({
        onSuccess: async (tokenResponse) => {
            const userInfo = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
                headers: { Authorization: `Bearer ${tokenResponse.access_token}` }
            });
            setUser(await userInfo.json());
        },
        onError: () => setError('Błąd logowania')
    });

    const handleSubmit = async () => {
        if (!user) {
            setError('Zaloguj się, aby kontynuować');
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/run_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${user.access_token}`
                },
                body: JSON.stringify({ payload: task })
            });
            const data = await response.json();
            if (data.error) {
                setError(data.error);
                setResult(null);
            } else {
                setResult(data);
                setError(null);
            }

            const migiResponse = await fetch('http://localhost:8000/api/migi_7g', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${user.access_token}`
                },
                body: JSON.stringify({ task })
            });
            const migiData = await migiResponse.json();
            setMigiResult(migiData);
        } catch (err) {
            setError('Błąd połączenia z serwerem');
            setResult(null);
            setMigiResult(null);
        }
    };

    return (
        <div className="max-w-md mx-auto p-6 bg-white rounded-lg shadow-lg">
            <h1 className="text-2xl font-bold mb-4 text-center">Mózg Boga</h1>
            {!user ? (
                <button
                    className="w-full bg-green-500 text-white p-2 rounded hover:bg-green-600 mb-4"
                    onClick={() => login()}
                >
                    Zaloguj się z Google
                </button>
            ) : (
                <p className="mb-4">Zalogowano jako: {user.email}</p>
            )}
            <div className="mb-4">
                <label className="block text-gray-700 mb-2">Wprowadź zadanie:</label>
                <textarea
                    className="w-full p-2 border rounded"
                    rows="4"
                    value={task}
                    onChange={(e) => setTask(e.target.value)}
                    placeholder="Np. Zaprojektuj robota..."
                />
            </div>
            <button
                className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
                onClick={handleSubmit}
                disabled={!task || !user}
            >
                Uruchom cykl
            </button>
            {result && (
                <div className="mt-4 p-4 bg-gray-100 rounded">
                    <p><strong>Wynik:</strong> {result.message}</p>
                    <p><strong>Sukces:</strong> {result.success_pct}%</p>
                    <p><strong>Strategia:</strong> {result.strategy}</p>
                    <p><strong>Użytkownik:</strong> {result.user}</p>
                </div>
            )}
            {migiResult && (
                <div className="mt-4 p-4 bg-blue-100 rounded">
                    <p><strong>MIGI 7G:</strong> Wkład: {migiResult.contribution}</p>
                    <p><strong>Liczba deweloperów:</strong> {migiResult.mock_developers}</p>
                    <p><strong>Użytkownik:</strong> {migiResult.user}</p>
                </div>
            )}
            {error && (
                <div className="mt-4 p-4 bg-red-100 text-red-700 rounded">
                    <p><strong>Błąd:</strong> {error}</p>
                </div>
            )}
        </div>
    );
};

export default App;