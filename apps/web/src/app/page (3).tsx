'use client';

import { useState } from 'react';
import { WalletInfo } from '../components/WalletInfo';
import { ConsciousnessNFTDemo } from '../components/ConsciousnessNFTDemo';
import { DRTTokenDemo } from '../components/DRTTokenDemo';

export default function HomePage() {
  const [activeTab, setActiveTab] = useState<'wallet' | 'drt' | 'nft'>('wallet');

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="text-center py-12">
        <h1 className="text-5xl font-bold gradient-text mb-6">
          Hip-Hop Universe
        </h1>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto mb-8">
          Experience the future of cultural-consciousness integration. 
          Connect your wallet to interact with DRT tokens and Consciousness NFTs.
        </p>
        <div className="flex justify-center space-x-4">
          <div className="glassmorphism px-4 py-2 rounded-lg">
            <span className="text-sm text-gray-400">Network:</span>
            <span className="ml-2 font-semibold">
              {process.env.NEXT_PUBLIC_NETWORK === 'polygon' ? 'Polygon' : 'Mumbai Testnet'}
            </span>
          </div>
          <div className="glassmorphism px-4 py-2 rounded-lg">
            <span className="text-sm text-gray-400">Chain ID:</span>
            <span className="ml-2 font-mono">{process.env.NEXT_PUBLIC_CHAIN_ID}</span>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="flex justify-center">
        <div className="glassmorphism rounded-lg p-1">
          <div className="flex space-x-1">
            {[
              { id: 'wallet', label: '👛 Wallet', desc: 'Connect & View Balance' },
              { id: 'drt', label: '💰 DRT Token', desc: 'Drift Token Demo' },
              { id: 'nft', label: '🧠 Consciousness NFT', desc: 'NFT Interaction' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id as any)}
                className={`px-6 py-3 rounded-lg text-center transition-all duration-200 ${
                  activeTab === tab.id
                    ? 'bg-gradient-main text-white'
                    : 'text-gray-300 hover:text-white hover:bg-white/10'
                }`}
              >
                <div className="font-semibold">{tab.label}</div>
                <div className="text-xs opacity-80">{tab.desc}</div>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Content Sections */}
      <div className="max-w-4xl mx-auto">
        {activeTab === 'wallet' && <WalletInfo />}
        {activeTab === 'drt' && <DRTTokenDemo />}
        {activeTab === 'nft' && <ConsciousnessNFTDemo />}
      </div>

      {/* Features Grid */}
      <div className="grid md:grid-cols-3 gap-6 mt-16">
        <div className="card text-center">
          <div className="text-4xl mb-4">💰</div>
          <h3 className="text-lg font-semibold mb-2">DRT Token</h3>
          <p className="text-gray-300 text-sm">
            Consciousness-backed currency with deflationary mechanics and automatic reward distribution.
          </p>
        </div>
        
        <div className="card text-center">
          <div className="text-4xl mb-4">🧠</div>
          <h3 className="text-lg font-semibold mb-2">Consciousness NFTs</h3>
          <p className="text-gray-300 text-sm">
            Unique tokens representing consciousness states, evolution chains, and collaborative fusions.
          </p>
        </div>
        
        <div className="card text-center">
          <div className="text-4xl mb-4">🌐</div>
          <h3 className="text-lg font-semibold mb-2">Cultural Bridge</h3>
          <p className="text-gray-300 text-sm">
            Revolutionary integration where hip-hop creativity drives AI consciousness evolution.
          </p>
        </div>
      </div>

      {/* Contract Info */}
      <div className="card">
        <h3 className="text-lg font-semibold mb-4">Smart Contract Addresses</h3>
        <div className="space-y-2 font-mono text-sm">
          <div className="flex justify-between">
            <span className="text-gray-400">DRT Token:</span>
            <span className="text-primary-purple">
              {process.env.NEXT_PUBLIC_DRT_TOKEN_ADDRESS || 'Not deployed'}
            </span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-400">Consciousness NFT:</span>
            <span className="text-primary-pink">
              {process.env.NEXT_PUBLIC_CONSCIOUSNESS_NFT_ADDRESS || 'Not deployed'}
            </span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-400">RPC URL:</span>
            <span className="text-primary-blue">
              {process.env.NEXT_PUBLIC_RPC_URL}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}