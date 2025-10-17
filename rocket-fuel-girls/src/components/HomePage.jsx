import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { ArrowRight, Sparkles, Rocket, Fuel } from 'lucide-react'

const HomePage = () => {
  const features = [
    {
      icon: '👩‍🚀',
      title: '6 Unikalnych Bohaterek',
      description: 'Poznaj galaktyczne wojowniczki z unikalnymi umiejętnościami',
      color: 'cosmic-purple'
    },
    {
      icon: '⚡',
      title: 'Paliwa Kosmiczne',
      description: 'Odkryj różne rodzaje paliw i ich magiczne właściwości',
      color: 'cosmic-blue'
    },
    {
      icon: '🎯',
      title: 'Epické Misje',
      description: 'Wyrusz na przygody w najbardziej odległe zakątki galaktyki',
      color: 'cosmic-red'
    },
    {
      icon: '✨',
      title: 'Interaktywne Doświadczenia',
      description: 'Zanurz się w świecie pełnym animacji i kosmicznych efektów',
      color: 'cosmic-green'
    }
  ]

  const stats = [
    { value: '6', label: 'Bohaterek', icon: '👩‍🚀' },
    { value: '12+', label: 'Rodzajów Paliw', icon: '⚡' },
    { value: '∞', label: 'Przygód', icon: '🌌' },
    { value: '99%', label: 'Epicości', icon: '🚀' }
  ]

  return (
    <div className="relative">
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center px-6 overflow-hidden">
        {/* Animated Background Elements */}
        <div className="absolute inset-0">
          {[...Array(20)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute rounded-full bg-white/10"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
                width: `${Math.random() * 4 + 1}px`,
                height: `${Math.random() * 4 + 1}px`,
              }}
              animate={{
                y: [0, -30, 0],
                opacity: [0.3, 1, 0.3],
              }}
              transition={{
                duration: Math.random() * 3 + 2,
                repeat: Infinity,
                delay: Math.random() * 2,
              }}
            />
          ))}
        </div>

        <div className="text-center z-10 max-w-4xl">
          <motion.div
            initial={{ scale: 0, rotate: -180 }}
            animate={{ scale: 1, rotate: 0 }}
            transition={{ duration: 1, ease: "easeOut" }}
            className="mb-8"
          >
            <div className="text-8xl md:text-9xl mb-4">🚀</div>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
            className="text-5xl md:text-7xl font-orbitron font-black text-gradient neon-glow mb-6"
          >
            ROCKET FUEL GIRLS
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8, duration: 0.8 }}
            className="text-xl md:text-2xl text-cosmic-blue mb-8 leading-relaxed"
          >
            Dołącz do elitarnego zespołu galaktycznych bohaterek,<br />
            które zarządzają najpotężniejszymi paliwami wszechświata!
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 1.1, duration: 0.8 }}
            className="flex flex-col sm:flex-row gap-4 justify-center"
          >
            <Link to="/gallery">
              <motion.button
                className="group px-8 py-4 bg-gradient-to-r from-cosmic-purple to-cosmic-pink rounded-xl font-bold text-white shadow-lg hover:shadow-cosmic-purple/50 transition-all duration-300 flex items-center space-x-2"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                <span>Poznaj Bohaterki</span>
                <ArrowRight className="group-hover:translate-x-1 transition-transform" size={20} />
              </motion.button>
            </Link>

            <Link to="/fuel-lab">
              <motion.button
                className="group px-8 py-4 bg-white/10 backdrop-blur-lg rounded-xl font-bold text-white border border-white/20 hover:bg-white/20 transition-all duration-300 flex items-center space-x-2"
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
              >
                <Fuel size={20} />
                <span>Laboratorium Paliw</span>
              </motion.button>
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 px-6">
        <div className="container mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="grid grid-cols-2 md:grid-cols-4 gap-8"
          >
            {stats.map((stat, index) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, scale: 0.5 }}
                whileInView={{ opacity: 1, scale: 1 }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
                viewport={{ once: true }}
                className="text-center cosmic-card"
              >
                <div className="text-4xl mb-2">{stat.icon}</div>
                <div className="text-3xl font-bold text-gradient mb-1">{stat.value}</div>
                <div className="text-cosmic-blue">{stat.label}</div>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-6">
        <div className="container mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl md:text-5xl font-orbitron font-bold text-gradient mb-6">
              Galaktyczne Możliwości
            </h2>
            <p className="text-xl text-cosmic-blue max-w-2xl mx-auto">
              Odkryj niesamowity świat kosmicznych przygód i poznaj bohaterki, które zmieniły historię galaktyki
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={feature.title}
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1, duration: 0.6 }}
                viewport={{ once: true }}
                className="cosmic-card text-center group hover:scale-105 transition-all duration-300"
              >
                <div className="text-5xl mb-4 group-hover:animate-bounce">{feature.icon}</div>
                <h3 className="text-xl font-bold text-white mb-3 group-hover:text-gradient transition-all">
                  {feature.title}
                </h3>
                <p className="text-cosmic-blue group-hover:text-white transition-colors">
                  {feature.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-6">
        <div className="container mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            whileInView={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
            className="cosmic-card max-w-4xl mx-auto bg-gradient-to-r from-cosmic-purple/20 to-cosmic-pink/20 border-cosmic-purple/30"
          >
            <div className="text-6xl mb-6">🌌</div>
            <h2 className="text-3xl md:text-4xl font-orbitron font-bold text-gradient mb-6">
              Gotowa na Galaktyczną Przygodę?
            </h2>
            <p className="text-lg text-cosmic-blue mb-8 max-w-2xl mx-auto">
              Rozpocznij swoją podróż z Rocket Fuel Girls już dziś! Odkryj sekrety kosmicznych paliw 
              i poznaj najbardziej niezwykłe bohaterki galaktyki.
            </p>
            <Link to="/gallery">
              <motion.button
                className="group px-10 py-5 bg-gradient-to-r from-cosmic-purple to-cosmic-pink rounded-xl font-bold text-white text-lg shadow-lg hover:shadow-cosmic-purple/50 transition-all duration-300 flex items-center space-x-3 mx-auto"
                whileHover={{ scale: 1.05, y: -3 }}
                whileTap={{ scale: 0.95 }}
              >
                <Sparkles className="group-hover:animate-spin" size={24} />
                <span>Zacznij Przygodę</span>
                <Rocket className="group-hover:translate-x-2 transition-transform" size={24} />
              </motion.button>
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  )
}

export default HomePage