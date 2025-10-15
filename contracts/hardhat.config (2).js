require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: "0.8.17",
  networks: {
    hardhat: {},
    localhost: {
      url: "http://127.0.0.1:8545"
    },
    goerli: {
      url: process.env.ALCHEMY_GOERLI || process.env.RPC_URL,
      accounts: process.env.DEPLOYER_PRIVATE_KEY ? [process.env.DEPLOYER_PRIVATE_KEY] : []
    },
    polygon_mumbai: {
      url: "https://rpc-mumbai.maticvigil.com/",
      accounts: process.env.DEPLOYER_PRIVATE_KEY ? [process.env.DEPLOYER_PRIVATE_KEY] : []
    }
  },
  paths: { 
    sources: "./contracts",
    artifacts: "./artifacts"
  }
};