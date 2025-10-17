import { motion } from 'framer-motion'
import { useState, useEffect } from 'react'
import { 
  Rocket, 
  Star, 
  Target, 
  Clock, 
  MapPin, 
  Users, 
  Zap,
  Award,
  AlertTriangle,
  CheckCircle
} from 'lucide-react'
import { rocketFuelGirls } from '../data/rocketFuelGirls'

const MissionControl = () => {
  const [activeMission, setActiveMission] = useState(null)
  const [missionStatus, setMissionStatus] = useState('standby')
  const [countdown, setCountdown] = useState(0)
  const [selectedGirl, setSelectedGirl] = useState(null)

  const missions = [
    {
      id: 1,
      name: 'Nebula Explorer',
      objective: 'Zbadaj tajemniczą mgławicę Andromedae',
      difficulty: 'Medium',
      duration: '2 godziny',
      rewards: ['5000 XP', 'Nebula Crystal', 'Explorer Badge'],
      requirements: {
        minLevel: 15,
        fuelType: 'stellar',
        skills: ['Navigation', 'Analysis']
      },
      location: 'Mgławica Andromedae',
      status: 'available'
    },
    {
      id: 2,
      name: 'Quantum Rescue',
      objective: 'Uratuj załogę uwięzioną w anomalii kwantowej',
      difficulty: 'Hard',
      duration: '3 godziny',
      rewards: ['10000 XP', 'Quantum Core', 'Hero Medal'],
      requirements: {
        minLevel: 25,
        fuelType: 'quantum',
        skills: ['Combat', 'Quantum Physics']
      },
      location: 'Sektor Q-7',
      status: 'urgent'
    },
    {
      id: 3,
      name: 'Stellar Race Championship',
      objective: 'Wygraj mistrzostwa wyścigów międzygalaktycznych',
      difficulty: 'Extreme',
      duration: '4 godziny',
      rewards: ['20000 XP', 'Champion Trophy', 'Speed Boost'],
      requirements: {
        minLevel: 30,
        fuelType: 'warp',
        skills: ['Racing', 'Navigation']
      },
      location: 'Arena Gwiezdna',
      status: 'available'
    },
    {
      id: 4,
      name: 'Dark Matter Investigation',
      objective: 'Zbadaj źródło tajemniczej ciemnej materii',
      difficulty: 'Medium',
      duration: '2.5 godziny',
      rewards: ['7500 XP', 'Dark Essence', 'Researcher Badge'],
      requirements: {
        minLevel: 20,
        fuelType: 'dark',
        skills: ['Science', 'Stealth']
      },
      location: 'Void Sector',
      status: 'available'
    }
  ]

  const startMission = (mission) => {
    if (!selectedGirl) {
      alert('Wybierz najpierw Rocket Fuel Girl!')
      return
    }
    
    setActiveMission(mission)
    setMissionStatus('launching')
    setCountdown(10)
  }

  useEffect(() => {
    if (countdown > 0 && missionStatus === 'launching') {
      const timer = setTimeout(() => setCountdown(countdown - 1), 1000)
      return () => clearTimeout(timer)
    } else if (countdown === 0 && missionStatus === 'launching') {
      setMissionStatus('in-progress')
      // Simulate mission completion after some time
      setTimeout(() => {
        setMissionStatus('completed')
      }, 5000)
    }
  }, [countdown, missionStatus])

  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'Easy': return '#00b894'
      case 'Medium': return '#fdcb6e'
      case 'Hard': return '#fd79a8'
      case 'Extreme': return '#e17055'
      default: return '#6c5ce7'
    }
  }

  const getStatusIcon = (status) => {
    switch (status) {
      case 'available': return <CheckCircle size={20} className="text-green-400" />
      case 'urgent': return <AlertTriangle size={20} className="text-red-400" />
      default: return <Clock size={20} className="text-yellow-400" />
    }
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
        <div className="text-6xl mb-4">🚀</div>
        <h1 className="text-5xl md:text-6xl font-orbitron font-bold text-gradient neon-glow mb-6">
          CENTRUM DOWODZENIA
        </h1>
        <p className="text-xl text-cosmic-blue max-w-3xl mx-auto">
          Zarządzaj misjami, śledź postępy swojej załogi i koordynuj operacje w całej galaktyce!
        </p>
      </motion.div>

      <div className="grid lg:grid-cols-3 gap-8">
        {/* Girl Selection */}
        <motion.div
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          className="lg:col-span-1"
        >
          <div className="cosmic-card">
            <h3 className="text-xl font-bold text-gradient mb-6 flex items-center space-x-2">
              <Users size={24} />
              <span>Wybierz Pilota</span>
            </h3>
            
            <div className="space-y-3">
              {rocketFuelGirls.map((girl) => (
                <motion.button
                  key={girl.id}
                  onClick={() => setSelectedGirl(girl)}
                  className={`
                    w-full p-4 rounded-xl transition-all duration-300 text-left
                    ${selectedGirl?.id === girl.id 
                      ? 'bg-white/20 border-2 border-white/50 shadow-lg' 
                      : 'bg-white/5 border border-white/20 hover:bg-white/10'
                    }
                  `}
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  <div className="flex items-center space-x-3">
                    <div className="text-2xl">{girl.emoji}</div>
                    <div>
                      <div className="font-bold text-white">{girl.name}</div>
                      <div className="text-sm text-cosmic-blue">
                        Level {girl.level} • {girl.speciality}
                      </div>
                    </div>
                  </div>
                </motion.button>
              ))}
            </div>
          </div>

          {/* Mission Status */}
          {activeMission && (
            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5 }}
              className="cosmic-card mt-6"
            >
              <h3 className="text-xl font-bold text-gradient mb-4 flex items-center space-x-2">
                <Rocket size={24} />
                <span>Status Misji</span>
              </h3>
              
              <div className="space-y-4">
                <div>
                  <div className="font-bold text-white">{activeMission.name}</div>
                  <div className="text-sm text-cosmic-blue">{activeMission.objective}</div>
                </div>
                
                {missionStatus === 'launching' && (
                  <div className="text-center">
                    <motion.div
                      className="text-4xl font-bold text-cosmic-pink mb-2"
                      animate={{ scale: [1, 1.2, 1] }}
                      transition={{ duration: 1, repeat: Infinity }}
                    >
                      {countdown}
                    </motion.div>
                    <div className="text-cosmic-blue">Start za...</div>
                  </div>
                )}
                
                {missionStatus === 'in-progress' && (
                  <div className="text-center">
                    <motion.div
                      className="w-8 h-8 mx-auto mb-2 border-4 border-cosmic-purple border-t-transparent rounded-full"
                      animate={{ rotate: 360 }}
                      transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                    />
                    <div className="text-cosmic-blue">Misja w toku...</div>
                  </div>
                )}
                
                {missionStatus === 'completed' && (
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    className="text-center"
                  >
                    <div className="text-4xl mb-2">🎉</div>
                    <div className="text-green-400 font-bold">Misja Zakończona!</div>
                    <button
                      onClick={() => {
                        setActiveMission(null)
                        setMissionStatus('standby')
                      }}
                      className="mt-2 px-4 py-2 bg-cosmic-purple rounded-lg text-white hover:bg-cosmic-purple/80 transition-colors"
                    >
                      Nowa Misja
                    </button>
                  </motion.div>
                )}
              </div>
            </motion.div>
          )}
        </motion.div>

        {/* Available Missions */}
        <motion.div
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="lg:col-span-2"
        >
          <div className="cosmic-card">
            <h3 className="text-2xl font-bold text-gradient mb-6 flex items-center space-x-2">
              <Target size={28} />
              <span>Dostępne Misje</span>
            </h3>

            <div className="space-y-6">
              {missions.map((mission, index) => (
                <motion.div
                  key={mission.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1, duration: 0.5 }}
                  className="border border-white/20 rounded-xl p-6 bg-white/5 hover:bg-white/10 transition-all duration-300"
                >
                  <div className="flex justify-between items-start mb-4">
                    <div>
                      <div className="flex items-center space-x-3 mb-2">
                        {getStatusIcon(mission.status)}
                        <h4 className="text-xl font-bold text-white">{mission.name}</h4>
                        <div
                          className="px-3 py-1 rounded-full text-xs font-bold text-white"
                          style={{ backgroundColor: getDifficultyColor(mission.difficulty) }}
                        >
                          {mission.difficulty}
                        </div>
                      </div>
                      <p className="text-cosmic-blue mb-3">{mission.objective}</p>
                    </div>
                  </div>

                  <div className="grid md:grid-cols-3 gap-4 mb-4">
                    <div className="flex items-center space-x-2">
                      <Clock size={16} className="text-cosmic-blue" />
                      <span className="text-sm text-white">{mission.duration}</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <MapPin size={16} className="text-cosmic-blue" />
                      <span className="text-sm text-white">{mission.location}</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <Star size={16} className="text-cosmic-blue" />
                      <span className="text-sm text-white">Level {mission.requirements.minLevel}+</span>
                    </div>
                  </div>

                  <div className="mb-4">
                    <div className="text-sm text-cosmic-blue mb-2">Nagrody:</div>
                    <div className="flex flex-wrap gap-2">
                      {mission.rewards.map((reward, i) => (
                        <span
                          key={i}
                          className="px-2 py-1 bg-cosmic-purple/30 rounded-lg text-xs text-white"
                        >
                          {reward}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div className="mb-4">
                    <div className="text-sm text-cosmic-blue mb-2">Wymagania:</div>
                    <div className="flex flex-wrap gap-2">
                      <span className="px-2 py-1 bg-cosmic-pink/30 rounded-lg text-xs text-white">
                        {mission.requirements.fuelType} fuel
                      </span>
                      {mission.requirements.skills.map((skill, i) => (
                        <span
                          key={i}
                          className="px-2 py-1 bg-cosmic-blue/30 rounded-lg text-xs text-white"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>

                  <motion.button
                    onClick={() => startMission(mission)}
                    disabled={!selectedGirl || activeMission}
                    className={`
                      w-full py-3 rounded-xl font-bold transition-all duration-300 flex items-center justify-center space-x-2
                      ${!selectedGirl || activeMission
                        ? 'bg-gray-600 text-gray-400 cursor-not-allowed'
                        : 'bg-gradient-to-r from-cosmic-purple to-cosmic-pink text-white hover:shadow-lg hover:shadow-cosmic-purple/50'
                      }
                    `}
                    whileHover={!selectedGirl || activeMission ? {} : { scale: 1.02 }}
                    whileTap={!selectedGirl || activeMission ? {} : { scale: 0.98 }}
                  >
                    <Rocket size={20} />
                    <span>
                      {!selectedGirl 
                        ? 'Wybierz pilota' 
                        : activeMission 
                        ? 'Misja w toku' 
                        : 'Rozpocznij misję'
                      }
                    </span>
                  </motion.button>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default MissionControl