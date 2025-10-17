import { motion } from 'framer-motion'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, Star, Zap, Trophy, Target, Brain, Heart, Lightning } from 'lucide-react'
import { useState, useEffect } from 'react'

const GirlProfile = ({ girls }) => {
  const { id } = useParams()
  const [girl, setGirl] = useState(null)
  const [activeTab, setActiveTab] = useState('overview')

  useEffect(() => {
    const foundGirl = girls?.find(g => g.id === id)
    setGirl(foundGirl)
  }, [id, girls])

  if (!girl) {
    return (
      <div className="container mx-auto px-6 py-20 text-center">
        <div className="text-6xl mb-4">🚀</div>
        <h2 className="text-2xl text-cosmic-blue">Ładowanie profilu bohaterki...</h2>
      </div>
    )
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

  const tabs = [
    { id: 'overview', label: 'Przegląd', icon: Star },
    { id: 'stats', label: 'Statystyki', icon: Target },
    { id: 'fuel', label: 'Paliwo', icon: Zap },
    { id: 'achievements', label: 'Osiągnięcia', icon: Trophy }
  ]

  const StatBar = ({ label, value, color, icon: Icon }) => (
    <div className="space-y-2">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Icon size={16} className={`text-${color}`} />
          <span className="text-sm text-cosmic-blue">{label}</span>
        </div>
        <span className="text-lg font-bold text-white">{value}</span>
      </div>
      <div className="w-full bg-gray-700 rounded-full h-2">
        <motion.div
          className={`h-2 rounded-full bg-${color}`}
          initial={{ width: 0 }}
          animate={{ width: `${value}%` }}
          transition={{ duration: 1.5, ease: "easeOut", delay: 0.5 }}
        />
      </div>
    </div>
  )

  return (
    <div className="container mx-auto px-6 py-8">
      {/* Back Button */}
      <motion.div
        initial={{ opacity: 0, x: -50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6 }}
        className="mb-8"
      >
        <Link 
          to="/gallery"
          className="flex items-center space-x-2 text-cosmic-blue hover:text-white transition-colors w-fit"
        >
          <ArrowLeft size={20} />
          <span>Powrót do galerii</span>
        </Link>
      </motion.div>

      {/* Main Profile */}
      <div className="grid lg:grid-cols-3 gap-8">
        {/* Left Column - Image & Basic Info */}
        <motion.div
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          className="lg:col-span-1"
        >
          {/* Profile Image */}
          <div className="cosmic-card mb-6 overflow-hidden">
            <div className="relative">
              <motion.img
                src={girl.image}
                alt={girl.name}
                className="w-full h-80 object-cover rounded-xl"
                whileHover={{ scale: 1.05 }}
                transition={{ duration: 0.5 }}
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-xl" />
              <div className="absolute bottom-4 left-4 right-4">
                <h1 className="text-3xl font-orbitron font-bold text-white neon-glow">
                  {girl.name}
                </h1>
                <p className="text-cosmic-blue font-medium">{girl.role}</p>
              </div>
            </div>
          </div>

          {/* Basic Info */}
          <div className="cosmic-card">
            <h3 className="text-xl font-bold text-gradient mb-4">Informacje Podstawowe</h3>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-cosmic-blue">Wiek:</span>
                <span className="text-white font-medium">{girl.age} lat</span>
              </div>
              <div className="flex justify-between">
                <span className="text-cosmic-blue">Planeta:</span>
                <span className="text-white font-medium">🪐 {girl.planet}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-cosmic-blue">Ranga:</span>
                <span className="text-yellow-400 font-medium">★ Legenda</span>
              </div>
            </div>
          </div>

          {/* Motto */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
            className="cosmic-card mt-6 bg-gradient-to-r from-cosmic-purple/20 to-cosmic-pink/20 border-cosmic-purple/30"
          >
            <div className="text-4xl mb-3">💭</div>
            <p className="text-white italic leading-relaxed">
              "{girl.motto}"
            </p>
          </motion.div>
        </motion.div>

        {/* Right Column - Detailed Info */}
        <motion.div
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="lg:col-span-2"
        >
          {/* Tab Navigation */}
          <div className="flex flex-wrap gap-2 mb-6">
            {tabs.map((tab) => {
              const Icon = tab.icon
              return (
                <motion.button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`
                    flex items-center space-x-2 px-4 py-2 rounded-lg font-medium transition-all
                    ${activeTab === tab.id 
                      ? 'bg-cosmic-purple text-white shadow-lg' 
                      : 'bg-white/10 text-cosmic-blue hover:bg-white/20 hover:text-white'
                    }
                  `}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Icon size={18} />
                  <span>{tab.label}</span>
                </motion.button>
              )
            })}
          </div>

          {/* Tab Content */}
          <div className="cosmic-card min-h-96">
            {activeTab === 'overview' && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <h3 className="text-2xl font-bold text-gradient mb-6">Historia Bohaterki</h3>
                <p className="text-cosmic-blue leading-relaxed text-lg mb-6">
                  {girl.story}
                </p>

                <h4 className="text-xl font-bold text-white mb-4">Umiejętności Specjalne</h4>
                <div className="grid md:grid-cols-2 gap-3">
                  {girl.skills.map((skill, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.1, duration: 0.5 }}
                      className="flex items-center space-x-3 p-3 bg-white/5 rounded-lg border border-white/10"
                    >
                      <div className="text-2xl">⚡</div>
                      <span className="text-white font-medium">{skill}</span>
                    </motion.div>
                  ))}
                </div>
              </motion.div>
            )}

            {activeTab === 'stats' && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <h3 className="text-2xl font-bold text-gradient mb-6">Statystyki Bojowe</h3>
                <div className="space-y-6">
                  <StatBar label="Moc" value={girl.stats.power} color="cosmic-red" icon={Lightning} />
                  <StatBar label="Prędkość" value={girl.stats.speed} color="cosmic-blue" icon={Zap} />
                  <StatBar label="Inteligencja" value={girl.stats.intelligence} color="cosmic-green" icon={Brain} />
                  <StatBar label="Przywództwo" value={girl.stats.leadership} color="cosmic-purple" icon={Target} />
                  <StatBar label="Kreatywność" value={girl.stats.creativity} color="cosmic-pink" icon={Heart} />
                </div>

                <div className="mt-8 grid grid-cols-2 md:grid-cols-3 gap-4">
                  <div className="text-center cosmic-card bg-cosmic-red/10 border-cosmic-red/30">
                    <div className="text-3xl font-bold text-cosmic-red">{girl.stats.power}</div>
                    <div className="text-sm text-cosmic-blue">Średnia Mocy</div>
                  </div>
                  <div className="text-center cosmic-card bg-cosmic-blue/10 border-cosmic-blue/30">
                    <div className="text-3xl font-bold text-cosmic-blue">A+</div>
                    <div className="text-sm text-cosmic-blue">Klasa</div>
                  </div>
                  <div className="text-center cosmic-card bg-cosmic-green/10 border-cosmic-green/30">
                    <div className="text-3xl font-bold text-cosmic-green">#{girl.id.split('-')[1] || '1'}</div>
                    <div className="text-sm text-cosmic-blue">Ranking</div>
                  </div>
                </div>
              </motion.div>
            )}

            {activeTab === 'fuel' && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <h3 className="text-2xl font-bold text-gradient mb-6">Specjalistyczne Paliwo</h3>
                
                <div className={`p-6 rounded-xl ${getFuelClass(girl.fuel.type)} mb-6`}>
                  <h4 className="text-2xl font-bold text-white mb-2">{girl.fuel.name}</h4>
                  <p className="text-white/90 text-lg">Typ: {girl.fuel.type.toUpperCase()}</p>
                </div>

                <div className="grid md:grid-cols-3 gap-4 mb-6">
                  <div className="cosmic-card text-center">
                    <div className="text-3xl font-bold text-cosmic-red">{girl.fuel.power}</div>
                    <div className="text-cosmic-blue">Moc (MW)</div>
                  </div>
                  <div className="cosmic-card text-center">
                    <div className="text-3xl font-bold text-cosmic-green">{girl.fuel.efficiency}%</div>
                    <div className="text-cosmic-blue">Wydajność</div>
                  </div>
                  <div className="cosmic-card text-center">
                    <div className="text-lg font-bold text-yellow-400">{girl.fuel.rarity}</div>
                    <div className="text-cosmic-blue">Rzadkość</div>
                  </div>
                </div>

                <h4 className="text-xl font-bold text-white mb-4">Właściwości Paliwa</h4>
                <div className="grid md:grid-cols-2 gap-4">
                  <div className="cosmic-card">
                    <h5 className="font-bold text-cosmic-purple mb-2">Efekty Specjalne</h5>
                    <ul className="space-y-1 text-cosmic-blue">
                      <li>• Booster energii kwantowej</li>
                      <li>• Stabilizacja czasoprzestrzeni</li>
                      <li>• Wzmocnienie ochrony</li>
                    </ul>
                  </div>
                  <div className="cosmic-card">
                    <h5 className="font-bold text-cosmic-purple mb-2">Zastosowanie</h5>
                    <ul className="space-y-1 text-cosmic-blue">
                      <li>• Podróże międzygalaktyczne</li>
                      <li>• Systemy obronne</li>
                      <li>• Laboratoria badawcze</li>
                    </ul>
                  </div>
                </div>
              </motion.div>
            )}

            {activeTab === 'achievements' && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <h3 className="text-2xl font-bold text-gradient mb-6">Osiągnięcia i Nagrody</h3>
                
                <div className="space-y-4">
                  {girl.achievements.map((achievement, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, x: -30 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.2, duration: 0.6 }}
                      className="flex items-start space-x-4 p-4 cosmic-card bg-gradient-to-r from-cosmic-purple/10 to-transparent border-cosmic-purple/30"
                    >
                      <div className="text-3xl">🏆</div>
                      <div>
                        <h4 className="font-bold text-white mb-1">{achievement}</h4>
                        <p className="text-cosmic-blue text-sm">
                          Prestiżowe osiągnięcie galaktyczne
                        </p>
                      </div>
                    </motion.div>
                  ))}
                </div>

                <div className="mt-8 p-6 cosmic-card bg-gradient-to-r from-yellow-400/10 to-orange-400/10 border-yellow-400/30">
                  <div className="flex items-center space-x-3 mb-3">
                    <div className="text-3xl">⭐</div>
                    <h4 className="text-xl font-bold text-yellow-400">Status Legendy</h4>
                  </div>
                  <p className="text-cosmic-blue leading-relaxed">
                    {girl.name} została oficjalnie uznana za Legendę Galaktyczną przez Wysoką Radę Kosmiczną 
                    za swoje niezwykłe osiągnięcia w dziedzinie eksploracji kosmosu i rozwoju technologii paliwowych.
                  </p>
                </div>
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default GirlProfile