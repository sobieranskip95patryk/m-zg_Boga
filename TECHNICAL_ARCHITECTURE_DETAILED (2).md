# 🏗️ Hip-Hop Universe - Szczegółowa Architektura Techniczna

## 📊 Model Biznesowy i Monetyzacja

### Scenariusze Przychodów (Miesięczne)

#### 🔸 Scenariusz A - Konserwatywny (MVP)
- **MAU**: 5,000 użytkowników
- **Conversion**: 1% (50 płacących użytkowników)
- **ARPPU**: $10/miesiąc
- **Przychód subskrypcji**: $500/miesiąc
- **GMV marketplace**: $5,000/miesiąc (prowizja 5% = $250)
- **Całkowity przychód**: $750/miesiąc
- **Koszty**: $7,500/miesiąc
- **Wynik**: -$6,750/miesiąc (strata $81,000/rok)

#### 🔸 Scenariusz B - Umiarkowany (Skalowanie)
- **MAU**: 50,000 użytkowników
- **Conversion**: 3% (1,500 płacących użytkowników)
- **ARPPU**: $8/miesiąc
- **Przychód subskrypcji**: $12,000/miesiąc
- **GMV marketplace**: $100,000/miesiąc (prowizja 5% = $5,000)
- **NFT/featured**: $10,000/miesiąc
- **Całkowity przychód**: $27,000/miesiąc
- **Koszty**: $20,000/miesiąc
- **Wynik**: +$7,000/miesiąc (zysk $84,000/rok)

#### 🔸 Scenariusz C - Optymistyczny (Wzrost)
- **MAU**: 200,000 użytkowników
- **Conversion**: 5% (10,000 płacących użytkowników)
- **ARPPU**: $12/miesiąc
- **Przychód subskrypcji**: $120,000/miesiąc
- **GMV marketplace**: $800,000/miesiąc (prowizja 5% = $40,000)
- **Sponsorships/premium**: $50,000/miesiąc
- **Całkowity przychód**: $210,000/miesiąc
- **Koszty**: $60,000/miesiąc
- **Wynik**: +$150,000/miesiąc (zysk $1,800,000/rok)

---

## 🛠️ Stos Technologiczny

### Frontend
- **Framework**: Next.js 14 + React 18
- **Styling**: Tailwind CSS + Framer Motion
- **State Management**: Zustand + React Query
- **UI Components**: Radix UI + Custom Design System
- **Web3**: ethers.js + web3modal + RainbowKit

### Backend
- **API**: Node.js + Express + GraphQL
- **Database**: PostgreSQL (relacyjne) + Redis (cache)
- **Authentication**: Auth0 + Web3 wallets (MetaMask/WalletConnect)
- **File Storage**: IPFS (Pinata) + AWS S3
- **CDN**: Cloudflare

### Blockchain
- **Network**: Polygon (Ethereum L2)
- **Smart Contracts**: Solidity + Hardhat
- **Tokens**: 
  - ERC-20 (DRT Token)
  - ERC-721/1155 (Consciousness NFTs)
- **Development**: Hardhat + OpenZeppelin

### AI/ML
- **Recommendations**: GPT-4 API (prototyp)
- **Style Analysis**: TensorFlow.js
- **Content Moderation**: AWS Rekognition
- **Custom Models**: Python + scikit-learn

### DevOps & Monitoring
- **CI/CD**: GitHub Actions
- **Hosting**: Vercel (frontend) + AWS/DigitalOcean (backend)
- **Monitoring**: Sentry + Prometheus/Grafana
- **Analytics**: LogRocket + Custom event tracking

---

## 📋 Modele Danych (PostgreSQL)

### Core Tables
```sql
-- Użytkownicy
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    display_name VARCHAR(100),
    wallet_address VARCHAR(42),
    bio TEXT,
    avatar_uri VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Profile artystów
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    stage_name VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    social_links JSONB,
    verified BOOLEAN DEFAULT FALSE,
    metadata_uri VARCHAR(500),
    consciousness_profile_id INTEGER
);

-- Utwory/Beaty
CREATE TABLE tracks (
    id SERIAL PRIMARY KEY,
    artist_id INTEGER REFERENCES artists(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    ipfs_uri VARCHAR(500) NOT NULL,
    preview_uri VARCHAR(500),
    price_drt DECIMAL(18,8),
    price_usd DECIMAL(10,2),
    license_type VARCHAR(50),
    is_nft BOOLEAN DEFAULT FALSE,
    token_id INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

-- NFT
CREATE TABLE nfts (
    id SERIAL PRIMARY KEY,
    token_id INTEGER NOT NULL,
    contract_address VARCHAR(42) NOT NULL,
    owner_address VARCHAR(42) NOT NULL,
    creator_address VARCHAR(42) NOT NULL,
    metadata_uri VARCHAR(500),
    consciousness_data JSONB,
    minted_at TIMESTAMP DEFAULT NOW(),
    last_transfer_at TIMESTAMP
);

-- Transakcje
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    tx_hash VARCHAR(66),
    type VARCHAR(50), -- 'purchase', 'mint', 'transfer', 'royalty'
    amount_drt DECIMAL(18,8),
    amount_usd DECIMAL(10,2),
    status VARCHAR(20), -- 'pending', 'completed', 'failed'
    created_at TIMESTAMP DEFAULT NOW()
);

-- Profile świadomości
CREATE TABLE consciousness_profiles (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id),
    vector_data JSONB, -- Zaszyfrowane wektory cech
    stage VARCHAR(50),
    evolution_history JSONB,
    metadata_uri VARCHAR(500),
    is_tokenized BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔗 API Endpoints

### Authentication
```
POST /api/auth/login           # Magic link login
POST /api/auth/connect-wallet  # Link Web3 wallet
POST /api/auth/logout          # Logout user
GET  /api/auth/session         # Get current session
```

### Users & Artists
```
GET    /api/users/profile      # Get user profile
PUT    /api/users/profile      # Update profile
GET    /api/artists            # List artists (with filters)
GET    /api/artists/:id        # Get artist details
POST   /api/artists            # Create artist profile
PUT    /api/artists/:id        # Update artist profile
```

### Content & Marketplace
```
GET    /api/tracks             # List tracks/beats
POST   /api/tracks             # Upload new track
GET    /api/tracks/:id         # Get track details
PUT    /api/tracks/:id         # Update track
DELETE /api/tracks/:id         # Delete track

POST   /api/marketplace/list   # List item for sale
POST   /api/marketplace/buy    # Purchase item
GET    /api/marketplace/orders # Get user orders
```

### NFT & Consciousness
```
POST   /api/nft/mint           # Mint consciousness NFT
GET    /api/nft/:id            # Get NFT metadata
POST   /api/consciousness      # Create/update consciousness profile
GET    /api/consciousness/:id  # Get consciousness data
```

### AI & Recommendations
```
POST   /api/ai/recommend       # Get recommendations
POST   /api/ai/analyze         # Analyze consciousness compatibility
GET    /api/ai/trends          # Get trending analysis
```

---

## 🔐 Smart Contracts

### DRTToken.sol (ERC-20)
```solidity
contract DRTToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18;
    
    mapping(address => bool) public minters;
    
    function mint(address to, uint256 amount) external onlyMinter {
        require(totalSupply() + amount <= MAX_SUPPLY, "Max supply exceeded");
        _mint(to, amount);
    }
    
    function addMinter(address minter) external onlyOwner {
        minters[minter] = true;
    }
}
```

### ConsciousnessNFT.sol (ERC-721)
```solidity
contract ConsciousnessNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
    struct ConsciousnessData {
        string metadataURI;
        uint256 evolutionStage;
        bytes32 vectorHash;
        uint256 createdAt;
    }
    
    mapping(uint256 => ConsciousnessData) public consciousnessData;
    
    function mintConsciousness(
        address to,
        string memory metadataURI,
        bytes32 vectorHash
    ) external onlyOwner returns (uint256) {
        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();
        
        _mint(to, tokenId);
        
        consciousnessData[tokenId] = ConsciousnessData({
            metadataURI: metadataURI,
            evolutionStage: 1,
            vectorHash: vectorHash,
            createdAt: block.timestamp
        });
        
        return tokenId;
    }
}
```

### Marketplace.sol
```solidity
contract HHUMarketplace is ReentrancyGuard, Ownable {
    IERC20 public drtToken;
    uint256 public platformFee = 250; // 2.5%
    
    struct Listing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool active;
    }
    
    mapping(bytes32 => Listing) public listings;
    
    function createListing(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        require(price > 0, "Price must be greater than 0");
        
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "Not token owner");
        require(nft.isApprovedForAll(msg.sender, address(this)), "Not approved");
        
        bytes32 listingId = keccak256(abi.encodePacked(nftContract, tokenId, block.timestamp));
        
        listings[listingId] = Listing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            active: true
        });
        
        emit ListingCreated(listingId, msg.sender, nftContract, tokenId, price);
    }
    
    function buyItem(bytes32 listingId) external nonReentrant {
        Listing storage listing = listings[listingId];
        require(listing.active, "Listing not active");
        
        uint256 platformCut = (listing.price * platformFee) / 10000;
        uint256 sellerAmount = listing.price - platformCut;
        
        drtToken.transferFrom(msg.sender, listing.seller, sellerAmount);
        drtToken.transferFrom(msg.sender, owner(), platformCut);
        
        IERC721(listing.nftContract).safeTransferFrom(
            listing.seller,
            msg.sender,
            listing.tokenId
        );
        
        listing.active = false;
        
        emit ItemSold(listingId, msg.sender, listing.seller, listing.price);
    }
}
```

---

## 🎯 User Journey Flows

### 1. Onboarding (Bez portfela)
```
1. Rejestracja email + magic link
2. Uzupełnienie profilu (alias, bio, avatar)
3. Wybór typu: Artist / Fan / Investor
4. Opcjonalne: połączenie portfela Web3
5. Claim free DRT tokens (airdrop)
6. Przewodnik po platformie
```

### 2. Onboarding (Z portfelem)
```
1. Połączenie portfela (MetaMask/WalletConnect)
2. Weryfikacja adresu
3. Mint profilu NFT lub claim tokenów
4. Dostęp do funkcji crypto
5. Automatic consciousness profile creation
```

### 3. Marketplace Flow (Kupno)
```
1. Browse beats/NFTs
2. Kliknij "Buy Now"
3. Wybór płatności: DRT / USD (Stripe)
4. Jeśli crypto: MetaMask transaction
5. Jeśli fiat: Stripe checkout
6. Transfer NFT + automatic royalty split
7. Email potwierdzenia + dashboard update
```

### 4. Upload & Mint Flow
```
1. Upload audio file
2. Add metadata (title, description, tags)
3. Choose license type
4. Set price (DRT/USD)
5. Optional: Mint as NFT
6. IPFS storage + metadata JSON
7. List on marketplace
```

---

## 🔄 Background Jobs & Workers

### Audio Processing Worker
```javascript
// Process uploaded audio files
const processAudio = async (fileUrl, trackId) => {
    // 1. Download from S3
    // 2. Generate waveform
    // 3. Create preview (30s)
    // 4. Extract metadata
    // 5. Upload to IPFS
    // 6. Update database
};
```

### Blockchain Event Listener
```javascript
// Listen for smart contract events
const listenToMarketplaceEvents = () => {
    marketplaceContract.on('ItemSold', async (listingId, buyer, seller, price) => {
        await updateDatabase({
            listingId,
            buyer,
            seller,
            price,
            status: 'completed'
        });
        
        await sendNotifications(buyer, seller);
        await updateUserStats(buyer, seller);
    });
};
```

### AI Recommendation Engine
```javascript
// Generate recommendations based on user behavior
const generateRecommendations = async (userId) => {
    const userHistory = await getUserListeningHistory(userId);
    const consciousnessProfile = await getConsciousnessProfile(userId);
    
    const recommendations = await aiModel.predict({
        history: userHistory,
        consciousness: consciousnessProfile,
        trending: await getTrendingTracks()
    });
    
    await cacheRecommendations(userId, recommendations);
};
```

---

## 📊 Analytics & KPIs

### Kluczowe Metryki
```javascript
const kpis = {
    // User Engagement
    MAU: 'Monthly Active Users',
    DAU: 'Daily Active Users',
    sessionDuration: 'Average session time',
    retention: {
        day1: '% users returning after 1 day',
        day7: '% users returning after 7 days',
        day30: '% users returning after 30 days'
    },
    
    // Monetization
    conversionRate: 'Paying users / Total users',
    ARPPU: 'Average Revenue Per Paying User',
    ARPU: 'Average Revenue Per User',
    GMV: 'Gross Merchandise Value',
    takeRate: 'Platform commission %',
    
    // Marketplace
    listingsPerDay: 'New listings created',
    salesConversion: 'Sales / Listings',
    averagePrice: 'Average NFT/track price',
    
    // Consciousness
    profilesCreated: 'New consciousness profiles',
    evolutionEvents: 'Consciousness evolution triggers',
    compatibilityMatches: 'Successful matchmaking'
};
```

### Event Tracking
```javascript
// Track user actions for analytics
const trackEvent = (userId, event, properties) => {
    const eventData = {
        userId,
        event,
        properties,
        timestamp: Date.now(),
        sessionId: getSessionId(),
        platform: 'web' // or 'mobile'
    };
    
    // Send to analytics pipeline
    analyticsQueue.add('track-event', eventData);
};

// Example events
trackEvent(userId, 'track_played', { trackId, duration, source: 'discovery' });
trackEvent(userId, 'nft_purchased', { tokenId, price, paymentMethod: 'DRT' });
trackEvent(userId, 'consciousness_evolved', { profileId, newStage, trigger: 'creation' });
```

---

## 🛡️ Bezpieczeństwo

### Smart Contract Security
- **Audyty**: Minimum 1 niezależny audyt przed mainnet
- **Reentrancy Protection**: OpenZeppelin ReentrancyGuard
- **Access Control**: Proper ownership patterns
- **Pausability**: Emergency stop mechanism
- **Upgrade Patterns**: Proxy contracts for critical components

### Backend Security
- **Rate Limiting**: API throttling + DDoS protection
- **Input Validation**: Wszystkie endpoints walidowane
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Content Security Policy
- **HTTPS**: TLS wszędzie
- **Secret Management**: AWS KMS + rotacja kluczy

### Privacy
- **Data Encryption**: Sensitive data encrypted at rest
- **Consciousness Data**: End-to-end encryption
- **GDPR Compliance**: Right to deletion, data portability
- **Consent Management**: Explicit consent for AI features

---

## 🚀 Deployment & Scaling

### Infrastructure
```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
      - IPFS_API_KEY=${IPFS_API_KEY}
    
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: hiphopuniverse
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

### CI/CD Pipeline
```yaml
# .github/workflows/deploy.yml
name: Deploy to Production
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          npm ci
          npm run test
          npm run test:contracts
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
```

---

## 📈 Roadmap Implementacyjny

### Faza 1: MVP (Miesiące 1-3)
- ✅ Podstawowe profile użytkowników
- ✅ Upload i streaming beats
- ✅ Prosty marketplace
- ✅ DRT token (testnet)
- ✅ Stripe integration

### Faza 2: Marketplace & NFT (Miesiące 4-6)
- 🔄 Consciousness NFT system
- 🔄 Advanced marketplace features
- 🔄 Royalty management
- 🔄 IPFS integration
- 🔄 Creator dashboard

### Faza 3: AI & Consciousness (Miesiące 7-9)
- ⏳ GPT-4 recommendations
- ⏳ Consciousness matching
- ⏳ AI curation features
- ⏳ Advanced analytics
- ⏳ Mobile app beta

### Faza 4: Scale & Govern (Miesiące 10-12)
- ⏳ Smart contract audits
- ⏳ Mainnet deployment
- ⏳ DAO governance
- ⏳ Global expansion
- ⏳ Enterprise partnerships

---

## 💰 Cost Breakdown

### Jednorazowe Koszty
- **Smart Contract Audit**: $8,000 - $50,000
- **Legal & Compliance**: $5,000 - $15,000
- **Initial Marketing**: $10,000 - $30,000
- **Design & Branding**: $3,000 - $10,000

### Miesięczne Koszty Operacyjne
- **Development Team**: $12,000 - $30,000
- **Infrastructure**: $500 - $5,000
- **Marketing & Growth**: $2,000 - $20,000
- **Third-party Services**: $500 - $2,000
- **Legal & Compliance**: $1,000 - $3,000

---

## 🎯 Następne Kroki

### Natychmiast (Tydzień 1-2)
1. Finalizacja smart contracts
2. Security audit scheduling
3. Team expansion (Solidity dev)
4. Marketing strategy

### Krótkoterminowo (Miesiąc 1)
1. Beta testing program
2. Artist onboarding
3. Community building
4. Partnership outreach

### Średnioterminowo (Miesiące 2-3)
1. Mainnet deployment
2. Mobile app development
3. Advanced AI features
4. Global expansion

---

*Dokument stworzony: 15 października 2025*
*Ostatnia aktualizacja: 15 października 2025*