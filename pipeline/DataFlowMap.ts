/**
 * DataFlowMap.ts
 * Mapa przepływu danych - dokumentacyjny schemat w kodzie.
 */
export const DataFlowMap = {
  inputs: ['sensors', 'network', 'user'],
  stages: ['ingest', 'intuit', 'decide', 'act', 'archive'],
  outputs: ['intent', 'telemetry', 'logs']
} as const;
