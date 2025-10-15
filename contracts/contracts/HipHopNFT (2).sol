// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HipHopNFT is ERC721URIStorage, Ownable {
    uint256 public nextTokenId;
    mapping(uint256 => uint256) public royaltiesBPS; // basis points for royalty

    event Minted(address indexed to, uint256 tokenId, string uri, uint256 royaltyBPS);

    constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) {}

    function mint(address to, string memory tokenURI, uint256 royaltyBps) external onlyOwner returns (uint256) {
        uint256 tokenId = ++nextTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        royaltiesBPS[tokenId] = royaltyBps;
        emit Minted(to, tokenId, tokenURI, royaltyBps);
        return tokenId;
    }

    // owner can set tokenURI if needed
    function setTokenURI(uint256 tokenId, string memory _tokenURI) external onlyOwner {
        require(_exists(tokenId), "Nonexistent token");
        _setTokenURI(tokenId, _tokenURI);
    }
}