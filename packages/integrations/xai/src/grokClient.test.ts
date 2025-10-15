describe('grokQuery (mock)', () => {
import { queryGrok, mockGrok } from './grokClient';

describe('xAI Integration', () => {
  it('should return mock response', async () => {
    const response = await mockGrok('test query');
    expect(response.response).toContain('Mock response for query: test query');
    expect(response.timestamp).toBeDefined();
  });

  it('should fail on invalid xAI API call', async () => {
    await expect(queryGrok('test', 'invalid-token')).rejects.toThrow('xAI API error');
  });
});
