import axios from 'axios';

export async function queryGrok(query: string, token: string) {
  try {
    const response = await axios.post(
      'https://api.x.ai/grok',
      { query },
      {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      }
    );
    return response.data;
  } catch (e) {
    throw new Error(`xAI API error: ${e.message}`);
  }
}

// Mock dla testów
export const mockGrok = async (query: string) => {
  return {
    response: `Mock response for query: ${query}`,
    timestamp: new Date().toISOString(),
  };
};
