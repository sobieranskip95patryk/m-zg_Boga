const express = require('express');
const router = express.Router();
const { ethers } = require('ethers');
const db = require('../db');

// Mint NFT endpoint - backend acts as relayer
router.post('/', async (req, res) => {
  try {
    const { to, tokenURI, royaltyBps, title, artist } = req.body;
    
    if (!to || !tokenURI) {
      return res.status(400).json({ error: 'Missing required fields: to, tokenURI' });
    }

    console.log('🎯 Minting NFT for:', to);

    // Initialize provider and wallet
    const rpcUrl = process.env.RPC_URL || 'http://localhost:8545';
    const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
    
    if (!process.env.DEPLOYER_PRIVATE_KEY) {
      return res.status(500).json({ error: 'DEPLOYER_PRIVATE_KEY not configured' });
    }
    
    const wallet = new ethers.Wallet(process.env.DEPLOYER_PRIVATE_KEY, provider);
    
    // Load contract ABI (simplified for MVP)
    const contractABI = [
      "function mint(address to, string memory tokenURI, uint256 royaltyBps) external returns (uint256)",
      "function nextTokenId() public view returns (uint256)",
      "event Minted(address indexed to, uint256 tokenId, string uri, uint256 royaltyBPS)"
    ];
    
    const contractAddress = process.env.CONTRACT_ADDRESS;
    if (!contractAddress) {
      return res.status(500).json({ error: 'CONTRACT_ADDRESS not configured' });
    }
    
    const contract = new ethers.Contract(contractAddress, contractABI, wallet);

    // Execute mint transaction
    console.log('📝 Sending mint transaction...');
    const tx = await contract.mint(to, tokenURI, royaltyBps || 500);
    console.log('⏳ Waiting for confirmation...', tx.hash);
    
    const receipt = await tx.wait();
    console.log('✅ Transaction confirmed!');

    // Parse events to get tokenId
    const mintedEvents = receipt.events?.filter(e => e.event === 'Minted') || [];
    const tokenId = mintedEvents[0]?.args?.tokenId?.toString() || null;

    // Store in database
    try {
      await db.query(
        'INSERT INTO nfts(token_id, owner, uri, title, artist, tx_hash) VALUES($1,$2,$3,$4,$5,$6)',
        [tokenId, to, tokenURI, title || 'Untitled', artist || 'Unknown', receipt.transactionHash]
      );
      console.log('💾 NFT stored in database');
    } catch (dbError) {
      console.error('⚠️ Database storage failed:', dbError.message);
      // Continue anyway - blockchain mint succeeded
    }

    res.json({
      success: true,
      txHash: receipt.transactionHash,
      tokenId: tokenId,
      gasUsed: receipt.gasUsed.toString(),
      blockNumber: receipt.blockNumber
    });

  } catch (error) {
    console.error('❌ Mint failed:', error);
    res.status(500).json({ 
      error: error.message,
      code: error.code || 'MINT_FAILED'
    });
  }
});

// Get user's NFTs
router.get('/user/:address', async (req, res) => {
  try {
    const { address } = req.params;
    const result = await db.query(
      'SELECT * FROM nfts WHERE LOWER(owner) = LOWER($1) ORDER BY created_at DESC',
      [address]
    );
    res.json({ nfts: result.rows });
  } catch (error) {
    console.error('❌ Failed to fetch user NFTs:', error);
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;