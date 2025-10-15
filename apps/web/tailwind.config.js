/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          purple: '#8B5CF6',
          pink: '#EC4899',
          blue: '#3B82F6',
        },
        dark: {
          bg: '#0F0F0F',
          card: '#1A1A1A',
          border: '#333333',
        },
      },
      backgroundImage: {
        'gradient-main': 'linear-gradient(135deg, #8B5CF6, #EC4899, #3B82F6)',
        'gradient-card': 'linear-gradient(135deg, #1A1A1A, #2D2D2D)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'bounce-slow': 'bounce 2s infinite',
      },
    },
  },
  plugins: [],
}