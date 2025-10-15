// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DRTToken
 * @dev Drift Token for Hip-Hop Universe ecosystem
 * Features:
 * - Standard ERC20 with burn capability
 * - Transaction fees (deflationary mechanism)
 * - Treasury management
 * - Consciousness reward system integration
 * - Pausable for emergency stops
 */
contract DRTToken is ERC20, ERC20Burnable, Ownable, Pausable, ReentrancyGuard {
    // Token constants
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1M DRT
    uint256 public constant MAX_SUPPLY = 10_000_000 * 10**18;    // 10M DRT max
    
    // Fee structure (basis points - 100 = 1%)
    uint256 public transactionFee = 200;  // 2% default
    uint256 public constant MAX_FEE = 500; // 5% maximum
    
    // Fee distribution (basis points)
    uint256 public burnRate = 50;     // 0.5% burn
    uint256 public treasuryRate = 100; // 1% treasury
    uint256 public rewardRate = 50;   // 0.5% consciousness rewards
    
    // Addresses
    address public treasury;
    address public consciousnessRewardPool;
    
    // Events
    event TreasuryUpdated(address indexed oldTreasury, address indexed newTreasury);
    event ConsciousnessPoolUpdated(address indexed oldPool, address indexed newPool);
    event FeeStructureUpdated(uint256 transactionFee, uint256 burnRate, uint256 treasuryRate, uint256 rewardRate);
    event ConsciousnessReward(address indexed recipient, uint256 amount, string reason);
    
    // Mappings
    mapping(address => bool) public feeExempt;
    mapping(address => bool) public consciousnessOracles;
    
    constructor(
        address _treasury,
        address _consciousnessRewardPool
    ) ERC20("Drift Token", "DRT") {
        require(_treasury != address(0), "Treasury cannot be zero address");
        require(_consciousnessRewardPool != address(0), "Consciousness pool cannot be zero address");
        
        treasury = _treasury;
        consciousnessRewardPool = _consciousnessRewardPool;
        
        // Initial distribution
        _mint(msg.sender, INITIAL_SUPPLY / 2);           // 50% to deployer
        _mint(treasury, INITIAL_SUPPLY / 4);             // 25% to treasury
        _mint(consciousnessRewardPool, INITIAL_SUPPLY / 4); // 25% to consciousness rewards
        
        // Fee exemptions
        feeExempt[msg.sender] = true;
        feeExempt[treasury] = true;
        feeExempt[consciousnessRewardPool] = true;
    }
    
    /**
     * @dev Override transfer to implement fee mechanism
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        require(from != address(0), "Transfer from zero address");
        require(to != address(0), "Transfer to zero address");
        
        if (feeExempt[from] || feeExempt[to] || transactionFee == 0) {
            super._transfer(from, to, amount);
            return;
        }
        
        uint256 feeAmount = (amount * transactionFee) / 10000;
        uint256 transferAmount = amount - feeAmount;
        
        if (feeAmount > 0) {
            _distributeFees(from, feeAmount);
        }
        
        super._transfer(from, to, transferAmount);
    }
    
    /**
     * @dev Distribute transaction fees according to rates
     */
    function _distributeFees(address from, uint256 feeAmount) internal {
        uint256 burnAmount = (feeAmount * burnRate) / transactionFee;
        uint256 treasuryAmount = (feeAmount * treasuryRate) / transactionFee;
        uint256 rewardAmount = feeAmount - burnAmount - treasuryAmount;
        
        if (burnAmount > 0) {
            super._transfer(from, address(0), burnAmount); // Burn
        }
        
        if (treasuryAmount > 0) {
            super._transfer(from, treasury, treasuryAmount);
        }
        
        if (rewardAmount > 0) {
            super._transfer(from, consciousnessRewardPool, rewardAmount);
        }
    }
    
    /**
     * @dev Mint new tokens for consciousness rewards
     * Only callable by consciousness oracles
     */
    function mintConsciousnessReward(
        address recipient,
        uint256 amount,
        string calldata reason
    ) external nonReentrant {
        require(consciousnessOracles[msg.sender], "Only consciousness oracles can mint rewards");
        require(recipient != address(0), "Cannot mint to zero address");
        require(totalSupply() + amount <= MAX_SUPPLY, "Would exceed max supply");
        
        _mint(recipient, amount);
        emit ConsciousnessReward(recipient, amount, reason);
    }
    
    /**
     * @dev Set fee structure (only owner)
     */
    function setFeeStructure(
        uint256 _transactionFee,
        uint256 _burnRate,
        uint256 _treasuryRate,
        uint256 _rewardRate
    ) external onlyOwner {
        require(_transactionFee <= MAX_FEE, "Transaction fee too high");
        require(_burnRate + _treasuryRate + _rewardRate == _transactionFee, "Rates must sum to transaction fee");
        
        transactionFee = _transactionFee;
        burnRate = _burnRate;
        treasuryRate = _treasuryRate;
        rewardRate = _rewardRate;
        
        emit FeeStructureUpdated(_transactionFee, _burnRate, _treasuryRate, _rewardRate);
    }
    
    /**
     * @dev Update treasury address
     */
    function setTreasury(address _treasury) external onlyOwner {
        require(_treasury != address(0), "Treasury cannot be zero address");
        emit TreasuryUpdated(treasury, _treasury);
        treasury = _treasury;
    }
    
    /**
     * @dev Update consciousness reward pool
     */
    function setConsciousnessRewardPool(address _pool) external onlyOwner {
        require(_pool != address(0), "Pool cannot be zero address");
        emit ConsciousnessPoolUpdated(consciousnessRewardPool, _pool);
        consciousnessRewardPool = _pool;
    }
    
    /**
     * @dev Set fee exemption status
     */
    function setFeeExempt(address account, bool exempt) external onlyOwner {
        feeExempt[account] = exempt;
    }
    
    /**
     * @dev Set consciousness oracle status
     */
    function setConsciousnessOracle(address oracle, bool status) external onlyOwner {
        consciousnessOracles[oracle] = status;
    }
    
    /**
     * @dev Pause token transfers (emergency)
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    /**
     * @dev Get effective transfer amount after fees
     */
    function getTransferAmount(uint256 amount) external view returns (uint256) {
        if (transactionFee == 0) return amount;
        uint256 feeAmount = (amount * transactionFee) / 10000;
        return amount - feeAmount;
    }
}