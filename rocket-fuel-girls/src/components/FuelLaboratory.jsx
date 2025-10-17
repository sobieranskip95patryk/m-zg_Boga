import { motion } from 'framer-motion'
import { useState } from 'react'
import { Flame, Zap, Star, Beaker, Settings, Play } from 'lucide-react'
import { fuelTypes } from '../data/rocketFuelGirls'

const FuelLaboratory = ({ currentFuel, onFuelChange }) => {
  const [selectedFuel, setSelectedFuel] = useState('quantum')
  const [isExperimenting, setIsExperimenting] = useState(false)
  const [experimentResult, setExperimentResult] = useState(null)

  const fuelData = {
    quantum: {
      name: 'Quantum Plasma',
      color: '#ff6b6b',
      power: 9500,
      efficiency: 98,
      stability: 87,
      effects: ['Reality Warp', 'Teleportation', 'Time Dilation'],
      description: 'Najzaawansowane paliwo manipulujące rzeczywistością na poziomie kwantowym'
    },
    stellar: {
      name: 'Stellar Wind',
      color: '#4ecdc4',
      power: 8800,
      efficiency: 94,
      stability: 91,
      effects: ['Solar Boost', 'Navigation Enhancement', 'Cosmic Communication'],
      description: 'Energia pochodząca bezpośrednio z wiatrów gwiezdnych'
    },
    dark: {
      name: 'Dark Energy',
      color: '#6c5ce7',
      power: 9200,
      efficiency: 91,
      stability: 89,
      effects: ['Stealth Mode', 'Phase Shift', 'Shadow Strike'],
      description: 'Tajemnicza energia ciemnej materii wszechświata'
    },
    nebular: {
      name: 'Nebula Essence',
      color: '#fd79a8',
      power: 8600,
      efficiency: 96,
      stability: 93,
      effects: ['Dream State', 'Crystallization', 'Essence Synthesis'],
      description: 'Esencja mgławic przekształcona w czyste paliwo'
    },
    aurora: {
      name: 'Aurora Plasma',
      color: '#00b894',
      power: 9100,
      efficiency: 93,
      stability: 88,
      effects: ['Light Show', 'Energy Conductor', 'Plasma Burst'],
      description: 'Plazma auroralna o spektakularnych właściwościach świetlnych'
    },
    warp: {
      name: 'Warp Fuel',
      color: '#fdcb6e',
      power: 9800,
      efficiency: 89,
      stability: 85,
      effects: ['Warp Drive', 'Time Acceleration', 'Space Folding'],
      description: 'Paliwo umożliwiające podróże nadświetlne'
    }
  }

  const runExperiment = () => {
    setIsExperimenting(true)
    setExperimentResult(null)
    
    setTimeout(() => {
      const fuel = fuelData[selectedFuel]
      const success = Math.random() > 0.3 // 70% szans na sukces
      const powerBoost = Math.floor(Math.random() * 500) + 100
      
      setExperimentResult({
        success,
        fuel: fuel.name,
        powerBoost: success ? powerBoost : 0,
        message: success 
          ? `Eksperyment udany! Zwiększono moc o ${powerBoost} MW!`
          : 'Eksperyment nieudany. Spróbuj ponownie z innymi parametrami.'
      })
      setIsExperimenting(false)
    }, 3000)
  }

  const ProgressBar = ({ value, color }) => (
    <div className="w-full bg-gray-700 rounded-full h-3">
      <motion.div
        className="h-3 rounded-full"
        style={{ backgroundColor: color }}
        initial={{ width: 0 }}
        animate={{ width: `${value}%` }}
        transition={{ duration: 1.5, ease: "easeOut" }}
      />
    </div>
  )

  const fuel = fuelData[selectedFuel]

  return (
    <div className="container mx-auto px-6 py-20">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-center mb-16"
      >
        <div className="text-6xl mb-4">🧪</div>
        <h1 className="text-5xl md:text-6xl font-orbitron font-bold text-gradient neon-glow mb-6">
          LABORATORIUM PALIW
        </h1>
        <p className="text-xl text-cosmic-blue max-w-3xl mx-auto">
          Eksperymentuj z różnymi rodzajami kosmicznych paliw, badaj ich właściwości 
          i odkrywaj nowe możliwości energetyczne!
        </p>
      </motion.div>

      <div className="grid lg:grid-cols-3 gap-8">
        {/* Fuel Selection */}
        <motion.div
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          className="lg:col-span-1"
        >
          <div className="cosmic-card">
            <h3 className="text-xl font-bold text-gradient mb-6 flex items-center space-x-2">
              <Flame size={24} />
              <span>Wybierz Paliwo</span>
            </h3>
            
            <div className="space-y-3">
              {Object.entries(fuelData).map(([key, fuel]) => (
                <motion.button
                  key={key}
                  onClick={() => setSelectedFuel(key)}
                  className={`
                    w-full p-4 rounded-xl transition-all duration-300 text-left
                    ${selectedFuel === key 
                      ? 'bg-white/20 border-2 border-white/50 shadow-lg' 
                      : 'bg-white/5 border border-white/20 hover:bg-white/10'
                    }
                  `}
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  <div className="flex items-center space-x-3">
                    <div 
                      className="w-4 h-4 rounded-full"
                      style={{ backgroundColor: fuel.color }}
                    />
                    <div>
                      <div className="font-bold text-white">{fuel.name}</div>
                      <div className="text-sm text-cosmic-blue">{fuel.power} MW</div>
                    </div>
                  </div>
                </motion.button>
              ))}
            </div>
          </div>

          {/* Experiment Controls */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
            className="cosmic-card mt-6"
          >
            <h3 className="text-xl font-bold text-gradient mb-6 flex items-center space-x-2">
              <Beaker size={24} />
              <span>Kontrola Eksperymentu</span>
            </h3>
            
            <motion.button
              onClick={runExperiment}
              disabled={isExperimenting}
              className={`
                w-full py-4 rounded-xl font-bold text-white transition-all duration-300 flex items-center justify-center space-x-2
                ${isExperimenting 
                  ? 'bg-gray-600 cursor-not-allowed' 
                  : 'bg-gradient-to-r from-cosmic-purple to-cosmic-pink hover:shadow-lg hover:shadow-cosmic-purple/50'
                }
              `}
              whileHover={!isExperimenting ? { scale: 1.05 } : {}}
              whileTap={!isExperimenting ? { scale: 0.95 } : {}}
            >
              {isExperimenting ? (
                <>
                  <motion.div
                    className="w-5 h-5 border-2 border-white border-t-transparent rounded-full"
                    animate={{ rotate: 360 }}
                    transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                  />
                  <span>Eksperyment w toku...</span>
                </>
              ) : (
                <>
                  <Play size={20} />
                  <span>Rozpocznij Eksperyment</span>
                </>
              )}
            </motion.button>

            {experimentResult && (
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5 }}
                className={`
                  mt-4 p-4 rounded-xl
                  ${experimentResult.success 
                    ? 'bg-green-500/20 border border-green-500/50' 
                    : 'bg-red-500/20 border border-red-500/50'
                  }
                `}
              >
                <div className="text-center">
                  <div className="text-2xl mb-2">
                    {experimentResult.success ? '✅' : '❌'}
                  </div>
                  <p className="text-white font-medium">
                    {experimentResult.message}
                  </p>
                </div>
              </motion.div>
            )}
          </motion.div>
        </motion.div>

        {/* Fuel Analysis */}
        <motion.div
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="lg:col-span-2"
        >
          <div className="cosmic-card">
            <h3 className="text-2xl font-bold text-gradient mb-6 flex items-center space-x-2">
              <Settings size={28} />
              <span>Analiza Paliwa: {fuel.name}</span>
            </h3>

            {/* Fuel Visualization */}
            <div className="mb-8">
              <motion.div
                className="relative h-40 rounded-xl overflow-hidden"
                style={{ 
                  background: `linear-gradient(135deg, ${fuel.color}40, ${fuel.color}20)`,
                  border: `2px solid ${fuel.color}60`
                }}
                animate={{
                  boxShadow: [
                    `0 0 20px ${fuel.color}40`,
                    `0 0 40px ${fuel.color}60`,
                    `0 0 20px ${fuel.color}40`
                  ]
                }}
                transition={{ duration: 2, repeat: Infinity }}
              >
                <div className="absolute inset-0 flex items-center justify-center">
                  <motion.div
                    className="text-6xl"
                    animate={{ 
                      rotate: [0, 360],
                      scale: [1, 1.1, 1]
                    }}
                    transition={{ 
                      rotate: { duration: 4, repeat: Infinity, ease: "linear" },
                      scale: { duration: 2, repeat: Infinity }
                    }}
                  >
                    ⚛️
                  </motion.div>
                </div>
                
                {/* Particle effects */}
                {[...Array(10)].map((_, i) => (
                  <motion.div
                    key={i}
                    className="absolute w-2 h-2 rounded-full"
                    style={{ backgroundColor: fuel.color }}
                    initial={{
                      x: Math.random() * 300,
                      y: Math.random() * 100,
                      opacity: 0.5
                    }}
                    animate={{
                      x: Math.random() * 300,
                      y: Math.random() * 100,
                      opacity: [0.5, 1, 0.5]
                    }}
                    transition={{
                      duration: Math.random() * 3 + 2,
                      repeat: Infinity,
                      ease: "linear"
                    }}
                  />
                ))}
              </motion.div>
            </div>

            {/* Fuel Stats */}
            <div className="grid md:grid-cols-3 gap-6 mb-8">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-cosmic-blue">Moc</span>
                  <span className="text-white font-bold">{fuel.power} MW</span>
                </div>
                <ProgressBar value={(fuel.power / 10000) * 100} color={fuel.color} />
              </div>
              
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-cosmic-blue">Wydajność</span>
                  <span className="text-white font-bold">{fuel.efficiency}%</span>
                </div>
                <ProgressBar value={fuel.efficiency} color={fuel.color} />
              </div>
              
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-cosmic-blue">Stabilność</span>
                  <span className="text-white font-bold">{fuel.stability}%</span>
                </div>
                <ProgressBar value={fuel.stability} color={fuel.color} />
              </div>
            </div>

            {/* Description */}
            <div className="mb-6">
              <h4 className="text-lg font-bold text-white mb-3">Opis</h4>
              <p className="text-cosmic-blue leading-relaxed">{fuel.description}</p>
            </div>

            {/* Effects */}
            <div>
              <h4 className="text-lg font-bold text-white mb-3">Efekty Specjalne</h4>
              <div className="grid md:grid-cols-3 gap-3">
                {fuel.effects.map((effect, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1, duration: 0.5 }}
                    className="p-3 bg-white/5 rounded-lg border border-white/10 text-center"
                  >
                    <div className="text-2xl mb-1">✨</div>
                    <div className="text-white font-medium text-sm">{effect}</div>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default FuelLaboratory