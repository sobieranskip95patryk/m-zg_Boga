-- Hip-Hop Universe Database Schema
-- PostgreSQL initialization script

-- Users table for wallet addresses and profiles
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  wallet_address VARCHAR(42) UNIQUE NOT NULL,
  username VARCHAR(50),
  email VARCHAR(255),
  bio TEXT,
  avatar_url TEXT,
  social_links JSONB,
  is_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- NFTs table for minted tokens
CREATE TABLE IF NOT EXISTS nfts (
  id SERIAL PRIMARY KEY,
  token_id VARCHAR(255) NOT NULL,
  contract_address VARCHAR(42),
  owner VARCHAR(42) NOT NULL,
  uri TEXT NOT NULL,
  title VARCHAR(255),
  artist VARCHAR(255),
  description TEXT,
  metadata JSONB,
  tx_hash VARCHAR(66),
  block_number BIGINT,
  royalty_bps INTEGER DEFAULT 500,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tracks table for music metadata
CREATE TABLE IF NOT EXISTS tracks (
  id SERIAL PRIMARY KEY,
  nft_id INTEGER REFERENCES nfts(id),
  title VARCHAR(255) NOT NULL,
  artist VARCHAR(255) NOT NULL,
  genre VARCHAR(100),
  mood VARCHAR(100),
  duration INTEGER, -- in seconds
  bpm INTEGER,
  key_signature VARCHAR(10),
  audio_url TEXT,
  waveform_data JSONB,
  lyrics TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Collections table for grouping NFTs
CREATE TABLE IF NOT EXISTS collections (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  creator VARCHAR(42) NOT NULL,
  image_url TEXT,
  banner_url TEXT,
  total_supply INTEGER DEFAULT 0,
  floor_price DECIMAL(20,8),
  volume_traded DECIMAL(20,8) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI generations table for tracking AI-created content
CREATE TABLE IF NOT EXISTS ai_generations (
  id SERIAL PRIMARY KEY,
  user_address VARCHAR(42),
  type VARCHAR(50) NOT NULL, -- 'metadata', 'artwork', 'lyrics'
  prompt TEXT NOT NULL,
  result JSONB NOT NULL,
  model_used VARCHAR(100),
  tokens_used INTEGER,
  cost_cents INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Marketplace listings (future feature)
CREATE TABLE IF NOT EXISTS listings (
  id SERIAL PRIMARY KEY,
  nft_id INTEGER REFERENCES nfts(id),
  seller VARCHAR(42) NOT NULL,
  price DECIMAL(20,8) NOT NULL,
  currency VARCHAR(10) DEFAULT 'ETH',
  expires_at TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_nfts_owner ON nfts(owner);
CREATE INDEX IF NOT EXISTS idx_nfts_token_id ON nfts(token_id);
CREATE INDEX IF NOT EXISTS idx_users_wallet ON users(wallet_address);
CREATE INDEX IF NOT EXISTS idx_tracks_artist ON tracks(artist);
CREATE INDEX IF NOT EXISTS idx_tracks_genre ON tracks(genre);
CREATE INDEX IF NOT EXISTS idx_listings_active ON listings(is_active) WHERE is_active = TRUE;

-- Insert sample data for testing
INSERT INTO users (wallet_address, username, bio, is_verified) 
VALUES 
  ('0x742d35Cc6b1BC8A9D1F5c6a8D9E9F0E1F2F3F4F5', 'MetaGeniusz', 'Hip-Hop Universe creator and visionary', TRUE),
  ('0x123456789012345678901234567890123456789a', 'TestArtist', 'Test artist for development', FALSE)
ON CONFLICT (wallet_address) DO NOTHING;

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for automatic updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    
CREATE TRIGGER update_nfts_updated_at BEFORE UPDATE ON nfts 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    
CREATE TRIGGER update_tracks_updated_at BEFORE UPDATE ON tracks 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    
CREATE TRIGGER update_collections_updated_at BEFORE UPDATE ON collections 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
    
CREATE TRIGGER update_listings_updated_at BEFORE UPDATE ON listings 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();