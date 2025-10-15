const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

async function main() {
  console.log("🚀 Deploying Hip-Hop Universe Smart Contracts...");
  
  const [deployer] = await hre.ethers.getSigners();
  const network = hre.network.name;
  
  console.log("📋 Deployment Details:");
  console.log("- Network:", network);
  console.log("- Deployer:", deployer.address);
  console.log("- Balance:", hre.ethers.utils.formatEther(await deployer.getBalance()), "ETH");
  
  // Configuration based on network
  let treasuryAddress, consciousnessPoolAddress;
  
  if (network === "mumbai") {
    treasuryAddress = process.env.TREASURY_ADDRESS_MUMBAI || deployer.address;
    consciousnessPoolAddress = deployer.address; // For testnet, use deployer
  } else if (network === "polygon") {
    treasuryAddress = process.env.TREASURY_ADDRESS_POLYGON || deployer.address;
    consciousnessPoolAddress = deployer.address; // Update for mainnet
  } else {
    treasuryAddress = deployer.address;
    consciousnessPoolAddress = deployer.address;
  }
  
  console.log("- Treasury:", treasuryAddress);
  console.log("- Consciousness Pool:", consciousnessPoolAddress);
  console.log("");
  
  // Deploy DRT Token
  console.log("💰 Deploying DRT Token...");
  const DRTToken = await hre.ethers.getContractFactory("DRTToken");
  const drtToken = await DRTToken.deploy(treasuryAddress, consciousnessPoolAddress);
  await drtToken.deployed();
  
  console.log("✅ DRT Token deployed to:", drtToken.address);
  console.log("- Name:", await drtToken.name());
  console.log("- Symbol:", await drtToken.symbol());
  console.log("- Total Supply:", hre.ethers.utils.formatEther(await drtToken.totalSupply()));
  console.log("");
  
  // Deploy Consciousness NFT
  console.log("🧠 Deploying Consciousness NFT...");
  const ConsciousnessNFT = await hre.ethers.getContractFactory("ConsciousnessNFT");
  const consciousnessNFT = await ConsciousnessNFT.deploy(treasuryAddress);
  await consciousnessNFT.deployed();
  
  console.log("✅ Consciousness NFT deployed to:", consciousnessNFT.address);
  console.log("- Name:", await consciousnessNFT.name());
  console.log("- Symbol:", await consciousnessNFT.symbol());
  console.log("- Royalty Recipient:", await consciousnessNFT.royaltyRecipient());
  console.log("");
  
  // Set up cross-contract permissions
  console.log("⚙️ Setting up permissions...");
  
  // Set consciousness NFT as consciousness oracle for DRT rewards
  await drtToken.setConsciousnessOracle(consciousnessNFT.address, true);
  console.log("✅ Consciousness NFT set as oracle for DRT rewards");
  
  // Set DRT token as consciousness minter (for future integrations)
  await consciousnessNFT.setConsciousnessMinter(drtToken.address, true);
  console.log("✅ DRT Token set as consciousness minter");
  
  console.log("");
  
  // Save deployment addresses
  const deploymentInfo = {
    network: network,
    deployer: deployer.address,
    timestamp: new Date().toISOString(),
    contracts: {
      DRTToken: {
        address: drtToken.address,
        name: await drtToken.name(),
        symbol: await drtToken.symbol(),
        totalSupply: hre.ethers.utils.formatEther(await drtToken.totalSupply()),
        treasury: treasuryAddress,
        consciousnessPool: consciousnessPoolAddress
      },
      ConsciousnessNFT: {
        address: consciousnessNFT.address,
        name: await consciousnessNFT.name(),
        symbol: await consciousnessNFT.symbol(),
        royaltyRecipient: await consciousnessNFT.royaltyRecipient()
      }
    },
    transactions: {
      drtDeploy: drtToken.deployTransaction.hash,
      nftDeploy: consciousnessNFT.deployTransaction.hash
    }
  };
  
  // Save to deployments folder
  const deploymentsDir = path.join(__dirname, "../deployments");
  if (!fs.existsSync(deploymentsDir)) {
    fs.mkdirSync(deploymentsDir, { recursive: true });
  }
  
  const deploymentFile = path.join(deploymentsDir, `${network}-${Date.now()}.json`);
  fs.writeFileSync(deploymentFile, JSON.stringify(deploymentInfo, null, 2));
  
  console.log("📁 Deployment info saved to:", deploymentFile);
  console.log("");
  
  // Environment variables for frontend
  console.log("🌐 Frontend Environment Variables:");
  console.log(`NEXT_PUBLIC_DRT_TOKEN_ADDRESS=${drtToken.address}`);
  console.log(`NEXT_PUBLIC_CONSCIOUSNESS_NFT_ADDRESS=${consciousnessNFT.address}`);
  console.log(`NEXT_PUBLIC_NETWORK=${network}`);
  
  if (network === "mumbai") {
    console.log(`NEXT_PUBLIC_RPC_URL=https://rpc-mumbai.maticvigil.com`);
    console.log(`NEXT_PUBLIC_CHAIN_ID=80001`);
  } else if (network === "polygon") {
    console.log(`NEXT_PUBLIC_RPC_URL=https://polygon-rpc.com`);
    console.log(`NEXT_PUBLIC_CHAIN_ID=137`);
  }
  
  console.log("");
  console.log("🎉 Deployment completed successfully!");
  
  // Verification instructions
  if (network !== "hardhat" && network !== "localhost") {
    console.log("");
    console.log("📝 To verify contracts on Polygonscan:");
    console.log(`npx hardhat verify --network ${network} ${drtToken.address} "${treasuryAddress}" "${consciousnessPoolAddress}"`);
    console.log(`npx hardhat verify --network ${network} ${consciousnessNFT.address} "${treasuryAddress}"`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });