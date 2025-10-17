import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { Star, Zap, Award } from 'lucide-react'

const GirlsGallery = ({ girls, onSelectGirl }) => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  }

  const cardVariants = {
    hidden: { 
      opacity: 0, 
      y: 50,
      scale: 0.8
    },
    visible: { 
      opacity: 1, 
      y: 0,
      scale: 1,
      transition: {
        duration: 0.6,
        ease: "easeOut"
      }
    }
  }

  const getFuelClass = (fuelType) => {
    const fuelClasses = {
      quantum: 'fuel-quantum',
      stellar: 'fuel-stellar',
      dark: 'fuel-dark',
      nebular: 'fuel-nebular',
      aurora: 'fuel-aurora',
      warp: 'fuel-warp'
    }
    return fuelClasses[fuelType] || 'fuel-quantum'
  }

  const getRarityColor = (rarity) => {
    const rarityColors = {
      'Legendary': 'text-yellow-400',
      'Mythical': 'text-purple-400',
      'Epic': 'text-blue-400',
      'Rare': 'text-green-400'
    }
    return rarityColors[rarity] || 'text-gray-400'
  }

  return (
    <div className="container mx-auto px-6 py-20">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-center mb-16"
      >
        <h1 className="text-5xl md:text-6xl font-orbitron font-bold text-gradient neon-glow mb-6">
          GALERIA BOHATEREK
        </h1>
        <p className="text-xl text-cosmic-blue max-w-3xl mx-auto leading-relaxed">
          Poznaj sześć niezwykłych wojowniczek kosmicznych, z których każda posiada unikalne umiejętności 
          i kontroluje różne rodzaje galaktycznych paliw. Kliknij na kartę, aby poznać pełną historię!
        </p>
      </motion.div>

      {/* Girls Grid */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="grid md:grid-cols-2 lg:grid-cols-3 gap-8"
      >
        {girls.map((girl, index) => (
          <motion.div
            key={girl.id}
            variants={cardVariants}
            whileHover={{ 
              scale: 1.05, 
              y: -10,
              transition: { duration: 0.3 }
            }}
            className="group"
          >
            <Link 
              to={`/girl/${girl.id}`}
              onClick={() => onSelectGirl(girl)}
              className="block"
            >
              <div className="cosmic-card overflow-hidden bg-gradient-to-br from-space-medium/50 to-space-dark/50 border-2 border-transparent hover:border-cosmic-purple/50 transition-all duration-300">
                {/* Image Container */}
                <div className="relative overflow-hidden rounded-xl mb-4">
                  <motion.img
                    src={girl.image}
                    alt={girl.name}
                    className="w-full h-64 object-cover group-hover:scale-110 transition-transform duration-500"
                    whileHover={{ filter: "brightness(1.1)" }}
                  />
                  
                  {/* Fuel Type Badge */}
                  <div className={`absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-bold ${getFuelClass(girl.fuel.type)} flex items-center space-x-1`}>
                    <Zap size={12} />
                    <span>{girl.fuel.name}</span>
                  </div>
                  
                  {/* Rarity Badge */}
                  <div className={`absolute top-3 left-3 flex items-center space-x-1 ${getRarityColor(girl.fuel.rarity)}`}>
                    <Star size={12} fill="currentColor" />
                    <span className="text-xs font-bold">{girl.fuel.rarity}</span>
                  </div>

                  {/* Hover Overlay */}
                  <motion.div
                    className="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end"
                    initial={{ opacity: 0 }}
                    whileHover={{ opacity: 1 }}
                  >
                    <p className="text-white text-sm p-4 leading-relaxed">
                      {girl.story.substring(0, 120)}...
                    </p>
                  </motion.div>
                </div>

                {/* Card Content */}
                <div className="space-y-4">
                  {/* Name & Role */}
                  <div>
                    <h3 className="text-2xl font-orbitron font-bold text-white group-hover:text-gradient transition-all duration-300">
                      {girl.name}
                    </h3>
                    <p className="text-cosmic-blue font-medium">{girl.role}</p>
                    <p className="text-sm text-gray-400">🪐 {girl.planet}</p>
                  </div>

                  {/* Stats Preview */}
                  <div className="grid grid-cols-3 gap-2 text-center">
                    <div className="bg-white/5 rounded-lg p-2">
                      <div className="text-lg font-bold text-cosmic-red">{girl.stats.power}</div>
                      <div className="text-xs text-gray-400">Moc</div>
                    </div>
                    <div className="bg-white/5 rounded-lg p-2">
                      <div className="text-lg font-bold text-cosmic-blue">{girl.stats.speed}</div>
                      <div className="text-xs text-gray-400">Prędkość</div>
                    </div>
                    <div className="bg-white/5 rounded-lg p-2">
                      <div className="text-lg font-bold text-cosmic-green">{girl.stats.intelligence}</div>
                      <div className="text-xs text-gray-400">Inteligencja</div>
                    </div>
                  </div>

                  {/* Fuel Info */}
                  <div className="bg-gradient-to-r from-white/5 to-transparent rounded-lg p-3 border border-white/10">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm font-medium text-cosmic-blue">Paliwo:</span>
                      <span className="text-sm font-bold text-white">{girl.fuel.power} MW</span>
                    </div>
                    <div className="w-full bg-gray-700 rounded-full h-2">
                      <motion.div
                        className={`h-2 rounded-full ${getFuelClass(girl.fuel.type)}`}
                        initial={{ width: 0 }}
                        animate={{ width: `${girl.fuel.efficiency}%` }}
                        transition={{ delay: index * 0.2, duration: 1.5, ease: "easeOut" }}
                      />
                    </div>
                    <div className="text-xs text-gray-400 mt-1">
                      Wydajność: {girl.fuel.efficiency}%
                    </div>
                  </div>

                  {/* Top Skills */}
                  <div>
                    <p className="text-sm text-cosmic-blue mb-2">Najlepsze umiejętności:</p>
                    <div className="flex flex-wrap gap-1">
                      {girl.skills.slice(0, 2).map((skill, skillIndex) => (
                        <span
                          key={skillIndex}
                          className="px-2 py-1 bg-cosmic-purple/20 text-cosmic-purple text-xs rounded-full border border-cosmic-purple/30"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Action Button */}
                  <motion.div
                    className="pt-2"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    <div className="w-full bg-gradient-to-r from-cosmic-purple to-cosmic-pink py-3 rounded-lg text-center font-bold text-white group-hover:shadow-lg group-hover:shadow-cosmic-purple/30 transition-all duration-300">
                      Poznaj Bohaterkę
                    </div>
                  </motion.div>
                </div>
              </div>
            </Link>
          </motion.div>
        ))}
      </motion.div>

      {/* Bottom Info */}
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1, duration: 0.8 }}
        className="text-center mt-20"
      >
        <div className="cosmic-card max-w-2xl mx-auto bg-gradient-to-r from-cosmic-purple/10 to-cosmic-pink/10 border-cosmic-purple/20">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <Award className="text-cosmic-purple" size={24} />
            <h3 className="text-xl font-bold text-gradient">Legenda Galaktyki</h3>
          </div>
          <p className="text-cosmic-blue leading-relaxed">
            Te sześć bohaterek razem uratowało galaktykę przed zagładą, każda wnoszając swoje unikalne 
            umiejętności i kosmiczne paliwa. Ich historia jest legendą opowiadaną w całym wszechświecie!
          </p>
        </div>
      </motion.div>
    </div>
  )
}

export default GirlsGallery