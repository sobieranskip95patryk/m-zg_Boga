async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("🚀 Deploying contracts with account:", deployer.address);
  console.log("💰 Account balance:", (await deployer.getBalance()).toString());

  const HipHop = await ethers.getContractFactory("HipHopNFT");
  const hipHop = await HipHop.deploy("HipHop Universe", "HHU");
  await hipHop.deployed();
  
  console.log("✅ HipHopNFT deployed to:", hipHop.address);
  console.log("📋 Contract owner:", await hipHop.owner());
  console.log("🎯 Next token ID:", (await hipHop.nextTokenId()).toString());
  
  // Save deployment info
  const fs = require('fs');
  const deploymentInfo = {
    address: hipHop.address,
    deployer: deployer.address,
    network: hre.network.name,
    timestamp: new Date().toISOString()
  };
  
  fs.writeFileSync('./deployment.json', JSON.stringify(deploymentInfo, null, 2));
  console.log("💾 Deployment info saved to deployment.json");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Deployment failed:", error);
    process.exit(1);
  });