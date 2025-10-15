// components/profile/ProfileCard.tsx
'use client';

import { useState, useEffect } from 'react';

interface Profile {
  id: string;
  displayName: string;
  alias: string;
  roleTags: string[];
  shortBio: string;
  manifestShort: string;
  avatarUrl: string;
  projects: Array<{
    id: string;
    title: string;
    type: string;
    description: string;
    status: string;
  }>;
  tokens: {
    platformToken: {
      symbol: string;
    };
  };
  stats: {
    respectPoints: number;
    followers: number;
    activeProjects: number;
    tokensMinted: number;
  };
}

export default function ProfileCard() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/profile/patryk')
      .then(res => res.json())
      .then(data => {
        setProfile(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error loading profile:', err);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="flex items-center justify-center p-8">
      <div className="text-gray-400">Ładowanie profilu...</div>
    </div>
  );

  if (!profile) return (
    <div className="flex items-center justify-center p-8">
      <div className="text-red-400">Błąd wczytywania profilu</div>
    </div>
  );

  return (
    <section className="bg-gradient-to-br from-purple-900/20 to-pink-900/20 backdrop-blur-lg border border-white/10 rounded-2xl p-6 max-w-md mx-auto">
      {/* Header */}
      <div className="flex items-center space-x-4 mb-6">
        <img 
          src={profile.avatarUrl} 
          alt={profile.displayName}
          className="w-16 h-16 rounded-full border-2 border-purple-400/50"
          onError={(e) => {
            (e.target as HTMLImageElement).src = '/assets/images/default-avatar.png';
          }}
        />
        <div>
          <h2 className="text-xl font-bold text-white">{profile.displayName}</h2>
          <p className="text-purple-300 text-sm">{profile.alias}</p>
        </div>
      </div>

      {/* Role Tags */}
      <div className="flex flex-wrap gap-2 mb-4">
        {profile.roleTags.map((tag, index) => (
          <span 
            key={index}
            className="px-3 py-1 bg-gradient-to-r from-purple-500/20 to-pink-500/20 text-purple-200 text-xs rounded-full border border-purple-400/30"
          >
            {tag}
          </span>
        ))}
      </div>

      {/* Bio */}
      <p className="text-gray-300 text-sm mb-4 leading-relaxed">{profile.shortBio}</p>

      {/* Manifest */}
      <div className="bg-black/20 rounded-lg p-3 mb-4 border border-purple-400/20">
        <p className="text-purple-200 text-xs italic">&quot;{profile.manifestShort}&quot;</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-2 gap-3 mb-4">
        <div className="text-center">
          <div className="text-lg font-bold text-purple-400">{profile.stats.respectPoints.toLocaleString()}</div>
          <div className="text-xs text-gray-400">Respect Points</div>
        </div>
        <div className="text-center">
          <div className="text-lg font-bold text-pink-400">{profile.stats.followers.toLocaleString()}</div>
          <div className="text-xs text-gray-400">Followers</div>
        </div>
        <div className="text-center">
          <div className="text-lg font-bold text-blue-400">{profile.stats.activeProjects}</div>
          <div className="text-xs text-gray-400">Active Projects</div>
        </div>
        <div className="text-center">
          <div className="text-lg font-bold text-green-400">{profile.stats.tokensMinted}</div>
          <div className="text-xs text-gray-400">Tokens Minted</div>
        </div>
      </div>

      {/* Projects */}
      <div className="mb-4">
        <h3 className="text-sm font-semibold text-white mb-2">Projekty:</h3>
        <div className="text-xs text-gray-300">
          {profile.projects.map(p => p.title).join(' • ')}
        </div>
      </div>

      {/* Token */}
      <div className="flex justify-between items-center text-xs">
        <span className="text-gray-400">Token preferowany:</span>
        <span className="font-bold text-yellow-400">{profile.tokens.platformToken.symbol}</span>
      </div>
    </section>
  );
}