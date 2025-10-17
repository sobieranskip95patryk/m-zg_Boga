import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import Navbar from './components/Navbar'
import HomePage from './components/HomePage'
import GirlsGallery from './components/GirlsGallery'
import GirlProfile from './components/GirlProfile'
import FuelLaboratory from './components/FuelLaboratory'
import MissionControl from './components/MissionControl'
import About from './components/About'
import { rocketFuelGirls } from './data/rocketFuelGirls'

function App() {
  const [selectedGirl, setSelectedGirl] = useState(null)
  const [currentFuel, setCurrentFuel] = useState('quantum')
  const [isLoading, setIsLoading] = useState(true)
  const [cosmicTheme, setCosmicTheme] = useState('nebula')

  useEffect(() => {
    // Simulate loading time for cosmic effect
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 2000)

    return () => clearTimeout(timer)
  }, [])

  const pageVariants = {
    initial: { 
      opacity: 0, 
      y: 50,
      scale: 0.95
    },
    in: { 
      opacity: 1, 
      y: 0,
      scale: 1,
      transition: {
        duration: 0.6,
        ease: "easeOut"
      }
    },
    out: { 
      opacity: 0, 
      y: -50,
      scale: 1.05,
      transition: {
        duration: 0.4,
        ease: "easeIn"
      }
    }
  }

  const containerClass = `
    min-h-screen bg-space-gradient relative overflow-hidden
    ${cosmicTheme === 'nebula' ? 'bg-nebula-gradient' : ''}
    ${cosmicTheme === 'cosmic' ? 'bg-cosmic-gradient' : ''}
  `

  if (isLoading) {
    return (
      <div className="fixed inset-0 bg-space-gradient flex items-center justify-center z-50">
        <motion.div 
          className="text-center"
          initial={{ scale: 0.5, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 1, ease: "easeOut" }}
        >
          <motion.div 
            className="text-8xl mb-6"
            animate={{ 
              rotate: [0, 360],
              y: [0, -20, 0]
            }}
            transition={{ 
              rotate: { duration: 2, repeat: Infinity, ease: "linear" },
              y: { duration: 2, repeat: Infinity, ease: "easeInOut" }
            }}
          >
            🚀
          </motion.div>
          <motion.h1 
            className="text-4xl font-orbitron font-bold text-gradient neon-glow mb-4"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 1 }}
          >
            ROCKET FUEL GIRLS
          </motion.h1>
          <motion.p 
            className="text-lg text-cosmic-blue"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1, duration: 1 }}
          >
            Inicjalizacja galaktycznego systemu...
          </motion.p>
          <motion.div 
            className="mt-6 flex justify-center space-x-2"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.5, duration: 1 }}
          >
            {[0, 1, 2].map((i) => (
              <motion.div
                key={i}
                className="w-3 h-3 bg-cosmic-purple rounded-full"
                animate={{
                  scale: [1, 1.5, 1],
                  opacity: [0.5, 1, 0.5]
                }}
                transition={{
                  duration: 1.5,
                  repeat: Infinity,
                  delay: i * 0.2
                }}
              />
            ))}
          </motion.div>
        </motion.div>
      </div>
    )
  }

  return (
    <Router>
      <div className={containerClass}>
        {/* Cosmic Background Particles */}
        <div className="particle-bg fixed inset-0 pointer-events-none" />
        
        {/* Navigation */}
        <Navbar 
          currentTheme={cosmicTheme}
          onThemeChange={setCosmicTheme}
        />

        {/* Main Content */}
        <main className="relative z-10">
          <AnimatePresence mode="wait">
            <Routes>
              <Route 
                path="/" 
                element={
                  <motion.div
                    key="home"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <HomePage />
                  </motion.div>
                } 
              />
              
              <Route 
                path="/gallery" 
                element={
                  <motion.div
                    key="gallery"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <GirlsGallery 
                      girls={rocketFuelGirls}
                      onSelectGirl={setSelectedGirl}
                    />
                  </motion.div>
                } 
              />
              
              <Route 
                path="/girl/:id" 
                element={
                  <motion.div
                    key="profile"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <GirlProfile 
                      girl={selectedGirl}
                      girls={rocketFuelGirls}
                    />
                  </motion.div>
                } 
              />
              
              <Route 
                path="/fuel-lab" 
                element={
                  <motion.div
                    key="fuel"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <FuelLaboratory 
                      currentFuel={currentFuel}
                      onFuelChange={setCurrentFuel}
                    />
                  </motion.div>
                } 
              />
              
              <Route 
                path="/missions" 
                element={
                  <motion.div
                    key="missions"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <MissionControl girls={rocketFuelGirls} />
                  </motion.div>
                } 
              />
              
              <Route 
                path="/about" 
                element={
                  <motion.div
                    key="about"
                    variants={pageVariants}
                    initial="initial"
                    animate="in"
                    exit="out"
                  >
                    <About />
                  </motion.div>
                } 
              />
            </Routes>
          </AnimatePresence>
        </main>

        {/* Cosmic Footer */}
        <footer className="relative z-10 mt-20 py-8 text-center border-t border-cosmic-purple/20">
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1 }}
          >
            <p className="text-cosmic-blue mb-2">
              🚀 Rocket Fuel Girls © 2025 - Galaktyczne Bohaterki
            </p>
            <p className="text-sm text-gray-400">
              Powered by MTA Ecosystem & Quantum Technology
            </p>
          </motion.div>
        </footer>
      </div>
    </Router>
  )
}

export default App