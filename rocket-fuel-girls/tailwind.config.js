/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        cosmic: {
          purple: '#6c5ce7',
          pink: '#fd79a8',
          blue: '#4ecdc4',
          green: '#00b894',
          orange: '#fdcb6e',
          red: '#ff6b6b'
        },
        space: {
          dark: '#0d0d1a',
          medium: '#1a1a33',
          light: '#2d2d4a'
        }
      },
      fontFamily: {
        'orbitron': ['Orbitron', 'monospace'],
        'space': ['Space Grotesk', 'sans-serif']
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite alternate',
        'cosmic-spin': 'cosmic-spin 20s linear infinite',
        'warp-speed': 'warp-speed 0.5s ease-out'
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' }
        },
        'pulse-glow': {
          '0%': { boxShadow: '0 0 20px rgba(108, 92, 231, 0.5)' },
          '100%': { boxShadow: '0 0 40px rgba(108, 92, 231, 0.8)' }
        },
        'cosmic-spin': {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' }
        },
        'warp-speed': {
          '0%': { transform: 'scale(0.8) translateY(50px)', opacity: '0' },
          '100%': { transform: 'scale(1) translateY(0)', opacity: '1' }
        }
      },
      backgroundImage: {
        'cosmic-gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'space-gradient': 'linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%)',
        'nebula-gradient': 'radial-gradient(ellipse at center, #fd79a8 0%, #6c5ce7 70%, #0d0d1a 100%)'
      }
    },
  },
  plugins: [],
}