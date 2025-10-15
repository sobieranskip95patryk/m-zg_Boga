'use client';

import { useAccount, useBalance, useContractRead } from 'wagmi';
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { formatEther } from 'ethers/lib/utils';
import { DRT_TOKEN_ABI } from '../lib/contracts';

export function WalletInfo() {
  const { address, isConnected } = useAccount();
  
  const { data: balance } = useBalance({
    address,
  });
  
  const { data: drtBalance } = useContractRead({
    address: process.env.NEXT_PUBLIC_DRT_TOKEN_ADDRESS as `0x${string}`,
    abi: DRT_TOKEN_ABI,
    functionName: 'balanceOf',
    args: [address],
    enabled: !!address,
  });
  
  const { data: drtName } = useContractRead({
    address: process.env.NEXT_PUBLIC_DRT_TOKEN_ADDRESS as `0x${string}`,
    abi: DRT_TOKEN_ABI,
    functionName: 'name',
  });
  
  const { data: drtSymbol } = useContractRead({
    address: process.env.NEXT_PUBLIC_DRT_TOKEN_ADDRESS as `0x${string}`,
    abi: DRT_TOKEN_ABI,
    functionName: 'symbol',
  });

  if (!isConnected) {
    return (
      <div className="card text-center">
        <h3 className="text-xl font-semibold mb-4">Connect Your Wallet</h3>
        <p className="text-gray-300 mb-6">
          Connect your wallet to interact with Hip-Hop Universe smart contracts
        </p>
        <ConnectButton />
      </div>
    );
  }

  return (
    <div className="card">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-xl font-semibold">Wallet Info</h3>
        <ConnectButton />
      </div>
      
      <div className="space-y-4">
        <div className="flex justify-between">
          <span className="text-gray-300">Address:</span>
          <span className="font-mono text-sm">
            {address?.slice(0, 6)}...{address?.slice(-4)}
          </span>
        </div>
        
        <div className="flex justify-between">
          <span className="text-gray-300">
            {process.env.NEXT_PUBLIC_NETWORK === 'polygon' ? 'MATIC' : 'Test MATIC'}:
          </span>
          <span className="font-semibold">
            {balance ? parseFloat(formatEther(balance.value)).toFixed(4) : '0.0000'}
          </span>
        </div>
        
        {drtBalance && (
          <div className="flex justify-between">
            <span className="text-gray-300">{drtSymbol || 'DRT'}:</span>
            <span className="font-semibold gradient-text">
              {parseFloat(formatEther(drtBalance)).toFixed(2)}
            </span>
          </div>
        )}
        
        <div className="pt-4 border-t border-gray-600">
          <div className="text-xs text-gray-400">
            Network: {process.env.NEXT_PUBLIC_NETWORK === 'polygon' ? 'Polygon' : 'Mumbai Testnet'}
          </div>
          {drtName && (
            <div className="text-xs text-gray-400">
              Token: {drtName} ({drtSymbol})
            </div>
          )}
        </div>
      </div>
    </div>
  );
}