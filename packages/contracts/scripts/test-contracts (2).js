const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  const network = hre.network.name;
  
  console.log("🧪 Testing Hip-Hop Universe Smart Contracts");
  console.log("Network:", network);
  console.log("Deployer:", deployer.address);
  console.log("");
  
  // Get deployed contract addresses (update these after deployment)
  const DRT_ADDRESS = process.env.DRT_ADDRESS || "0x..."; // Update after deploy
  const NFT_ADDRESS = process.env.NFT_ADDRESS || "0x..."; // Update after deploy
  
  if (DRT_ADDRESS === "0x..." || NFT_ADDRESS === "0x...") {
    console.log("❌ Please set DRT_ADDRESS and NFT_ADDRESS environment variables");
    console.log("or update the addresses in this script after deployment");
    return;
  }
  
  // Connect to deployed contracts
  const DRTToken = await hre.ethers.getContractFactory("DRTToken");
  const drtToken = DRTToken.attach(DRT_ADDRESS);
  
  const ConsciousnessNFT = await hre.ethers.getContractFactory("ConsciousnessNFT");
  const consciousnessNFT = ConsciousnessNFT.attach(NFT_ADDRESS);
  
  console.log("📋 Contract Information:");
  console.log("DRT Token:", await drtToken.name(), "(" + await drtToken.symbol() + ")");
  console.log("DRT Balance:", hre.ethers.utils.formatEther(await drtToken.balanceOf(deployer.address)));
  console.log("NFT Name:", await consciousnessNFT.name(), "(" + await consciousnessNFT.symbol() + ")");
  console.log("");
  
  // Test DRT Token features
  console.log("💰 Testing DRT Token Features...");
  
  try {
    // Get transfer amount after fees
    const testAmount = hre.ethers.utils.parseEther("100");
    const transferAmount = await drtToken.getTransferAmount(testAmount);
    console.log("✅ Fee calculation:", 
      hre.ethers.utils.formatEther(testAmount), "DRT →", 
      hre.ethers.utils.formatEther(transferAmount), "DRT after fees"
    );
    
    // Check fee structure
    const transactionFee = await drtToken.transactionFee();
    const burnRate = await drtToken.burnRate();
    const treasuryRate = await drtToken.treasuryRate();
    console.log("✅ Fee structure:", 
      `${transactionFee/100}% total (${burnRate/100}% burn, ${treasuryRate/100}% treasury)`
    );
    
  } catch (error) {
    console.log("❌ DRT Token test failed:", error.message);
  }
  
  console.log("");
  
  // Test Consciousness NFT features
  console.log("🧠 Testing Consciousness NFT Features...");
  
  try {
    // Test minting a consciousness state
    console.log("🎯 Minting test consciousness state...");
    
    const testURI = "ipfs://QmTestConsciousness123";
    const tx = await consciousnessNFT.mintConsciousnessState(
      deployer.address,
      testURI,
      0, // CORE_STATE
      2, // RARE
      85, // energy level
      70, // intuition score
      90, // cultural relevance
      "CoreSelph-v1.0"
    );
    
    const receipt = await tx.wait();
    const tokenId = receipt.events?.find(e => e.event === 'ConsciousnessMinted')?.args?.tokenId;
    
    if (tokenId) {
      console.log("✅ Consciousness NFT minted! Token ID:", tokenId.toString());
      
      // Get consciousness data
      const consciousnessData = await consciousnessNFT.consciousnessData(tokenId);
      console.log("✅ Consciousness metadata:");
      console.log("   - Type:", consciousnessData.consciousnessType.toString());
      console.log("   - Rarity:", consciousnessData.rarity.toString());
      console.log("   - Energy Level:", consciousnessData.energyLevel.toString());
      console.log("   - Dimension:", consciousnessData.dimensionSignature);
      
      // Test evolution creation
      console.log("🧬 Creating evolution...");
      const evolutionTx = await consciousnessNFT.createEvolution(
        tokenId,
        deployer.address,
        "ipfs://QmEvolution123",
        90, // Higher energy
        80, // Higher intuition
        95  // Higher cultural relevance
      );
      
      const evolutionReceipt = await evolutionTx.wait();
      const evolutionTokenId = evolutionReceipt.events?.find(e => e.event === 'EvolutionChainCreated')?.args?.newTokenId;
      
      if (evolutionTokenId) {
        console.log("✅ Evolution created! Token ID:", evolutionTokenId.toString());
        
        // Test compatibility scoring
        const compatibility = await consciousnessNFT.getCompatibilityScore(tokenId, evolutionTokenId);
        console.log("✅ Compatibility score:", compatibility.toString() + "%");
      }
    }
    
  } catch (error) {
    console.log("❌ NFT test failed:", error.message);
    console.log("Note: Make sure the deployer is set as a consciousness minter");
  }
  
  console.log("");
  console.log("🎉 Testing completed!");
  console.log("");
  console.log("🔗 Next Steps:");
  console.log("1. Update frontend environment variables with contract addresses");
  console.log("2. Add liquidity to DRT token if needed");
  console.log("3. Set up consciousness oracles for automated minting");
  console.log("4. Configure IPFS metadata storage");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Testing failed:", error);
    process.exit(1);
  });