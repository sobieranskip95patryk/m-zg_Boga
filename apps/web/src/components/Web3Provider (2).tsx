'use client';

import { WagmiConfig, createConfig, configureChains } from 'wagmi';
import { polygon, polygonMumbai } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';
import { RainbowKitProvider, getDefaultWallets, connectorsForWallets } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';

const { chains, publicClient, webSocketPublicClient } = configureChains(
  [
    process.env.NEXT_PUBLIC_NETWORK === 'polygon' ? polygon : polygonMumbai,
  ],
  [publicProvider()]
);

const projectId = process.env.NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID || 'demo';

const { wallets } = getDefaultWallets({
  appName: 'Hip-Hop Universe',
  projectId,
  chains,
});

const connectors = connectorsForWallets([
  ...wallets,
]);

const wagmiConfig = createConfig({
  autoConnect: true,
  connectors,
  publicClient,
  webSocketPublicClient,
});

interface Web3ProviderProps {
  children: React.ReactNode;
}

export function Web3Provider({ children }: Web3ProviderProps) {
  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider 
        chains={chains}
        theme="dark"
        showRecentTransactions={true}
      >
        {children}
      </RainbowKitProvider>
    </WagmiConfig>
  );
}