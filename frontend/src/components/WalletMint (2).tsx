import React, { useState } from 'react';
import { useAccount, useWalletClient, usePublicClient } from 'wagmi';
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { ethers } from 'ethers';
import toast from 'react-hot-toast';
import { Music, Upload, Loader2, CheckCircle } from 'lucide-react';

interface MintFormData {
  title: string;
  artist: string;
  mood: string;
  genre: string;
  description: string;
}

export default function WalletMint() {
  const { address, isConnected } = useAccount();
  const { data: walletClient } = useWalletClient();
  const publicClient = usePublicClient();
  
  const [formData, setFormData] = useState<MintFormData>({
    title: '',
    artist: '',
    mood: 'energetic',
    genre: 'hip-hop',
    description: ''
  });
  
  const [isGenerating, setIsGenerating] = useState(false);
  const [isMinting, setIsMinting] = useState(false);
  const [generatedMetadata, setGeneratedMetadata] = useState(null);
  const [mintResult, setMintResult] = useState(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const generateMetadata = async () => {
    if (!formData.title || !formData.artist) {
      toast.error('Tytuł i artysta są wymagane');
      return;
    }

    setIsGenerating(true);
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL || 'http://localhost:4000'}/api/ai/generate-metadata`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('Nie udało się wygenerować metadanych');
      }

      const result = await response.json();
      setGeneratedMetadata(result.metadata);
      toast.success('🤖 Metadata wygenerowane przez AI!');
    } catch (error) {
      console.error('Błąd generowania metadata:', error);
      toast.error('Błąd podczas generowania metadanych');
    } finally {
      setIsGenerating(false);
    }
  };

  const mintNFT = async () => {
    if (!isConnected || !address) {
      toast.error('Połącz portfel, aby mintować NFT');
      return;
    }

    if (!generatedMetadata) {
      toast.error('Najpierw wygeneruj metadata');
      return;
    }

    setIsMinting(true);
    try {
      // Call backend to mint NFT
      const response = await fetch(`${process.env.REACT_APP_API_URL || 'http://localhost:4000'}/api/mint`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          to: address,
          tokenURI: JSON.stringify(generatedMetadata),
          royaltyBps: 500, // 5% royalty
          title: formData.title,
          artist: formData.artist
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Mint nie powiódł się');
      }

      const result = await response.json();
      setMintResult(result);
      toast.success(`🎉 NFT zmintowane! Token ID: ${result.tokenId}`);
      
      // Reset form
      setFormData({
        title: '',
        artist: '',
        mood: 'energetic',
        genre: 'hip-hop',
        description: ''
      });
      setGeneratedMetadata(null);
      
    } catch (error) {
      console.error('Błąd mintowania:', error);
      toast.error(`Błąd mintowania: ${error.message}`);
    } finally {
      setIsMinting(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent mb-2">
          🎵 Hip-Hop Universe NFT Mint
        </h1>
        <p className="text-gray-600">Stwórz swój unikalny NFT z AI-wygenerowanymi metadanymi</p>
      </div>

      {/* Wallet Connection */}
      <div className="flex justify-center">
        <ConnectButton />
      </div>

      {isConnected && (
        <div className="bg-white rounded-lg shadow-lg p-6 space-y-4">
          <h2 className="text-xl font-semibold flex items-center gap-2">
            <Music className="w-5 h-5" />
            Dane utworu
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Tytuł utworu *
              </label>
              <input
                type="text"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="Wpisz tytuł utworu"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Artysta *
              </label>
              <input
                type="text"
                name="artist"
                value={formData.artist}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                placeholder="Nazwa artysty"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Nastrój
              </label>
              <select
                name="mood"
                value={formData.mood}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="energetic">Energiczny</option>
                <option value="chill">Spokojny</option>
                <option value="aggressive">Agresywny</option>
                <option value="melancholic">Melancholijny</option>
                <option value="uplifting">Podnoszący na duchu</option>
                <option value="dark">Mroczny</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Gatunek
              </label>
              <select
                name="genre"
                value={formData.genre}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="hip-hop">Hip-Hop</option>
                <option value="trap">Trap</option>
                <option value="drill">Drill</option>
                <option value="conscious-rap">Conscious Rap</option>
                <option value="old-school">Old School</option>
                <option value="experimental">Experimental</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Dodatkowy opis (opcjonalnie)
            </label>
            <textarea
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              placeholder="Dodatkowe informacje o utworze..."
            />
          </div>

          {/* Generate Metadata Button */}
          <button
            onClick={generateMetadata}
            disabled={isGenerating || !formData.title || !formData.artist}
            className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 px-4 rounded-md font-medium disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            {isGenerating ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                Generowanie AI...
              </>
            ) : (
              <>
                🤖 Wygeneruj metadata AI
              </>
            )}
          </button>

          {/* Generated Metadata Preview */}
          {generatedMetadata && (
            <div className="bg-gray-50 rounded-lg p-4">
              <h3 className="font-semibold text-green-700 flex items-center gap-2 mb-2">
                <CheckCircle className="w-4 h-4" />
                Wygenerowane metadata:
              </h3>
              <pre className="text-sm text-gray-700 overflow-x-auto">
                {JSON.stringify(generatedMetadata, null, 2)}
              </pre>
            </div>
          )}

          {/* Mint Button */}
          {generatedMetadata && (
            <button
              onClick={mintNFT}
              disabled={isMinting}
              className="w-full bg-gradient-to-r from-green-600 to-emerald-600 text-white py-3 px-4 rounded-md font-medium disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              {isMinting ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  Mintowanie...
                </>
              ) : (
                <>
                  <Upload className="w-4 h-4" />
                  Mintuj NFT
                </>
              )}
            </button>
          )}

          {/* Mint Result */}
          {mintResult && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <h3 className="font-semibold text-green-800 mb-2">✅ NFT został pomyślnie zmintowany!</h3>
              <div className="text-sm text-green-700">
                <p><strong>Token ID:</strong> {mintResult.tokenId}</p>
                <p><strong>Transaction Hash:</strong> 
                  <a 
                    href={`https://etherscan.io/tx/${mintResult.txHash}`} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-blue-600 hover:underline ml-1"
                  >
                    {mintResult.txHash}
                  </a>
                </p>
                <p><strong>Gas Used:</strong> {mintResult.gasUsed}</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}