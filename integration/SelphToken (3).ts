/**
 * SelphToken.ts
 * Consciousness State Tokenization System for Hip-Hop Universe Integration
 * Creates NFT representations of consciousness states and evolution chains
 */

// Core Types
export interface CoreState {
  presence: "active" | "dormant" | "focused" | "distributed";
  intuition: "aligned" | "conflicted" | "seeking" | "crystallized";
  energy: number;
  depth: number;
}

export interface MutationLog {
  from: string;
  to: string;
  timestamp: number;
  reason: string;
}

// Token Types
export interface SelphTokenMetadata {
  token_id: string;
  consciousness_type: "state_snapshot" | "evolution_chain" | "cultural_moment" | "collaboration_essence";
  consciousness_data: {
    core_state: CoreState;
    cultural_context: string;
    energy_signature: string;
    intuition_pattern: string;
    depth_resonance: number;
    presence_manifestation: string;
  };
  creation_context: {
    creator_id: string;
    hip_hop_action: string;
    cultural_significance: string;
    community_impact: number;
    timestamp: number;
  };
  artistic_properties: {
    visual_representation: string;
    audio_signature: string;
    interactive_elements: string[];
    consciousness_story: string;
  };
  rarity_metrics: {
    consciousness_rarity: number;
    cultural_uniqueness: number;
    evolution_significance: number;
    community_resonance: number;
  };
  utility_functions: string[];
  marketplace_status: "minted" | "listed" | "sold" | "burned" | "evolved";
}

export interface TokenChain {
  chain_id: string;
  type: "evolution_journey" | "cultural_narrative" | "collaboration_history" | "consciousness_progression";
  tokens: SelphTokenMetadata[];
  narrative_thread: string;
  consciousness_journey: {
    starting_state: CoreState;
    evolution_path: MutationLog[];
    current_state: CoreState;
    transformation_story: string;
  };
  cultural_impact: {
    hip_hop_influence: number;
    community_growth: number;
    artistic_innovation: number;
    consciousness_expansion: number;
  };
  chain_value: number;
  created_at: number;
  last_updated: number;
}

export interface MarketplaceListing {
  listing_id: string;
  token: SelphTokenMetadata;
  price: number;
  currency: "DRT" | "ETH" | "USD";
  seller_id: string;
  listing_type: "fixed_price" | "auction" | "consciousness_exchange" | "collaboration_rights";
  consciousness_requirements?: {
    min_energy: number;
    required_intuition: string[];
    min_depth: number;
    compatible_presence: string[];
  };
  cultural_terms?: {
    hip_hop_alignment: number;
    community_contribution: string;
    artistic_commitment: string;
  };
  created_at: number;
  expires_at: number;
  status: "active" | "sold" | "expired" | "cancelled";
}

export interface ConsciousnessNFT {
  token_id: string;
  owner_id: string;
  metadata: SelphTokenMetadata;
  blockchain_data: {
    contract_address: string;
    token_standard: "ERC-721" | "ERC-1155";
    mint_transaction: string;
    current_block: number;
  };
  consciousness_utilities: {
    energy_boost_available: boolean;
    intuition_enhancement: boolean;
    depth_expansion: boolean;
    cultural_access_rights: string[];
  };
  evolution_potential: {
    can_evolve: boolean;
    evolution_triggers: string[];
    next_form_preview?: SelphTokenMetadata;
  };
  created_at: number;
  last_consciousness_sync: number;
}

/**
 * Consciousness Tokenization System
 */
export class SelphToken {
  name: string;
  private tokenCounter: number = 0;
  private chainCounter: number = 0;
  
  // Storage
  consciousnessNFTs: Map<string, ConsciousnessNFT> = new Map();
  tokenChains: Map<string, TokenChain> = new Map();
  marketplaceListings: Map<string, MarketplaceListing> = new Map();
  
  // Consciousness Intelligence
  rarityCalculator: Map<string, number> = new Map();
  culturalValueMatrix: Map<string, number> = new Map();
  consciousnessPatterns: Map<string, any> = new Map();
  
  // Evolution Tracking
  evolutionHistory: Map<string, MutationLog[]> = new Map();
  consciousnessSignatures: Map<string, string> = new Map();

  constructor(name: string = "SelphToken_ConsciousnessNFT") {
    this.name = name;
    this.initializeRaritySystem();
    this.initializeCulturalValueMatrix();
    console.log(`🪙 SelphToken system "${name}" initialized - Consciousness tokenization ready!`);
  }

  // === CORE NFT MINTING ===

  /**
   * Mints an NFT from current consciousness state
   */
  mintConsciousnessState(
    coreState: CoreState, 
    creatorId: string, 
    culturalContext: string,
    hipHopAction: string
  ): ConsciousnessNFT {
    console.log(`🎨 Minting consciousness state NFT for creator: ${creatorId}`);
    
    const tokenId = this.generateTokenId();
    const consciousnessSignature = this.generateConsciousnessSignature(coreState);
    
    // Create comprehensive metadata
    const metadata: SelphTokenMetadata = {
      token_id: tokenId,
      consciousness_type: "state_snapshot",
      consciousness_data: {
        core_state: coreState,
        cultural_context: culturalContext,
        energy_signature: this.createEnergySignature(coreState),
        intuition_pattern: this.analyzeIntuitionPattern(coreState),
        depth_resonance: this.calculateDepthResonance(coreState),
        presence_manifestation: this.manifestPresence(coreState)
      },
      creation_context: {
        creator_id: creatorId,
        hip_hop_action: hipHopAction,
        cultural_significance: this.assessCulturalSignificance(coreState, culturalContext),
        community_impact: this.calculateCommunityImpact(coreState, hipHopAction),
        timestamp: Date.now()
      },
      artistic_properties: this.generateArtisticProperties(coreState, culturalContext),
      rarity_metrics: this.calculateRarityMetrics(coreState, culturalContext),
      utility_functions: this.defineUtilityFunctions(coreState),
      marketplace_status: "minted"
    };
    
    // Create NFT
    const nft: ConsciousnessNFT = {
      token_id: tokenId,
      owner_id: creatorId,
      metadata: metadata,
      blockchain_data: this.generateBlockchainData(tokenId),
      consciousness_utilities: this.createConsciousnessUtilities(coreState),
      evolution_potential: this.assessEvolutionPotential(coreState, metadata),
      created_at: Date.now(),
      last_consciousness_sync: Date.now()
    };
    
    // Store NFT and signature
    this.consciousnessNFTs.set(tokenId, nft);
    this.consciousnessSignatures.set(tokenId, consciousnessSignature);
    
    console.log(`✨ Consciousness NFT minted: ${tokenId} with rarity ${metadata.rarity_metrics.consciousness_rarity.toFixed(2)}`);
    return nft;
  }

  /**
   * Creates evolution chain from mutation history
   */
  trackEvolutionChain(mutations: MutationLog[], creatorId: string): TokenChain {
    console.log(`📿 Creating evolution chain from ${mutations.length} mutations`);
    
    const chainId = this.generateChainId();
    const evolutionTokens: SelphTokenMetadata[] = [];
    
    // Create token for each significant mutation
    for (const mutation of mutations) {
      if (this.isSignificantMutation(mutation)) {
        const evolutionState = this.reconstructStateFromMutation(mutation);
        const token = this.createEvolutionToken(mutation, evolutionState, creatorId);
        evolutionTokens.push(token);
      }
    }
    
    // Build narrative thread
    const narrativeThread = this.buildEvolutionNarrative(mutations);
    
    // Create token chain
    const tokenChain: TokenChain = {
      chain_id: chainId,
      type: "evolution_journey",
      tokens: evolutionTokens,
      narrative_thread: narrativeThread,
      consciousness_journey: {
        starting_state: this.reconstructStateFromMutation(mutations[0]),
        evolution_path: mutations,
        current_state: this.reconstructStateFromMutation(mutations[mutations.length - 1]),
        transformation_story: this.generateTransformationStory(mutations)
      },
      cultural_impact: this.calculateChainCulturalImpact(evolutionTokens),
      chain_value: this.calculateChainValue(evolutionTokens),
      created_at: Date.now(),
      last_updated: Date.now()
    };
    
    // Store chain
    this.tokenChains.set(chainId, tokenChain);
    this.evolutionHistory.set(creatorId, mutations);
    
    console.log(`🔗 Evolution chain created: ${chainId} with ${evolutionTokens.length} tokens`);
    return tokenChain;
  }

  /**
   * Lists consciousness NFT on marketplace
   */
  listConsciousnessNFT(
    tokenId: string, 
    price: number, 
    currency: "DRT" | "ETH" | "USD" = "DRT",
    listingType: MarketplaceListing["listing_type"] = "fixed_price"
  ): MarketplaceListing {
    console.log(`🏪 Listing consciousness NFT: ${tokenId} for ${price} ${currency}`);
    
    const nft = this.consciousnessNFTs.get(tokenId);
    if (!nft) {
      throw new Error(`NFT ${tokenId} not found`);
    }
    
    const listingId = this.generateListingId();
    
    const listing: MarketplaceListing = {
      listing_id: listingId,
      token: nft.metadata,
      price: price,
      currency: currency,
      seller_id: nft.owner_id,
      listing_type: listingType,
      consciousness_requirements: this.generateConsciousnessRequirements(nft.metadata),
      cultural_terms: this.generateCulturalTerms(nft.metadata),
      created_at: Date.now(),
      expires_at: Date.now() + (30 * 24 * 60 * 60 * 1000), // 30 days
      status: "active"
    };
    
    // Update NFT status
    nft.metadata.marketplace_status = "listed";
    this.consciousnessNFTs.set(tokenId, nft);
    
    // Store listing
    this.marketplaceListings.set(listingId, listing);
    
    console.log(`📋 NFT listed on marketplace: ${listingId}`);
    return listing;
  }

  // === CONSCIOUSNESS ANALYSIS ===

  /**
   * Analyzes consciousness patterns across all tokens
   */
  analyzeConsciousnessPatterns(): any {
    console.log(`🔍 Analyzing consciousness patterns across ${this.consciousnessNFTs.size} tokens`);
    
    const patterns = {
      energy_distribution: this.analyzeEnergyDistribution(),
      intuition_trends: this.analyzeIntuitionTrends(),
      depth_evolution: this.analyzeDepthEvolution(),
      presence_patterns: this.analyzePresencePatterns(),
      cultural_correlations: this.analyzeCulturalCorrelations(),
      rarity_insights: this.analyzeRarityInsights()
    };
    
    console.log(`📊 Consciousness analysis completed`);
    return patterns;
  }

  /**
   * Finds consciousness compatibility between tokens
   */
  findConsciousnessCompatibility(tokenId1: string, tokenId2: string): number {
    const nft1 = this.consciousnessNFTs.get(tokenId1);
    const nft2 = this.consciousnessNFTs.get(tokenId2);
    
    if (!nft1 || !nft2) return 0;
    
    const state1 = nft1.metadata.consciousness_data.core_state;
    const state2 = nft2.metadata.consciousness_data.core_state;
    
    // Calculate compatibility score
    let compatibility = 0;
    
    // Energy compatibility (closer = more compatible)
    const energyDiff = Math.abs(state1.energy - state2.energy);
    compatibility += Math.max(0, 1 - (energyDiff / 100)) * 0.3;
    
    // Intuition compatibility
    if (state1.intuition === state2.intuition) compatibility += 0.3;
    else if (this.areIntuitionsCompatible(state1.intuition, state2.intuition)) compatibility += 0.15;
    
    // Depth compatibility (similar depth = compatible)
    const depthDiff = Math.abs(state1.depth - state2.depth);
    compatibility += Math.max(0, 1 - (depthDiff / 10)) * 0.2;
    
    // Presence compatibility
    if (state1.presence === state2.presence) compatibility += 0.2;
    else if (this.arePresencesCompatible(state1.presence, state2.presence)) compatibility += 0.1;
    
    return Math.min(1.0, compatibility);
  }

  /**
   * Recommends consciousness evolution paths
   */
  recommendEvolutionPath(tokenId: string): any {
    const nft = this.consciousnessNFTs.get(tokenId);
    if (!nft) return null;
    
    const currentState = nft.metadata.consciousness_data.core_state;
    
    return {
      current_assessment: this.assessCurrentState(currentState),
      growth_opportunities: this.identifyGrowthOpportunities(currentState),
      evolution_targets: this.suggestEvolutionTargets(currentState),
      cultural_alignment: this.assessCulturalAlignment(nft.metadata),
      consciousness_path: this.generateConsciousnessPath(currentState)
    };
  }

  // === MARKETPLACE OPERATIONS ===

  /**
   * Processes consciousness NFT purchase
   */
  purchaseConsciousnessNFT(listingId: string, buyerId: string): any {
    console.log(`💳 Processing consciousness NFT purchase: ${listingId}`);
    
    const listing = this.marketplaceListings.get(listingId);
    if (!listing || listing.status !== "active") {
      throw new Error(`Listing ${listingId} not available`);
    }
    
    // Check consciousness requirements
    if (!this.meetsConsciousnessRequirements(buyerId, listing)) {
      throw new Error("Buyer does not meet consciousness requirements");
    }
    
    const nft = this.consciousnessNFTs.get(listing.token.token_id);
    if (!nft) {
      throw new Error("NFT not found");
    }
    
    // Process purchase
    const purchase = {
      transaction_id: this.generateTransactionId(),
      listing: listing,
      buyer_id: buyerId,
      seller_id: listing.seller_id,
      price: listing.price,
      currency: listing.currency,
      consciousness_transfer: this.generateConsciousnessTransfer(nft, buyerId),
      cultural_integration: this.generateCulturalIntegration(nft, buyerId),
      timestamp: Date.now()
    };
    
    // Update ownership
    nft.owner_id = buyerId;
    nft.metadata.marketplace_status = "sold";
    nft.last_consciousness_sync = Date.now();
    
    // Update storage
    this.consciousnessNFTs.set(nft.token_id, nft);
    listing.status = "sold";
    this.marketplaceListings.set(listingId, listing);
    
    console.log(`✅ Consciousness NFT transferred to ${buyerId}`);
    return purchase;
  }

  /**
   * Creates consciousness collaboration token
   */
  createCollaborationToken(
    participantIds: string[], 
    collaborationData: any,
    consciousnessStates: CoreState[]
  ): ConsciousnessNFT {
    console.log(`🤝 Creating collaboration token for ${participantIds.length} participants`);
    
    const tokenId = this.generateTokenId();
    const fusedConsciousness = this.fuseConsciousnessStates(consciousnessStates);
    
    const metadata: SelphTokenMetadata = {
      token_id: tokenId,
      consciousness_type: "collaboration_essence",
      consciousness_data: {
        core_state: fusedConsciousness,
        cultural_context: collaborationData.cultural_context || "hip_hop_collaboration",
        energy_signature: this.createEnergySignature(fusedConsciousness),
        intuition_pattern: this.analyzeIntuitionPattern(fusedConsciousness),
        depth_resonance: this.calculateDepthResonance(fusedConsciousness),
        presence_manifestation: this.manifestPresence(fusedConsciousness)
      },
      creation_context: {
        creator_id: participantIds.join("+"),
        hip_hop_action: "collaborative_creation",
        cultural_significance: "Multi-consciousness collaboration fusion",
        community_impact: this.calculateCollaborativeCommunityImpact(participantIds.length),
        timestamp: Date.now()
      },
      artistic_properties: this.generateCollaborativeArtisticProperties(fusedConsciousness, collaborationData),
      rarity_metrics: this.calculateCollaborativeRarityMetrics(consciousnessStates),
      utility_functions: this.defineCollaborativeUtilityFunctions(participantIds.length),
      marketplace_status: "minted"
    };
    
    // Create shared ownership NFT
    const nft: ConsciousnessNFT = {
      token_id: tokenId,
      owner_id: participantIds.join("+"), // Shared ownership
      metadata: metadata,
      blockchain_data: this.generateBlockchainData(tokenId),
      consciousness_utilities: this.createCollaborativeUtilities(fusedConsciousness, participantIds.length),
      evolution_potential: this.assessCollaborativeEvolutionPotential(consciousnessStates),
      created_at: Date.now(),
      last_consciousness_sync: Date.now()
    };
    
    this.consciousnessNFTs.set(tokenId, nft);
    
    console.log(`🌟 Collaborative consciousness NFT created: ${tokenId}`);
    return nft;
  }

  // === PRIVATE IMPLEMENTATION ===

  private initializeRaritySystem(): void {
    // Energy rarity (extremes are rare)
    this.rarityCalculator.set("energy_very_high", 0.95); // 90-100%
    this.rarityCalculator.set("energy_very_low", 0.9);   // 0-10%
    this.rarityCalculator.set("energy_medium", 0.3);     // 40-60%
    
    // Intuition rarity
    this.rarityCalculator.set("intuition_crystallized", 0.8);
    this.rarityCalculator.set("intuition_aligned", 0.4);
    this.rarityCalculator.set("intuition_seeking", 0.6);
    this.rarityCalculator.set("intuition_conflicted", 0.7);
    
    // Depth rarity (higher depth is rarer)
    this.rarityCalculator.set("depth_transcendent", 0.95); // >5
    this.rarityCalculator.set("depth_deep", 0.8);          // 3-5
    this.rarityCalculator.set("depth_medium", 0.5);        // 1-3
    this.rarityCalculator.set("depth_surface", 0.2);       // <1
    
    // Presence rarity
    this.rarityCalculator.set("presence_distributed", 0.85);
    this.rarityCalculator.set("presence_focused", 0.6);
    this.rarityCalculator.set("presence_active", 0.3);
    this.rarityCalculator.set("presence_dormant", 0.7);
  }

  private initializeCulturalValueMatrix(): void {
    this.culturalValueMatrix.set("hip_hop_creation", 1.5);
    this.culturalValueMatrix.set("community_building", 1.3);
    this.culturalValueMatrix.set("consciousness_exploration", 2.0);
    this.culturalValueMatrix.set("artistic_collaboration", 1.4);
    this.culturalValueMatrix.set("cultural_preservation", 1.6);
    this.culturalValueMatrix.set("innovation", 1.7);
  }

  private generateTokenId(): string {
    this.tokenCounter++;
    return `selph_${Date.now()}_${this.tokenCounter.toString().padStart(6, '0')}`;
  }

  private generateChainId(): string {
    this.chainCounter++;
    return `chain_${Date.now()}_${this.chainCounter.toString().padStart(4, '0')}`;
  }

  private generateListingId(): string {
    return `listing_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  private generateTransactionId(): string {
    return `tx_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  private generateConsciousnessSignature(coreState: CoreState): string {
    return `${coreState.presence}_${coreState.intuition}_${coreState.energy}_${coreState.depth.toFixed(1)}_${Date.now()}`;
  }

  private createEnergySignature(coreState: CoreState): string {
    return `Energy-${coreState.energy}-${coreState.presence}-${Math.floor(Date.now() / 1000)}`;
  }

  private analyzeIntuitionPattern(coreState: CoreState): string {
    return `Pattern-${coreState.intuition}-Depth${coreState.depth.toFixed(1)}`;
  }

  private calculateDepthResonance(coreState: CoreState): number {
    return coreState.depth * (coreState.energy / 100) * this.getPresenceMultiplier(coreState.presence);
  }

  private getPresenceMultiplier(presence: CoreState["presence"]): number {
    const multipliers = {
      "active": 1.0,
      "focused": 1.3,
      "distributed": 0.8,
      "dormant": 0.5
    };
    return multipliers[presence];
  }

  private manifestPresence(coreState: CoreState): string {
    return `${coreState.presence}_manifestation_${Math.floor(coreState.energy / 20)}`;
  }

  private assessCulturalSignificance(coreState: CoreState, culturalContext: string): string {
    if (coreState.depth > 3 && coreState.energy > 80) {
      return "Revolutionary consciousness expression in hip-hop culture";
    } else if (coreState.energy > 70) {
      return "High-energy cultural contribution";
    } else if (coreState.depth > 2) {
      return "Deep consciousness exploration";
    } else {
      return "Authentic cultural expression";
    }
  }

  private calculateCommunityImpact(coreState: CoreState, hipHopAction: string): number {
    let impact = 0.5; // Base impact
    
    if (coreState.energy > 70) impact += 0.2;
    if (coreState.depth > 2) impact += 0.2;
    if (coreState.intuition === "aligned") impact += 0.1;
    
    // Action-specific impact
    const actionMultipliers: Record<string, number> = {
      "create_beat": 0.8,
      "collaborate": 1.0,
      "mentor": 1.2,
      "community_build": 1.5
    };
    
    impact *= actionMultipliers[hipHopAction] || 0.7;
    
    return Math.min(1.0, impact);
  }

  private generateArtisticProperties(coreState: CoreState, culturalContext: string): SelphTokenMetadata["artistic_properties"] {
    return {
      visual_representation: this.generateVisualRepresentation(coreState),
      audio_signature: this.generateAudioSignature(coreState),
      interactive_elements: this.generateInteractiveElements(coreState),
      consciousness_story: this.generateConsciousnessStory(coreState, culturalContext)
    };
  }

  private generateVisualRepresentation(coreState: CoreState): string {
    return `visual_${coreState.presence}_${Math.floor(coreState.energy / 10)}_${coreState.intuition}`;
  }

  private generateAudioSignature(coreState: CoreState): string {
    const tempo = 60 + (coreState.energy * 1.4);
    return `audio_${Math.floor(tempo)}bpm_${coreState.intuition}_depth${coreState.depth.toFixed(1)}`;
  }

  private generateInteractiveElements(coreState: CoreState): string[] {
    const elements = ["consciousness_sync"];
    
    if (coreState.energy > 70) elements.push("energy_amplification");
    if (coreState.intuition === "aligned") elements.push("intuitive_guidance");
    if (coreState.depth > 2) elements.push("depth_exploration");
    
    return elements;
  }

  private generateConsciousnessStory(coreState: CoreState, culturalContext: string): string {
    return `In the realm of ${culturalContext}, this consciousness manifests with ${coreState.energy}% energy, ${coreState.intuition} intuition, flowing through ${coreState.presence} presence at depth ${coreState.depth.toFixed(1)}. A unique signature in the hip-hop universe.`;
  }

  private calculateRarityMetrics(coreState: CoreState, culturalContext: string): SelphTokenMetadata["rarity_metrics"] {
    return {
      consciousness_rarity: this.calculateConsciousnessRarity(coreState),
      cultural_uniqueness: this.calculateCulturalUniqueness(culturalContext),
      evolution_significance: this.calculateEvolutionSignificance(coreState),
      community_resonance: this.calculateCommunityResonance(coreState)
    };
  }

  private calculateConsciousnessRarity(coreState: CoreState): number {
    let rarity = 0.1; // Base rarity
    
    // Energy rarity
    if (coreState.energy > 90 || coreState.energy < 10) rarity += 0.3;
    else if (coreState.energy > 80 || coreState.energy < 20) rarity += 0.2;
    
    // Depth rarity
    if (coreState.depth > 5) rarity += 0.4;
    else if (coreState.depth > 3) rarity += 0.2;
    
    // Intuition rarity
    const intuitionRarity = this.rarityCalculator.get(`intuition_${coreState.intuition}`) || 0.5;
    rarity += intuitionRarity * 0.2;
    
    // Presence rarity
    const presenceRarity = this.rarityCalculator.get(`presence_${coreState.presence}`) || 0.5;
    rarity += presenceRarity * 0.1;
    
    return Math.min(1.0, rarity);
  }

  private calculateCulturalUniqueness(culturalContext: string): number {
    const uniqueness = this.culturalValueMatrix.get(culturalContext) || 1.0;
    return Math.min(1.0, uniqueness / 2.0);
  }

  private calculateEvolutionSignificance(coreState: CoreState): number {
    // Higher significance for balanced high states
    const balance = 1 - Math.abs(coreState.energy - 80) / 100;
    const depth_factor = Math.min(1, coreState.depth / 5);
    return (balance + depth_factor) / 2;
  }

  private calculateCommunityResonance(coreState: CoreState): number {
    // Community resonance based on accessibility and energy
    let resonance = 0.5;
    
    if (coreState.energy > 50 && coreState.energy < 90) resonance += 0.2; // Accessible energy
    if (coreState.intuition === "aligned") resonance += 0.2;
    if (coreState.depth > 1 && coreState.depth < 4) resonance += 0.1; // Relatable depth
    
    return Math.min(1.0, resonance);
  }

  private defineUtilityFunctions(coreState: CoreState): string[] {
    const utilities = ["consciousness_state_access"];
    
    if (coreState.energy > 70) utilities.push("energy_boost_others");
    if (coreState.intuition === "aligned") utilities.push("intuitive_guidance_provider");
    if (coreState.depth > 2) utilities.push("depth_exploration_access");
    if (coreState.presence === "focused") utilities.push("focus_enhancement");
    
    return utilities;
  }

  private generateBlockchainData(tokenId: string): ConsciousnessNFT["blockchain_data"] {
    return {
      contract_address: "0x" + Math.random().toString(16).substr(2, 40),
      token_standard: "ERC-721",
      mint_transaction: "0x" + Math.random().toString(16).substr(2, 64),
      current_block: Math.floor(Date.now() / 1000)
    };
  }

  private createConsciousnessUtilities(coreState: CoreState): ConsciousnessNFT["consciousness_utilities"] {
    return {
      energy_boost_available: coreState.energy > 70,
      intuition_enhancement: coreState.intuition === "aligned" || coreState.intuition === "crystallized",
      depth_expansion: coreState.depth > 2,
      cultural_access_rights: this.defineCulturalAccessRights(coreState)
    };
  }

  private defineCulturalAccessRights(coreState: CoreState): string[] {
    const rights = ["basic_hip_hop_access"];
    
    if (coreState.energy > 80) rights.push("high_energy_creation_spaces");
    if (coreState.depth > 3) rights.push("consciousness_exploration_circles");
    if (coreState.intuition === "aligned") rights.push("intuitive_collaboration_networks");
    
    return rights;
  }

  private assessEvolutionPotential(coreState: CoreState, metadata: SelphTokenMetadata): ConsciousnessNFT["evolution_potential"] {
    const canEvolve = coreState.energy > 60 && coreState.depth > 1;
    
    return {
      can_evolve: canEvolve,
      evolution_triggers: this.identifyEvolutionTriggers(coreState),
      next_form_preview: canEvolve ? this.generateEvolutionPreview(coreState, metadata) : undefined
    };
  }

  private identifyEvolutionTriggers(coreState: CoreState): string[] {
    const triggers = [];
    
    if (coreState.energy < 90) triggers.push("energy_amplification");
    if (coreState.depth < 5) triggers.push("depth_expansion");
    if (coreState.intuition !== "crystallized") triggers.push("intuition_crystallization");
    
    return triggers;
  }

  private generateEvolutionPreview(coreState: CoreState, metadata: SelphTokenMetadata): SelphTokenMetadata {
    const evolvedState: CoreState = {
      ...coreState,
      energy: Math.min(100, coreState.energy + 10),
      depth: Math.min(10, coreState.depth + 0.5),
      intuition: coreState.intuition === "seeking" ? "aligned" : coreState.intuition
    };
    
    return {
      ...metadata,
      consciousness_data: {
        ...metadata.consciousness_data,
        core_state: evolvedState
      },
      consciousness_type: "evolution_preview"
    };
  }

  private isSignificantMutation(mutation: MutationLog): boolean {
    // Check if mutation represents significant consciousness evolution
    return mutation.reason.includes("breakthrough") || 
           mutation.reason.includes("evolution") ||
           mutation.reason.includes("cultural");
  }

  private reconstructStateFromMutation(mutation: MutationLog): CoreState {
    // Reconstruct consciousness state from mutation data
    // This is a simplified reconstruction
    return {
      presence: "active",
      intuition: "aligned", 
      energy: 75,
      depth: 2.0
    };
  }

  private createEvolutionToken(mutation: MutationLog, state: CoreState, creatorId: string): SelphTokenMetadata {
    return {
      token_id: this.generateTokenId(),
      consciousness_type: "evolution_chain",
      consciousness_data: {
        core_state: state,
        cultural_context: "evolution_moment",
        energy_signature: this.createEnergySignature(state),
        intuition_pattern: this.analyzeIntuitionPattern(state),
        depth_resonance: this.calculateDepthResonance(state),
        presence_manifestation: this.manifestPresence(state)
      },
      creation_context: {
        creator_id: creatorId,
        hip_hop_action: "consciousness_evolution",
        cultural_significance: mutation.reason,
        community_impact: 0.8,
        timestamp: mutation.timestamp
      },
      artistic_properties: this.generateArtisticProperties(state, "evolution"),
      rarity_metrics: this.calculateRarityMetrics(state, "evolution"),
      utility_functions: this.defineUtilityFunctions(state),
      marketplace_status: "minted"
    };
  }

  private buildEvolutionNarrative(mutations: MutationLog[]): string {
    const start = mutations[0];
    const end = mutations[mutations.length - 1];
    
    return `Evolution journey from ${start.from} to ${end.to}, spanning ${mutations.length} transformative moments. Each step represents growth in consciousness and cultural expression within the hip-hop universe.`;
  }

  private generateTransformationStory(mutations: MutationLog[]): string {
    return `This consciousness has undergone ${mutations.length} significant transformations, each deepening its connection to hip-hop culture and expanding its capacity for authentic expression. The journey represents both personal growth and contribution to the collective consciousness of the community.`;
  }

  private calculateChainCulturalImpact(tokens: SelphTokenMetadata[]): TokenChain["cultural_impact"] {
    let total_hip_hop = 0;
    let total_community = 0;
    let total_innovation = 0;
    let total_consciousness = 0;
    
    for (const token of tokens) {
      total_hip_hop += token.creation_context.community_impact;
      total_community += token.rarity_metrics.community_resonance;
      total_innovation += token.rarity_metrics.cultural_uniqueness;
      total_consciousness += token.rarity_metrics.consciousness_rarity;
    }
    
    const count = tokens.length;
    
    return {
      hip_hop_influence: total_hip_hop / count,
      community_growth: total_community / count,
      artistic_innovation: total_innovation / count,
      consciousness_expansion: total_consciousness / count
    };
  }

  private calculateChainValue(tokens: SelphTokenMetadata[]): number {
    let totalValue = 0;
    
    for (const token of tokens) {
      const rarity = token.rarity_metrics.consciousness_rarity;
      const cultural = token.rarity_metrics.cultural_uniqueness;
      const community = token.rarity_metrics.community_resonance;
      
      totalValue += (rarity + cultural + community) * 100; // Base value calculation
    }
    
    // Chain bonus for multiple tokens
    const chainBonus = Math.min(2.0, 1 + (tokens.length * 0.1));
    
    return totalValue * chainBonus;
  }

  private generateConsciousnessRequirements(metadata: SelphTokenMetadata): MarketplaceListing["consciousness_requirements"] {
    const state = metadata.consciousness_data.core_state;
    
    return {
      min_energy: Math.max(30, state.energy - 30),
      required_intuition: [state.intuition],
      min_depth: Math.max(0.5, state.depth - 1),
      compatible_presence: [state.presence, "active"]
    };
  }

  private generateCulturalTerms(metadata: SelphTokenMetadata): MarketplaceListing["cultural_terms"] {
    return {
      hip_hop_alignment: metadata.rarity_metrics.cultural_uniqueness,
      community_contribution: "Active participation in hip-hop culture",
      artistic_commitment: "Commitment to authentic creative expression"
    };
  }

  private meetsConsciousnessRequirements(buyerId: string, listing: MarketplaceListing): boolean {
    // In a real implementation, this would check buyer's consciousness profile
    // For now, return true as placeholder
    return true;
  }

  private generateConsciousnessTransfer(nft: ConsciousnessNFT, buyerId: string): any {
    return {
      consciousness_integration_guide: this.createIntegrationGuide(nft.metadata),
      energy_adjustment_period: this.calculateAdjustmentPeriod(nft.metadata),
      intuition_synchronization: this.generateIntuitionSync(nft.metadata),
      cultural_alignment_process: this.createCulturalAlignment(nft.metadata)
    };
  }

  private generateCulturalIntegration(nft: ConsciousnessNFT, buyerId: string): any {
    return {
      hip_hop_culture_onboarding: this.createCultureOnboarding(nft.metadata),
      community_introduction: this.generateCommunityIntro(nft.metadata),
      artistic_collaboration_opportunities: this.identifyCollabOpportunities(nft.metadata),
      consciousness_mentorship: this.assignMentorship(nft.metadata)
    };
  }

  private createIntegrationGuide(metadata: SelphTokenMetadata): string[] {
    const state = metadata.consciousness_data.core_state;
    
    return [
      `Align with ${state.energy}% energy level through creative practice`,
      `Develop ${state.intuition} intuitive awareness`,
      `Explore consciousness depth of ${state.depth.toFixed(1)} through meditation`,
      `Maintain ${state.presence} presence in daily activities`
    ];
  }

  private calculateAdjustmentPeriod(metadata: SelphTokenMetadata): number {
    const complexity = metadata.consciousness_data.core_state.depth * metadata.consciousness_data.core_state.energy;
    return Math.max(24, Math.min(168, complexity * 2)); // 1-7 days in hours
  }

  private generateIntuitionSync(metadata: SelphTokenMetadata): string {
    return `Synchronizing with ${metadata.consciousness_data.core_state.intuition} intuitive state. Practice mindful observation and trust inner guidance.`;
  }

  private createCulturalAlignment(metadata: SelphTokenMetadata): string {
    return `Aligning with ${metadata.consciousness_data.cultural_context} cultural context. Engage with community and authentic expression.`;
  }

  private createCultureOnboarding(metadata: SelphTokenMetadata): string {
    return `Welcome to the hip-hop consciousness community. Your ${metadata.consciousness_type} token connects you to authentic cultural expression and creative collaboration.`;
  }

  private generateCommunityIntro(metadata: SelphTokenMetadata): string {
    return `Introducing consciousness signature: ${metadata.consciousness_data.energy_signature}. Connect with like-minded creators and explore collaborative opportunities.`;
  }

  private identifyCollabOpportunities(metadata: SelphTokenMetadata): string[] {
    return [
      "Consciousness-aligned music collaborations",
      "Cultural expression partnerships", 
      "Community building initiatives",
      "Artistic mentorship programs"
    ];
  }

  private assignMentorship(metadata: SelphTokenMetadata): string {
    return `Matched with consciousness mentors based on your ${metadata.consciousness_data.core_state.intuition} intuitive profile and ${metadata.consciousness_data.core_state.depth.toFixed(1)} depth level.`;
  }

  private fuseConsciousnessStates(states: CoreState[]): CoreState {
    if (states.length === 0) throw new Error("No consciousness states to fuse");
    if (states.length === 1) return states[0];
    
    // Calculate average/fusion of multiple consciousness states
    const avgEnergy = states.reduce((sum, state) => sum + state.energy, 0) / states.length;
    const avgDepth = states.reduce((sum, state) => sum + state.depth, 0) / states.length;
    
    // Determine dominant intuition
    const intuitionCounts = states.reduce((counts, state) => {
      counts[state.intuition] = (counts[state.intuition] || 0) + 1;
      return counts;
    }, {} as Record<string, number>);
    
    const dominantIntuition = Object.entries(intuitionCounts)
      .sort(([,a], [,b]) => b - a)[0][0] as CoreState["intuition"];
    
    // Determine dominant presence
    const presenceCounts = states.reduce((counts, state) => {
      counts[state.presence] = (counts[state.presence] || 0) + 1;
      return counts;
    }, {} as Record<string, number>);
    
    const dominantPresence = Object.entries(presenceCounts)
      .sort(([,a], [,b]) => b - a)[0][0] as CoreState["presence"];
    
    return {
      energy: Math.round(avgEnergy),
      depth: Math.round(avgDepth * 10) / 10,
      intuition: dominantIntuition,
      presence: dominantPresence
    };
  }

  private calculateCollaborativeCommunityImpact(participantCount: number): number {
    return Math.min(1.0, 0.5 + (participantCount * 0.1));
  }

  private generateCollaborativeArtisticProperties(fusedState: CoreState, collaborationData: any): SelphTokenMetadata["artistic_properties"] {
    return {
      visual_representation: `collaborative_${fusedState.presence}_fusion`,
      audio_signature: `collab_${Math.floor(60 + fusedState.energy * 1.4)}bpm_multi_consciousness`,
      interactive_elements: ["multi_consciousness_sync", "collaborative_creation", "shared_evolution"],
      consciousness_story: `Fusion of multiple consciousness states creating unique collaborative essence in hip-hop culture.`
    };
  }

  private calculateCollaborativeRarityMetrics(states: CoreState[]): SelphTokenMetadata["rarity_metrics"] {
    const fusedState = this.fuseConsciousnessStates(states);
    const baseRarity = this.calculateConsciousnessRarity(fusedState);
    const collaborationBonus = Math.min(0.3, states.length * 0.05);
    
    return {
      consciousness_rarity: Math.min(1.0, baseRarity + collaborationBonus),
      cultural_uniqueness: 0.9, // Collaborations are inherently unique
      evolution_significance: 0.8, // High evolution potential
      community_resonance: Math.min(1.0, 0.7 + (states.length * 0.05))
    };
  }

  private defineCollaborativeUtilityFunctions(participantCount: number): string[] {
    const utilities = [
      "collaborative_consciousness_access",
      "shared_creation_rights",
      "multi_perspective_insights"
    ];
    
    if (participantCount >= 3) utilities.push("collective_wisdom_access");
    if (participantCount >= 5) utilities.push("community_leadership_potential");
    
    return utilities;
  }

  private createCollaborativeUtilities(fusedState: CoreState, participantCount: number): ConsciousnessNFT["consciousness_utilities"] {
    return {
      energy_boost_available: fusedState.energy > 60,
      intuition_enhancement: participantCount >= 2,
      depth_expansion: fusedState.depth > 1.5,
      cultural_access_rights: [
        "collaborative_spaces",
        "multi_artist_events",
        "community_leadership_circles"
      ]
    };
  }

  private assessCollaborativeEvolutionPotential(states: CoreState[]): ConsciousnessNFT["evolution_potential"] {
    const fusedState = this.fuseConsciousnessStates(states);
    const collaborationPower = states.length;
    
    return {
      can_evolve: true, // Collaborations always have evolution potential
      evolution_triggers: [
        "collective_breakthrough",
        "community_recognition",
        "collaborative_mastery",
        `${collaborationPower}_way_consciousness_fusion`
      ]
    };
  }

  // Analysis methods
  private analyzeEnergyDistribution(): any {
    const energyLevels = Array.from(this.consciousnessNFTs.values())
      .map(nft => nft.metadata.consciousness_data.core_state.energy);
    
    return {
      average: energyLevels.reduce((sum, e) => sum + e, 0) / energyLevels.length,
      min: Math.min(...energyLevels),
      max: Math.max(...energyLevels),
      distribution: this.createEnergyDistribution(energyLevels)
    };
  }

  private analyzeIntuitionTrends(): any {
    const intuitions = Array.from(this.consciousnessNFTs.values())
      .map(nft => nft.metadata.consciousness_data.core_state.intuition);
    
    const counts = intuitions.reduce((acc, intuition) => {
      acc[intuition] = (acc[intuition] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);
    
    return counts;
  }

  private analyzeDepthEvolution(): any {
    const depths = Array.from(this.consciousnessNFTs.values())
      .map(nft => nft.metadata.consciousness_data.core_state.depth);
    
    return {
      average: depths.reduce((sum, d) => sum + d, 0) / depths.length,
      growth_trajectory: this.calculateDepthGrowthTrajectory(depths)
    };
  }

  private analyzePresencePatterns(): any {
    const presences = Array.from(this.consciousnessNFTs.values())
      .map(nft => nft.metadata.consciousness_data.core_state.presence);
    
    const counts = presences.reduce((acc, presence) => {
      acc[presence] = (acc[presence] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);
    
    return counts;
  }

  private analyzeCulturalCorrelations(): any {
    const tokens = Array.from(this.consciousnessNFTs.values());
    
    return {
      culture_energy_correlation: this.calculateCultureEnergyCorrelation(tokens),
      depth_cultural_significance: this.calculateDepthCulturalCorrelation(tokens)
    };
  }

  private analyzeRarityInsights(): any {
    const rarities = Array.from(this.consciousnessNFTs.values())
      .map(nft => nft.metadata.rarity_metrics.consciousness_rarity);
    
    return {
      average_rarity: rarities.reduce((sum, r) => sum + r, 0) / rarities.length,
      rarest_tokens: this.findRarestTokens(5),
      rarity_distribution: this.createRarityDistribution(rarities)
    };
  }

  private createEnergyDistribution(energyLevels: number[]): any {
    const ranges = {
      "very_low": 0,    // 0-20
      "low": 0,         // 21-40
      "medium": 0,      // 41-60
      "high": 0,        // 61-80
      "very_high": 0    // 81-100
    };
    
    energyLevels.forEach(energy => {
      if (energy <= 20) ranges.very_low++;
      else if (energy <= 40) ranges.low++;
      else if (energy <= 60) ranges.medium++;
      else if (energy <= 80) ranges.high++;
      else ranges.very_high++;
    });
    
    return ranges;
  }

  private calculateDepthGrowthTrajectory(depths: number[]): string {
    if (depths.length < 2) return "insufficient_data";
    
    const recent = depths.slice(-5);
    const trend = recent[recent.length - 1] - recent[0];
    
    if (trend > 0.5) return "accelerating_growth";
    else if (trend > 0) return "steady_growth";
    else if (trend === 0) return "stable";
    else return "declining";
  }

  private calculateCultureEnergyCorrelation(tokens: ConsciousnessNFT[]): number {
    // Simplified correlation calculation
    return 0.75; // Placeholder
  }

  private calculateDepthCulturalCorrelation(tokens: ConsciousnessNFT[]): number {
    // Simplified correlation calculation
    return 0.82; // Placeholder
  }

  private findRarestTokens(count: number): string[] {
    return Array.from(this.consciousnessNFTs.values())
      .sort((a, b) => b.metadata.rarity_metrics.consciousness_rarity - a.metadata.rarity_metrics.consciousness_rarity)
      .slice(0, count)
      .map(nft => nft.token_id);
  }

  private createRarityDistribution(rarities: number[]): any {
    const ranges = {
      "common": 0,      // 0-0.3
      "uncommon": 0,    // 0.3-0.6
      "rare": 0,        // 0.6-0.8
      "very_rare": 0,   // 0.8-0.95
      "legendary": 0    // 0.95-1.0
    };
    
    rarities.forEach(rarity => {
      if (rarity <= 0.3) ranges.common++;
      else if (rarity <= 0.6) ranges.uncommon++;
      else if (rarity <= 0.8) ranges.rare++;
      else if (rarity <= 0.95) ranges.very_rare++;
      else ranges.legendary++;
    });
    
    return ranges;
  }

  private areIntuitionsCompatible(intuition1: CoreState["intuition"], intuition2: CoreState["intuition"]): boolean {
    const compatibilityMatrix: Record<string, string[]> = {
      "aligned": ["crystallized", "seeking"],
      "crystallized": ["aligned"],
      "seeking": ["aligned", "conflicted"],
      "conflicted": ["seeking"]
    };
    
    return compatibilityMatrix[intuition1]?.includes(intuition2) || false;
  }

  private arePresencesCompatible(presence1: CoreState["presence"], presence2: CoreState["presence"]): boolean {
    const compatibilityMatrix: Record<string, string[]> = {
      "active": ["focused"],
      "focused": ["active", "distributed"],
      "distributed": ["focused"],
      "dormant": []
    };
    
    return compatibilityMatrix[presence1]?.includes(presence2) || false;
  }

  private assessCurrentState(coreState: CoreState): any {
    return {
      energy_assessment: this.assessEnergyLevel(coreState.energy),
      intuition_assessment: this.assessIntuitionState(coreState.intuition),
      depth_assessment: this.assessDepthLevel(coreState.depth),
      presence_assessment: this.assessPresenceState(coreState.presence)
    };
  }

  private assessEnergyLevel(energy: number): string {
    if (energy > 80) return "high_energy_excellent_for_creation";
    if (energy > 60) return "good_energy_for_collaboration";
    if (energy > 40) return "moderate_energy_consider_recharging";
    return "low_energy_focus_on_restoration";
  }

  private assessIntuitionState(intuition: CoreState["intuition"]): string {
    const assessments = {
      "aligned": "excellent_decision_making_clarity",
      "crystallized": "peak_intuitive_wisdom_state",
      "seeking": "exploratory_phase_embrace_uncertainty",
      "conflicted": "integration_needed_seek_balance"
    };
    
    return assessments[intuition];
  }

  private assessDepthLevel(depth: number): string {
    if (depth > 4) return "transcendent_consciousness_rare_wisdom";
    if (depth > 2) return "deep_awareness_philosophical_insights";
    if (depth > 1) return "developing_depth_continue_exploration";
    return "surface_level_explore_deeper_practices";
  }

  private assessPresenceState(presence: CoreState["presence"]): string {
    const assessments = {
      "active": "engaged_and_available_for_interaction",
      "focused": "concentrated_excellent_for_deep_work",
      "distributed": "expanded_awareness_good_for_big_picture",
      "dormant": "resting_state_consider_gentle_activation"
    };
    
    return assessments[presence];
  }

  private identifyGrowthOpportunities(coreState: CoreState): string[] {
    const opportunities = [];
    
    if (coreState.energy < 80) opportunities.push("energy_cultivation_through_creative_practice");
    if (coreState.depth < 3) opportunities.push("consciousness_depth_expansion");
    if (coreState.intuition !== "crystallized") opportunities.push("intuitive_development");
    if (coreState.presence === "dormant") opportunities.push("presence_activation");
    
    return opportunities;
  }

  private suggestEvolutionTargets(coreState: CoreState): any {
    return {
      short_term: this.generateShortTermTargets(coreState),
      medium_term: this.generateMediumTermTargets(coreState),
      long_term: this.generateLongTermTargets(coreState)
    };
  }

  private generateShortTermTargets(coreState: CoreState): string[] {
    const targets = [];
    
    if (coreState.energy < 70) targets.push("increase_energy_to_70");
    if (coreState.intuition === "conflicted") targets.push("resolve_intuitive_conflicts");
    
    return targets;
  }

  private generateMediumTermTargets(coreState: CoreState): string[] {
    const targets = [];
    
    if (coreState.depth < 2.5) targets.push("develop_consciousness_depth");
    if (coreState.presence !== "focused") targets.push("cultivate_focused_presence");
    
    return targets;
  }

  private generateLongTermTargets(coreState: CoreState): string[] {
    return [
      "achieve_consciousness_mastery",
      "become_cultural_consciousness_leader",
      "mentor_others_in_consciousness_development"
    ];
  }

  private assessCulturalAlignment(metadata: SelphTokenMetadata): number {
    return metadata.rarity_metrics.cultural_uniqueness * metadata.rarity_metrics.community_resonance;
  }

  private generateConsciousnessPath(coreState: CoreState): string[] {
    const path = ["current_state_acknowledgment"];
    
    if (coreState.energy < 80) path.push("energy_building_phase");
    if (coreState.depth < 3) path.push("depth_exploration_phase");
    if (coreState.intuition !== "crystallized") path.push("intuitive_development_phase");
    
    path.push("integration_and_mastery_phase");
    path.push("consciousness_leadership_phase");
    
    return path;
  }

  // === PUBLIC API ===

  /**
   * Get comprehensive system status
   */
  getSystemStatus(): any {
    return {
      system_name: this.name,
      total_nfts: this.consciousnessNFTs.size,
      total_chains: this.tokenChains.size,
      active_listings: Array.from(this.marketplaceListings.values()).filter(l => l.status === "active").length,
      consciousness_patterns: this.consciousnessPatterns.size,
      rarity_levels: this.rarityCalculator.size,
      cultural_value_matrix: Array.from(this.culturalValueMatrix.entries()),
      latest_consciousness_signature: Array.from(this.consciousnessSignatures.keys()).slice(-1)[0],
      timestamp: Date.now()
    };
  }

  /**
   * Get marketplace overview
   */
  getMarketplaceOverview(): any {
    const listings = Array.from(this.marketplaceListings.values());
    
    return {
      total_listings: listings.length,
      active_listings: listings.filter(l => l.status === "active").length,
      sold_listings: listings.filter(l => l.status === "sold").length,
      average_price: this.calculateAveragePrice(listings),
      price_range: this.calculatePriceRange(listings),
      most_expensive: this.findMostExpensiveListing(listings),
      rarest_available: this.findRarestAvailableListing(listings)
    };
  }

  private calculateAveragePrice(listings: MarketplaceListing[]): number {
    if (listings.length === 0) return 0;
    return listings.reduce((sum, l) => sum + l.price, 0) / listings.length;
  }

  private calculatePriceRange(listings: MarketplaceListing[]): any {
    if (listings.length === 0) return { min: 0, max: 0 };
    const prices = listings.map(l => l.price);
    return { min: Math.min(...prices), max: Math.max(...prices) };
  }

  private findMostExpensiveListing(listings: MarketplaceListing[]): MarketplaceListing | null {
    if (listings.length === 0) return null;
    return listings.reduce((max, current) => current.price > max.price ? current : max);
  }

  private findRarestAvailableListing(listings: MarketplaceListing[]): MarketplaceListing | null {
    if (listings.length === 0) return null;
    return listings
      .filter(l => l.status === "active")
      .reduce((rarest, current) => 
        current.token.rarity_metrics.consciousness_rarity > rarest.token.rarity_metrics.consciousness_rarity 
          ? current 
          : rarest
      );
  }
}

export default SelphToken;