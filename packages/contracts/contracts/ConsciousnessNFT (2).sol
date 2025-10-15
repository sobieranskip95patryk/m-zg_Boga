// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ConsciousnessNFT
 * @dev NFT representing consciousness states and evolution chains in Hip-Hop Universe
 * Features:
 * - Evolution chain tracking
 * - Consciousness metadata on-chain
 * - Rarity scoring system
 * - Collaboration tokens (multi-consciousness)
 * - Royalty enforcement
 */
contract ConsciousnessNFT is 
    ERC721, 
    ERC721Enumerable, 
    ERC721URIStorage, 
    ERC721Burnable, 
    Ownable, 
    Pausable, 
    ReentrancyGuard 
{
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter;
    
    // Consciousness Types
    enum ConsciousnessType {
        CORE_STATE,
        EVOLUTION_SNAPSHOT,
        COLLABORATION_FUSION,
        CULTURAL_MOMENT,
        ARTISTIC_FLOW,
        COMMUNITY_RESONANCE
    }
    
    // Rarity Levels
    enum RarityLevel {
        COMMON,
        UNCOMMON,
        RARE,
        EPIC,
        LEGENDARY,
        MYTHIC
    }
    
    // Consciousness Metadata Structure
    struct ConsciousnessMetadata {
        ConsciousnessType consciousnessType;
        RarityLevel rarity;
        uint256 energyLevel;        // 0-100
        uint256 intuitionScore;     // 0-100
        uint256 culturalRelevance;  // 0-100
        uint256 evolutionStage;     // Version number
        string dimensionSignature;  // CoreSelph, SelphOS, etc.
        address[] collaborators;    // For multi-consciousness tokens
        uint256 parentTokenId;      // For evolution chains (0 if genesis)
        uint256 timestamp;
        bool isCollaborative;
    }
    
    // Events
    event ConsciousnessMinted(
        uint256 indexed tokenId,
        address indexed recipient,
        ConsciousnessType consciousnessType,
        RarityLevel rarity,
        uint256 energyLevel
    );
    
    event EvolutionChainCreated(
        uint256 indexed newTokenId,
        uint256 indexed parentTokenId,
        address indexed owner
    );
    
    event CollaborationMinted(
        uint256 indexed tokenId,
        address[] collaborators,
        string fusionType
    );
    
    // Mappings
    mapping(uint256 => ConsciousnessMetadata) public consciousnessData;
    mapping(address => bool) public consciousnessMinters;
    mapping(uint256 => uint256[]) public evolutionChains; // parentId => childIds[]
    mapping(string => uint256) public dimensionCounts;    // Track dimensions
    
    // Royalty info (EIP-2981)
    uint256 public royaltyPercentage = 250; // 2.5%
    address public royaltyRecipient;
    
    constructor(address _royaltyRecipient) ERC721("ConsciousnessNFT", "CNSC") {
        royaltyRecipient = _royaltyRecipient;
        consciousnessMinters[msg.sender] = true;
    }
    
    /**
     * @dev Mint a new consciousness state NFT
     */
    function mintConsciousnessState(
        address to,
        string calldata uri,
        ConsciousnessType consciousnessType,
        RarityLevel rarity,
        uint256 energyLevel,
        uint256 intuitionScore,
        uint256 culturalRelevance,
        string calldata dimensionSignature
    ) external nonReentrant returns (uint256) {
        require(consciousnessMinters[msg.sender], "Not authorized to mint consciousness NFTs");
        require(to != address(0), "Cannot mint to zero address");
        require(energyLevel <= 100, "Energy level must be 0-100");
        require(intuitionScore <= 100, "Intuition score must be 0-100");
        require(culturalRelevance <= 100, "Cultural relevance must be 0-100");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
        
        // Create consciousness metadata
        ConsciousnessMetadata memory metadata = ConsciousnessMetadata({
            consciousnessType: consciousnessType,
            rarity: rarity,
            energyLevel: energyLevel,
            intuitionScore: intuitionScore,
            culturalRelevance: culturalRelevance,
            evolutionStage: 1,
            dimensionSignature: dimensionSignature,
            collaborators: new address[](0),
            parentTokenId: 0,
            timestamp: block.timestamp,
            isCollaborative: false
        });
        
        consciousnessData[tokenId] = metadata;
        dimensionCounts[dimensionSignature]++;
        
        emit ConsciousnessMinted(tokenId, to, consciousnessType, rarity, energyLevel);
        
        return tokenId;
    }
    
    /**
     * @dev Create evolution chain from existing token
     */
    function createEvolution(
        uint256 parentTokenId,
        address to,
        string calldata uri,
        uint256 newEnergyLevel,
        uint256 newIntuitionScore,
        uint256 newCulturalRelevance
    ) external nonReentrant returns (uint256) {
        require(consciousnessMinters[msg.sender], "Not authorized to create evolution");
        require(_exists(parentTokenId), "Parent token does not exist");
        require(newEnergyLevel <= 100, "Energy level must be 0-100");
        
        ConsciousnessMetadata memory parentData = consciousnessData[parentTokenId];
        
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        
        _safeMint(to, newTokenId);
        _setTokenURI(newTokenId, uri);
        
        // Create evolved consciousness metadata
        ConsciousnessMetadata memory evolvedMetadata = ConsciousnessMetadata({
            consciousnessType: parentData.consciousnessType,
            rarity: _calculateEvolvedRarity(parentData.rarity),
            energyLevel: newEnergyLevel,
            intuitionScore: newIntuitionScore,
            culturalRelevance: newCulturalRelevance,
            evolutionStage: parentData.evolutionStage + 1,
            dimensionSignature: parentData.dimensionSignature,
            collaborators: new address[](0),
            parentTokenId: parentTokenId,
            timestamp: block.timestamp,
            isCollaborative: false
        });
        
        consciousnessData[newTokenId] = evolvedMetadata;
        evolutionChains[parentTokenId].push(newTokenId);
        
        emit EvolutionChainCreated(newTokenId, parentTokenId, to);
        
        return newTokenId;
    }
    
    /**
     * @dev Create collaborative consciousness token
     */
    function mintCollaboration(
        address[] calldata collaborators,
        string calldata uri,
        string calldata fusionType,
        uint256 avgEnergyLevel,
        uint256 avgIntuitionScore,
        uint256 culturalRelevance
    ) external nonReentrant returns (uint256) {
        require(consciousnessMinters[msg.sender], "Not authorized to mint collaborations");
        require(collaborators.length >= 2, "Need at least 2 collaborators");
        require(collaborators.length <= 10, "Too many collaborators");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        // Mint to first collaborator (they can distribute)
        _safeMint(collaborators[0], tokenId);
        _setTokenURI(tokenId, uri);
        
        // Create collaborative metadata
        ConsciousnessMetadata memory metadata = ConsciousnessMetadata({
            consciousnessType: ConsciousnessType.COLLABORATION_FUSION,
            rarity: _calculateCollaborationRarity(collaborators.length),
            energyLevel: avgEnergyLevel,
            intuitionScore: avgIntuitionScore,
            culturalRelevance: culturalRelevance,
            evolutionStage: 1,
            dimensionSignature: fusionType,
            collaborators: collaborators,
            parentTokenId: 0,
            timestamp: block.timestamp,
            isCollaborative: true
        });
        
        consciousnessData[tokenId] = metadata;
        dimensionCounts[fusionType]++;
        
        emit CollaborationMinted(tokenId, collaborators, fusionType);
        
        return tokenId;
    }
    
    /**
     * @dev Calculate rarity for evolved consciousness
     */
    function _calculateEvolvedRarity(RarityLevel parentRarity) internal pure returns (RarityLevel) {
        if (parentRarity == RarityLevel.MYTHIC) return RarityLevel.MYTHIC;
        return RarityLevel(uint(parentRarity) + 1);
    }
    
    /**
     * @dev Calculate rarity based on collaboration size
     */
    function _calculateCollaborationRarity(uint256 collaboratorCount) internal pure returns (RarityLevel) {
        if (collaboratorCount >= 8) return RarityLevel.MYTHIC;
        if (collaboratorCount >= 6) return RarityLevel.LEGENDARY;
        if (collaboratorCount >= 4) return RarityLevel.EPIC;
        if (collaboratorCount >= 3) return RarityLevel.RARE;
        return RarityLevel.UNCOMMON;
    }
    
    /**
     * @dev Get evolution chain for a token
     */
    function getEvolutionChain(uint256 tokenId) external view returns (uint256[] memory) {
        return evolutionChains[tokenId];
    }
    
    /**
     * @dev Get consciousness compatibility score between two tokens
     */
    function getCompatibilityScore(uint256 tokenId1, uint256 tokenId2) external view returns (uint256) {
        require(_exists(tokenId1) && _exists(tokenId2), "Token does not exist");
        
        ConsciousnessMetadata memory data1 = consciousnessData[tokenId1];
        ConsciousnessMetadata memory data2 = consciousnessData[tokenId2];
        
        // Calculate compatibility based on various factors
        uint256 energyDiff = data1.energyLevel > data2.energyLevel ? 
            data1.energyLevel - data2.energyLevel : 
            data2.energyLevel - data1.energyLevel;
        
        uint256 intuitionDiff = data1.intuitionScore > data2.intuitionScore ? 
            data1.intuitionScore - data2.intuitionScore : 
            data2.intuitionScore - data1.intuitionScore;
        
        // Higher compatibility for similar energy/intuition levels
        uint256 compatibility = 100 - ((energyDiff + intuitionDiff) / 2);
        
        // Bonus for same dimension
        if (keccak256(bytes(data1.dimensionSignature)) == keccak256(bytes(data2.dimensionSignature))) {
            compatibility += 20;
        }
        
        return compatibility > 100 ? 100 : compatibility;
    }
    
    /**
     * @dev Set consciousness minter status
     */
    function setConsciousnessMinter(address minter, bool status) external onlyOwner {
        consciousnessMinters[minter] = status;
    }
    
    /**
     * @dev Set royalty information
     */
    function setRoyaltyInfo(address recipient, uint256 percentage) external onlyOwner {
        require(percentage <= 1000, "Royalty too high"); // Max 10%
        royaltyRecipient = recipient;
        royaltyPercentage = percentage;
    }
    
    /**
     * @dev EIP-2981 royalty info
     */
    function royaltyInfo(uint256, uint256 salePrice) external view returns (address, uint256) {
        uint256 royaltyAmount = (salePrice * royaltyPercentage) / 10000;
        return (royaltyRecipient, royaltyAmount);
    }
    
    /**
     * @dev Pause contract
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    // Override required functions
    function _beforeTokenTransfer(address from, address to, uint256 tokenId, uint256 batchSize)
        internal
        override(ERC721, ERC721Enumerable)
        whenNotPaused
    {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }
    
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete consciousnessData[tokenId];
    }
    
    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
    
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}