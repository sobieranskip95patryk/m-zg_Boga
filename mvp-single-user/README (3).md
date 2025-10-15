# Hip-Hop Universe — MVP (single user)

## Uruchomienie lokalne
1. `npm install`
2. `npm run dev`
3. Otwórz `http://localhost:3000`

## Co robi:
- profil użytkownika (seed w `data/profiles/...`)
- symulowane saldo DRT (`data/state.json`)
- mint NFT zapisuje dane do `data/nfts.json`
- prosty "AI manifest" mock w `/api/ai/manifest`

## Uwaga
To prototype local only. Do produkcji: podmiana na DB, prawdziwe smart contracty, audyt, integracja z wallets i Stripe.

## Struktura:
```
mvp-single-user/
├─ package.json          # Next.js dependencies
├─ pages/index.tsx       # Main dashboard
├─ components/           # ProfileCard, Dashboard
├─ pages/api/            # REST endpoints
├─ data/                 # JSON file storage
└─ styles/globals.css    # Simple styling
```

## Test scenariusze:
1. Top-up DRT balance
2. Mint NFT (cost DRT)
3. Generate AI manifest
4. View profile & NFT collection

**Ready to test!** 🚀