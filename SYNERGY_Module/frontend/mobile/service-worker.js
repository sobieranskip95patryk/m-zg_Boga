// SYNERGY Mobile PWA Service Worker
// Meta-Geniusz-mózg_Boga Mobile Offline Support
// MTAQuestWebsideX.com - Advanced Caching Strategy

const CACHE_NAME = 'synergy-mobile-v1.2.0';
const STATIC_CACHE_NAME = 'synergy-static-v1.2.0';
const DYNAMIC_CACHE_NAME = 'synergy-dynamic-v1.2.0';

// Files to cache immediately
const STATIC_ASSETS = [
  '/synergy-mobile',
  'index.html',
  'style.css',
  'app.js',
  'manifest.json',
  'icons/icon-192.png',
  'icons/icon-512.png'
];

// API endpoints to cache
const API_CACHE_PATTERNS = [
  '/api/synergy/dashboard',
  '/api/synergy/voting-status',
  '/api/consciousness/status',
  '/api/spiral/status',
  '/api/globalvision/status'
];

// Cache strategies
const CACHE_STRATEGIES = {
  static: 'cache-first',
  api: 'network-first',
  images: 'cache-first',
  dynamic: 'stale-while-revalidate'
};

// Install event - cache static assets
self.addEventListener('install', event => {
  console.log('🔧 Service Worker: Installing...');
  
  event.waitUntil(
    Promise.all([
      // Cache static assets
      caches.open(STATIC_CACHE_NAME).then(cache => {
        console.log('📦 Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      }),
      
      // Skip waiting to activate immediately
      self.skipWaiting()
    ])
  );
});

// Activate event - clean old caches
self.addEventListener('activate', event => {
  console.log('🚀 Service Worker: Activating...');
  
  event.waitUntil(
    Promise.all([
      // Clean old caches
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== STATIC_CACHE_NAME && 
                cacheName !== DYNAMIC_CACHE_NAME && 
                cacheName !== CACHE_NAME) {
              console.log('🗑️ Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      }),
      
      // Take control of all clients
      self.clients.claim()
    ])
  );
});

// Fetch event - implement caching strategies
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Handle different types of requests
  if (isStaticAsset(url)) {
    event.respondWith(handleStaticAsset(request));
  } else if (isAPIRequest(url)) {
    event.respondWith(handleAPIRequest(request));
  } else if (isImageRequest(request)) {
    event.respondWith(handleImageRequest(request));
  } else {
    event.respondWith(handleDynamicRequest(request));
  }
});

// Static assets - cache first strategy
function handleStaticAsset(request) {
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
        if (request.url.includes('index.html') || request.url.endsWith('/synergy-mobile')) {
          return cache.match('index.html');
        }
        throw new Error('Network failed and no cache available');
      });
    });
  });
}

// API requests - network first with offline fallback
function handleAPIRequest(request) {
  return caches.open(DYNAMIC_CACHE_NAME).then(cache => {
    return fetch(request).then(networkResponse => {
      if (networkResponse.ok) {
        // Cache successful API responses
        cache.put(request, networkResponse.clone());
        
        // Add timestamp to response headers
        const responseWithTimestamp = new Response(networkResponse.body, {
          status: networkResponse.status,
          statusText: networkResponse.statusText,
          headers: {
            ...networkResponse.headers,
            'sw-cache-timestamp': Date.now()
          }
        });
        
        return responseWithTimestamp;
      }
      return networkResponse;
    }).catch(() => {
      // Network failed, try cache
      return cache.match(request).then(cachedResponse => {
        if (cachedResponse) {
          // Add offline indicator to cached response
          const offlineResponse = cachedResponse.clone();
          return offlineResponse.json().then(data => {
            const offlineData = {
              ...data,
              offline: true,
              cached_at: cachedResponse.headers.get('sw-cache-timestamp') || 'unknown'
            };
            
            return new Response(JSON.stringify(offlineData), {
              status: 200,
              headers: {
                'Content-Type': 'application/json',
                'X-Served-From': 'service-worker-cache'
              }
            });
          });
        }
        
        // No cache available, return minimal offline data
        return new Response(JSON.stringify({
          error: 'Offline - no cached data available',
          offline: true,
          message: 'Brak połączenia z internetem i brak danych w cache'
        }), {
          status: 503,
          headers: { 'Content-Type': 'application/json' }
        });
      });
    });
  });
}

// Images - cache first strategy
function handleImageRequest(request) {
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
      });
    });
  });
}

// Dynamic requests - stale while revalidate
function handleDynamicRequest(request) {
  return caches.open(DYNAMIC_CACHE_NAME).then(cache => {
    return cache.match(request).then(cachedResponse => {
      const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
          cache.put(request, networkResponse.clone());
        }
        return networkResponse;
      });
      
      // Return cached version immediately, update in background
      return cachedResponse || fetchPromise;
    });
  });
}

// Helper functions
function isStaticAsset(url) {
  return STATIC_ASSETS.some(asset => url.pathname.includes(asset)) ||
         url.pathname.endsWith('.css') ||
         url.pathname.endsWith('.js') ||
         url.pathname.endsWith('.html') ||
         url.pathname.includes('/icons/');
}

function isAPIRequest(url) {
  return url.pathname.startsWith('/api/') ||
         API_CACHE_PATTERNS.some(pattern => url.pathname.includes(pattern));
}

function isImageRequest(request) {
  return request.destination === 'image' ||
         request.url.includes('.png') ||
         request.url.includes('.jpg') ||
         request.url.includes('.jpeg') ||
         request.url.includes('.svg') ||
         request.url.includes('.gif') ||
         request.url.includes('.webp');
}

// Background sync for offline actions
self.addEventListener('sync', event => {
  console.log('🔄 Background Sync:', event.tag);
  
  if (event.tag === 'sync-corrections') {
    event.waitUntil(syncPendingCorrections());
  } else if (event.tag === 'sync-votes') {
    event.waitUntil(syncPendingVotes());
  }
});

// Sync pending corrections when back online
async function syncPendingCorrections() {
  try {
    const pendingCorrections = await getStoredData('pending-corrections');
    
    for (const correction of pendingCorrections) {
      try {
        const response = await fetch('/api/synergy/apply-correction', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(correction)
        });
        
        if (response.ok) {
          console.log('✅ Synced correction:', correction.id);
        }
      } catch (error) {
        console.error('❌ Failed to sync correction:', error);
      }
    }
    
    // Clear synced corrections
    await clearStoredData('pending-corrections');
    
  } catch (error) {
    console.error('❌ Background sync failed:', error);
  }
}

// Sync pending votes when back online
async function syncPendingVotes() {
  try {
    const pendingVotes = await getStoredData('pending-votes');
    
    for (const vote of pendingVotes) {
      try {
        const response = await fetch('/api/synergy/vote', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(vote)
        });
        
        if (response.ok) {
          console.log('✅ Synced vote:', vote.id);
        }
      } catch (error) {
        console.error('❌ Failed to sync vote:', error);
      }
    }
    
    // Clear synced votes
    await clearStoredData('pending-votes');
    
  } catch (error) {
    console.error('❌ Vote sync failed:', error);
  }
}

// IndexedDB helpers for offline storage
async function getStoredData(storeName) {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('SynergyOfflineDB', 1);
    
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
    const request = indexedDB.open('SynergyOfflineDB', 1);
    
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

// Push notification handler
self.addEventListener('push', event => {
  console.log('📱 Push notification received');
  
  const options = {
    body: 'Nowa decyzja SYNERGY dostępna',
    icon: 'icons/icon-192.png',
    badge: 'icons/icon-72.png',
    tag: 'synergy-update',
    data: {
      url: '/synergy-mobile'
    },
    actions: [
      {
        action: 'view',
        title: 'Zobacz',
        icon: 'icons/view-icon.png'
      },
      {
        action: 'dismiss',
        title: 'Odrzuć',
        icon: 'icons/dismiss-icon.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('🧠 SYNERGY Update', options)
  );
});

// Notification click handler
self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'view') {
    event.waitUntil(
      clients.openWindow('/synergy-mobile')
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
      
    case 'GET_VERSION':
      event.ports[0].postMessage({ version: CACHE_NAME });
      break;
      
    case 'CLEAR_CACHE':
      event.waitUntil(
        caches.keys().then(cacheNames => {
          return Promise.all(
            cacheNames.map(cacheName => caches.delete(cacheName))
          );
        })
      );
      break;
      
    default:
      console.log('Unknown message type:', type);
  }
});

console.log('🚀 SYNERGY Mobile Service Worker loaded successfully');