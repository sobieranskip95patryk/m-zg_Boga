const express = require('express');
const router = express.Router();
const fetch = require('node-fetch');

// Generate AI metadata for NFT
router.post('/generate-metadata', async (req, res) => {
  try {
    const { title, artist, mood, genre, extras } = req.body || {};
    
    if (!title || !artist) {
      return res.status(400).json({ error: 'Title and artist are required' });
    }

    console.log('🤖 Generating AI metadata for:', { title, artist, mood, genre });

    const prompt = `Create a detailed JSON metadata for a Hip-Hop music NFT with the following details:
Title: ${title}
Artist: ${artist}
Mood: ${mood || 'energetic'}
Genre: ${genre || 'hip-hop'}
Additional info: ${extras || 'none'}

Return only valid JSON with these fields:
- name: the track title
- description: creative 2-3 sentence description capturing the vibe
- image: placeholder URL "ipfs://QmPlaceholder"
- attributes: array with trait_type and value pairs for mood, genre, style
- external_url: placeholder "https://hiphopuniverse.io/track/{id}"

Make it authentic to hip-hop culture and engaging.`;

    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      // Fallback to rule-based generation
      console.log('⚠️ OpenAI API key not found, using fallback generation');
      const fallbackMetadata = {
        name: title,
        description: `${title} by ${artist} - A powerful ${mood || 'energetic'} ${genre || 'hip-hop'} track that captures the essence of the culture.`,
        image: "ipfs://QmPlaceholder",
        attributes: [
          { trait_type: "Artist", value: artist },
          { trait_type: "Mood", value: mood || "energetic" },
          { trait_type: "Genre", value: genre || "hip-hop" },
          { trait_type: "Style", value: "conscious rap" }
        ],
        external_url: `https://hiphopuniverse.io/track/${Date.now()}`
      };
      return res.json({ success: true, metadata: fallbackMetadata, source: 'fallback' });
    }

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages: [{ role: "user", content: prompt }],
        max_tokens: 500,
        temperature: 0.8
      })
    });

    if (!response.ok) {
      throw new Error(`OpenAI API error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    const aiText = data?.choices?.[0]?.message?.content || '';
    
    // Parse AI response
    let metadata;
    try {
      // Clean up the response - remove markdown code blocks if present
      const cleanText = aiText.replace(/```json\n?|\n?```/g, '').trim();
      metadata = JSON.parse(cleanText);
    } catch (parseError) {
      console.log('⚠️ Failed to parse AI response, using fallback');
      metadata = {
        name: title,
        description: `${title} by ${artist} - Generated with AI assistance`,
        image: "ipfs://QmPlaceholder",
        attributes: [
          { trait_type: "Artist", value: artist },
          { trait_type: "Mood", value: mood || "creative" },
          { trait_type: "Genre", value: genre || "hip-hop" }
        ],
        raw_ai_response: aiText
      };
    }

    console.log('✅ AI metadata generated successfully');
    res.json({ 
      success: true, 
      metadata: metadata,
      source: 'openai',
      tokens_used: data?.usage?.total_tokens
    });

  } catch (error) {
    console.error('❌ AI generation failed:', error);
    res.status(500).json({ 
      error: error.message,
      fallback_available: true
    });
  }
});

// Generate album artwork description
router.post('/generate-artwork', async (req, res) => {
  try {
    const { title, artist, mood, style } = req.body;
    
    const prompt = `Create a detailed description for album artwork for a hip-hop track:
Title: ${title}
Artist: ${artist}
Mood: ${mood}
Style: ${style}

Describe visual elements, colors, themes, and artistic style in 2-3 sentences.`;

    // Simple fallback for artwork descriptions
    const artworkDescription = `Vibrant ${mood || 'dynamic'} artwork featuring bold typography for "${title}" with ${style || 'street art'} influences. Rich color palette combining urban aesthetics with modern design elements that reflect ${artist}'s artistic vision.`;

    res.json({
      success: true,
      artwork_description: artworkDescription,
      suggested_colors: ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
      style_elements: ['typography', 'urban', 'modern', 'vibrant']
    });

  } catch (error) {
    console.error('❌ Artwork generation failed:', error);
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;