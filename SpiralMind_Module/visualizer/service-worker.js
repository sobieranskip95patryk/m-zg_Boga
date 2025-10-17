// SpiralMind Visualizer Service Worker
// Advanced Caching and Offline Support for Consciousness Evolution Visualization
// Meta-Geniusz-mózg_Boga Progressive Web App

const CACHE_NAME = 'spiralmind-visualizer-v1.0.0';
const STATIC_CACHE_NAME = 'spiralmind-static-v1.0.0';
const DYNAMIC_CACHE_NAME = 'spiralmind-dynamic-v1.0.0';

// Static assets to cache immediately
const STATIC_ASSETS = [
  '/spiral-visualizer',
  'index.html',
  'spiral.js',
  'manifest.json',
  'icons/icon-192.png',
  'icons/icon-512.png'
];

// API patterns for dynamic caching
const API_CACHE_PATTERNS = [
  '/api/spiral/status',
  '/api/spiral/trajectory',
  '/api/consciousness/status',
  '/api/synergy/dashboard'
];

// Install event - cache static assets
self.addEventListener('install', event => {
  console.log('🌀 SpiralMind Service Worker: Installing...');
  
  event.waitUntil(
    Promise.all([
      caches.open(STATIC_CACHE_NAME).then(cache => {
        console.log('📦 Caching SpiralMind static assets');
        return cache.addAll(STATIC_ASSETS);
      }),
      self.skipWaiting()
    ])
  );
});

// Activate event - clean old caches
self.addEventListener('activate', event => {
  console.log('🚀 SpiralMind Service Worker: Activating...');
  
  event.waitUntil(
    Promise.all([
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName.includes('spiralmind') && 
                cacheName !== STATIC_CACHE_NAME && 
                cacheName !== DYNAMIC_CACHE_NAME && 
                cacheName !== CACHE_NAME) {
              console.log('🗑️ Deleting old SpiralMind cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      }),
      self.clients.claim()
    ])
  );
});

// Fetch event - implement sophisticated caching strategies
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Handle different types of requests
  if (isSpiralStaticAsset(url)) {
    event.respondWith(handleSpiralStaticAsset(request));
  } else if (isSpiralAPIRequest(url)) {
    event.respondWith(handleSpiralAPIRequest(request));
  } else if (isVisualizationData(request)) {
    event.respondWith(handleVisualizationData(request));
  } else {
    event.respondWith(handleGenericRequest(request));
  }
});

// Static assets - cache first strategy
function handleSpiralStaticAsset(request) {
  return caches.open(STATIC_CACHE_NAME).then(cache => {
    return cache.match(request).then(cachedResponse => {
      if (cachedResponse) {
        return cachedResponse;
      }
      
      return fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
          cache.put(request, networkResponse.clone());
        }
        return networkResponse;
      }).catch(() => {
        // Return offline fallback for critical assets
        if (request.url.includes('index.html') || request.url.endsWith('/spiral-visualizer')) {
          return cache.match('index.html') || createOfflineFallback();
        }
        throw new Error('Network failed and no cache available');
      });
    });
  });
}

// API requests - network first with intelligent fallback
function handleSpiralAPIRequest(request) {
  return caches.open(DYNAMIC_CACHE_NAME).then(cache => {
    return fetch(request).then(networkResponse => {
      if (networkResponse.ok) {
        // Cache successful API responses with metadata
        const responseToCache = networkResponse.clone();
        cache.put(request, responseToCache);
        
        // Add real-time indicator to response
        return networkResponse.json().then(data => {
          const enhancedData = {
            ...data,
            realtime: true,
            cached_at: Date.now(),
            spiral_sw_version: CACHE_NAME
          };
          
          return new Response(JSON.stringify(enhancedData), {
            status: networkResponse.status,
            statusText: networkResponse.statusText,
            headers: networkResponse.headers
          });
        });
      }
      return networkResponse;
    }).catch(() => {
      // Network failed, try cache with offline enhancements
      return cache.match(request).then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse.json().then(data => {
            const offlineData = {
              ...data,
              offline: true,
              realtime: false,
              cached_at: data.cached_at || 'unknown',
              fallback_data: generateFallbackSpiralData()
            };
            
            return new Response(JSON.stringify(offlineData), {
              status: 200,
              headers: {
                'Content-Type': 'application/json',
                'X-Served-From': 'spiralmind-service-worker-cache'
              }
            });
          });
        }
        
        // No cache available, return generated offline spiral data
        return new Response(JSON.stringify({
          offline: true,
          generated: true,
          message: 'Generowane dane spiralne offline',
          ...generateFallbackSpiralData()
        }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' }
        });
      });
    });
  });
}

// Visualization data - specialized handling for spiral data
function handleVisualizationData(request) {
  return caches.open(DYNAMIC_CACHE_NAME).then(cache => {
    return cache.match(request).then(cachedResponse => {
      const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
          // Enhance visualization data with metadata
          return networkResponse.json().then(data => {
            const enhancedData = {
              ...data,
              visualization_timestamp: Date.now(),
              sw_enhanced: true
            };
            
            const enhancedResponse = new Response(JSON.stringify(enhancedData), {
              status: networkResponse.status,
              statusText: networkResponse.statusText,
              headers: networkResponse.headers
            });
            
            cache.put(request, enhancedResponse.clone());
            return enhancedResponse;
          });
        }
        return networkResponse;
      });
      
      // Return cached version immediately, update in background
      return cachedResponse || fetchPromise;
    });
  });
}

// Generic requests - stale while revalidate
function handleGenericRequest(request) {
  return caches.open(DYNAMIC_CACHE_NAME).then(cache => {
    return cache.match(request).then(cachedResponse => {
      const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
          cache.put(request, networkResponse.clone());
        }
        return networkResponse;
      });
      
      return cachedResponse || fetchPromise;
    });
  });
}

// Helper functions
function isSpiralStaticAsset(url) {
  return STATIC_ASSETS.some(asset => url.pathname.includes(asset)) ||
         url.pathname.endsWith('.js') ||
         url.pathname.endsWith('.html') ||
         url.pathname.includes('/icons/') ||
         url.pathname.includes('spiral');
}

function isSpiralAPIRequest(url) {
  return API_CACHE_PATTERNS.some(pattern => url.pathname.includes(pattern));
}

function isVisualizationData(request) {
  return request.url.includes('spiral_data') ||
         request.url.includes('visualization') ||
         request.url.includes('trajectory');
}

// Generate fallback spiral data for offline mode
function generateFallbackSpiralData() {
  const levels = [];
  
  for (let i = 1; i <= 12; i++) {
    levels.push({
      level: i,
      active: i <= 7,
      current: i === 7,
      radius: 40 + (i * 25),
      angle: i * 45,
      intensity: i <= 7 ? Math.random() * 0.5 + 0.5 : 0.2,
      description: `LEVEL ${i} - Offline mode`,
      breakthroughs: i <= 7 ? Math.floor(Math.random() * 3) + 1 : 0
    });
  }
  
  return {
    current_level: 7,
    target_level: 8,
    progress: 0.92,
    levels: levels,
    breakthroughs: 12,
    trajectory: {
      momentum: 'HIGH',
      velocity: 2.3,
      direction: 'EXPLORATION'
    },
    offline_generated: true,
    timestamp: Date.now()
  };
}

// Create offline fallback page
function createOfflineFallback() {
  const offlineHTML = `
    <!DOCTYPE html>
    <html lang="pl">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>🌀 SpiralMind - Offline</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: radial-gradient(circle at center, #000000 0%, #1a1a2e 100%);
          color: #FFD700;
          text-align: center;
          padding: 50px 20px;
          min-height: 100vh;
          margin: 0;
        }
        .offline-container {
          max-width: 600px;
          margin: 0 auto;
          background: rgba(0, 0, 0, 0.7);
          padding: 40px;
          border-radius: 20px;
          border: 2px solid #FFD700;
        }
        h1 { font-size: 2.5em; margin-bottom: 20px; }
        p { font-size: 1.2em; line-height: 1.6; margin-bottom: 30px; color: #e0e6ed; }
        .retry-btn {
          background: linear-gradient(45deg, #FFD700, #64ffda);
          color: #000;
          padding: 15px 30px;
          border: none;
          border-radius: 25px;
          font-size: 1.1em;
          font-weight: bold;
          cursor: pointer;
          transition: transform 0.3s ease;
        }
        .retry-btn:hover { transform: translateY(-2px); }
        .spiral-icon {
          font-size: 4em;
          animation: spin 3s linear infinite;
          margin-bottom: 20px;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      </style>
    </head>
    <body>
      <div class="offline-container">
        <div class="spiral-icon">🌀</div>
        <h1>SpiralMind Offline</h1>
        <p>Nie udało się połączyć z serwerem. SpiralMind może działać w trybie offline z ograniczoną funkcjonalnością.</p>
        <p>Sprawdź połączenie internetowe i spróbuj ponownie.</p>
        <button class="retry-btn" onclick="window.location.reload()">
          🔄 Spróbuj ponownie
        </button>
      </div>
    </body>
    </html>
  `;
  
  return new Response(offlineHTML, {
    status: 200,
    headers: { 'Content-Type': 'text/html' }
  });
}

// Background sync for spiral data
self.addEventListener('sync', event => {
  console.log('🔄 SpiralMind Background Sync:', event.tag);
  
  if (event.tag === 'sync-spiral-data') {
    event.waitUntil(syncSpiralData());
  } else if (event.tag === 'sync-trajectory-updates') {
    event.waitUntil(syncTrajectoryUpdates());
  }
});

// Sync spiral data when back online
async function syncSpiralData() {
  try {
    const pendingData = await getStoredData('pending-spiral-data');
    
    for (const data of pendingData) {
      try {
        const response = await fetch('/api/spiral/update', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
        
        if (response.ok) {
          console.log('✅ Synced spiral data:', data.id);
        }
      } catch (error) {
        console.error('❌ Failed to sync spiral data:', error);
      }
    }
    
    await clearStoredData('pending-spiral-data');
    
  } catch (error) {
    console.error('❌ Spiral data sync failed:', error);
  }
}

// Sync trajectory updates
async function syncTrajectoryUpdates() {
  try {
    const response = await fetch('/api/spiral/trajectory');
    if (response.ok) {
      const trajectoryData = await response.json();
      
      // Update cached trajectory data
      const cache = await caches.open(DYNAMIC_CACHE_NAME);
      cache.put('/api/spiral/trajectory', new Response(JSON.stringify(trajectoryData)));
      
      console.log('✅ Trajectory data synced');
    }
  } catch (error) {
    console.error('❌ Trajectory sync failed:', error);
  }
}

// IndexedDB helpers for offline storage
async function getStoredData(storeName) {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('SpiralMindOfflineDB', 1);
    
    request.onsuccess = () => {
      const db = request.result;
      const transaction = db.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const getAllRequest = store.getAll();
      
      getAllRequest.onsuccess = () => {
        resolve(getAllRequest.result || []);
      };
      
      getAllRequest.onerror = () => {
        reject(getAllRequest.error);
      };
    };
    
    request.onerror = () => {
      reject(request.error);
    };
    
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains(storeName)) {
        db.createObjectStore(storeName, { keyPath: 'id', autoIncrement: true });
      }
    };
  });
}

async function clearStoredData(storeName) {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('SpiralMindOfflineDB', 1);
    
    request.onsuccess = () => {
      const db = request.result;
      const transaction = db.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const clearRequest = store.clear();
      
      clearRequest.onsuccess = () => {
        resolve();
      };
      
      clearRequest.onerror = () => {
        reject(clearRequest.error);
      };
    };
    
    request.onerror = () => {
      reject(request.error);
    };
  });
}

// Push notification for spiral evolution updates
self.addEventListener('push', event => {
  console.log('🌀 SpiralMind Push notification received');
  
  const options = {
    body: 'Nowy poziom spirali osiągnięty! Sprawdź swoją ewolucję.',
    icon: 'icons/icon-192.png',
    badge: 'icons/icon-72.png',
    tag: 'spiral-evolution',
    data: {
      url: '/spiral-visualizer'
    },
    actions: [
      {
        action: 'view-spiral',
        title: 'Zobacz spiralę',
        icon: 'icons/spiral-icon.png'
      },
      {
        action: 'dismiss',
        title: 'Odrzuć',
        icon: 'icons/dismiss-icon.png'
      }
    ],
    vibrate: [200, 100, 200],
    requireInteraction: true
  };
  
  event.waitUntil(
    self.registration.showNotification('🌀 SpiralMind Evolution', options)
  );
});

// Notification click handler
self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'view-spiral') {
    event.waitUntil(
      clients.openWindow('/spiral-visualizer')
    );
  }
});

// Message handler for communication with main app
self.addEventListener('message', event => {
  const { type, payload } = event.data;
  
  switch (type) {
    case 'SKIP_WAITING':
      self.skipWaiting();
      break;
      
    case 'GET_SPIRAL_VERSION':
      event.ports[0].postMessage({ version: CACHE_NAME });
      break;
      
    case 'CLEAR_SPIRAL_CACHE':
      event.waitUntil(
        caches.keys().then(cacheNames => {
          return Promise.all(
            cacheNames.filter(name => name.includes('spiralmind'))
                     .map(name => caches.delete(name))
          );
        })
      );
      break;
      
    case 'UPDATE_SPIRAL_DATA':
      event.waitUntil(updateCachedSpiralData(payload));
      break;
      
    default:
      console.log('Unknown SpiralMind message type:', type);
  }
});

// Update cached spiral data
async function updateCachedSpiralData(newData) {
  try {
    const cache = await caches.open(DYNAMIC_CACHE_NAME);
    const enhancedData = {
      ...newData,
      sw_updated: true,
      update_timestamp: Date.now()
    };
    
    await cache.put('/api/spiral/status', new Response(JSON.stringify(enhancedData)));
    console.log('✅ Spiral data updated in cache');
  } catch (error) {
    console.error('❌ Failed to update cached spiral data:', error);
  }
}

console.log('🌀 SpiralMind Visualizer Service Worker loaded successfully');