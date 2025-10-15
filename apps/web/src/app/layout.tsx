'use client';

import { Web3Provider } from '../components/Web3Provider';
import '../styles/globals.css';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Hip-Hop Universe - Demo</title>
        <meta name="description" content="Hip-Hop Universe - Web3 Demo with DRT Token and Consciousness NFTs" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <Web3Provider>
          <div className="min-h-screen bg-dark-bg">
            <header className="glassmorphism">
              <div className="container mx-auto px-4 py-6">
                <div className="flex justify-between items-center">
                  <h1 className="text-2xl font-bold gradient-text">
                    🎵 Hip-Hop Universe
                  </h1>
                  <div className="text-sm text-gray-400">
                    Web3 Demo - {process.env.NEXT_PUBLIC_NETWORK === 'polygon' ? 'Polygon' : 'Mumbai Testnet'}
                  </div>
                </div>
              </div>
            </header>
            <main className="container mx-auto px-4 py-8">
              {children}
            </main>
            <footer className="mt-16 py-8 border-t border-gray-800">
              <div className="container mx-auto px-4 text-center text-gray-400">
                <p>Hip-Hop Universe © 2025 - Where Culture Meets Consciousness</p>
              </div>
            </footer>
          </div>
        </Web3Provider>
      </body>
    </html>
  );
}