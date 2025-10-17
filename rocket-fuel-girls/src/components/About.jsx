import { motion } from 'framer-motion'
import { Heart, Code, Rocket, Star, Users, Zap } from 'lucide-react'

const About = () => {
  const features = [
    {
      icon: <Users size={32} />,
      title: 'Galaktyczne Bohaterki',
      description: 'Poznaj 6 niesamowitych Rocket Fuel Girls, każda z unikalnymi umiejętnościami i historią'
    },
    {
      icon: <Zap size={32} />,
      title: 'System Paliw',
      description: 'Eksperymentuj z różnymi rodzajami kosmicznych paliw i odkrywaj ich właściwości'
    },
    {
      icon: <Rocket size={32} />,
      title: 'Centrum Misji',
      description: 'Zarządzaj misjami, śledź postępy i koordynuj operacje w całej galaktyce'
    },
    {
      icon: <Star size={32} />,
      title: 'Animacje Cosmic',
      description: 'Ciesz się płynnymi animacjami i efektami wizualnymi w stylu kosmicznym'
    }
  ]

  const technologies = [
    { name: 'React 18', description: 'Nowoczesny framework UI' },
    { name: 'Vite', description: 'Szybki build tool' },
    { name: 'Framer Motion', description: 'Animacje i przejścia' },
    { name: 'TailwindCSS', description: 'Utility-first CSS' },
    { name: 'React Router', description: 'Routing po stronie klienta' },
    { name: 'Lucide React', description: 'Piękne ikony' }
  ]

  const teamMembers = [
    {
      name: 'Nova Strike',
      role: 'Lead Developer',
      emoji: '💻',
      description: 'Specjalistka od quantum computing i React development'
    },
    {
      name: 'Stellar Phoenix',
      role: 'UI/UX Designer',
      emoji: '🎨',
      description: 'Tworzy niesamowite interfejsy i cosmic experiences'
    },
    {
      name: 'Cosmic Viper',
      role: 'Backend Engineer',
      emoji: '⚡',
      description: 'Buduje potężne API i zarządza infrastrukturą'
    }
  ]

  return (
    <div className="container mx-auto px-6 py-20">
      {/* Header */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-center mb-16"
      >
        <div className="text-6xl mb-4">🌟</div>
        <h1 className="text-5xl md:text-6xl font-orbitron font-bold text-gradient neon-glow mb-6">
          O PROJEKCIE
        </h1>
        <p className="text-xl text-cosmic-blue max-w-3xl mx-auto">
          Rocket Fuel Girls to interaktywna platforma łącząca technologię, 
          kosmiczne przygody i potęgę kobiecych bohaterek galaktyki!
        </p>
      </motion.div>

      {/* Mission Statement */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.2 }}
        className="cosmic-card mb-16"
      >
        <div className="text-center">
          <div className="text-4xl mb-4">🚀</div>
          <h2 className="text-3xl font-bold text-gradient mb-6">Nasza Misja</h2>
          <p className="text-lg text-cosmic-blue leading-relaxed max-w-4xl mx-auto">
            Tworzymy przestrzeń, gdzie technologia spotyka się z wyobraźnią, 
            a galaktyczne bohaterki pokazują, że w kosmosie nie ma granic dla marzeń. 
            Każda Rocket Fuel Girl reprezentuje różne aspekty nauki, technologii i przygody, 
            inspirując do eksploracji wszechświata możliwości.
          </p>
        </div>
      </motion.div>

      {/* Features */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.4 }}
        className="mb-16"
      >
        <h2 className="text-3xl font-bold text-gradient text-center mb-12">
          Funkcjonalności
        </h2>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1, duration: 0.5 }}
              className="cosmic-card text-center group hover:scale-105 transition-transform duration-300"
            >
              <motion.div
                className="text-cosmic-purple mb-4 flex justify-center"
                whileHover={{ scale: 1.2, rotate: 10 }}
                transition={{ duration: 0.3 }}
              >
                {feature.icon}
              </motion.div>
              <h3 className="text-xl font-bold text-white mb-3">{feature.title}</h3>
              <p className="text-cosmic-blue text-sm leading-relaxed">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Technologies */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.6 }}
        className="mb-16"
      >
        <div className="cosmic-card">
          <h2 className="text-3xl font-bold text-gradient text-center mb-12 flex items-center justify-center space-x-3">
            <Code size={32} />
            <span>Technologie</span>
          </h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {technologies.map((tech, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1, duration: 0.5 }}
                className="p-4 bg-white/5 rounded-lg border border-white/10 hover:bg-white/10 transition-all duration-300"
              >
                <div className="flex items-center space-x-3">
                  <div className="w-3 h-3 bg-cosmic-purple rounded-full"></div>
                  <div>
                    <div className="font-bold text-white">{tech.name}</div>
                    <div className="text-sm text-cosmic-blue">{tech.description}</div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.div>

      {/* Team */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.8 }}
        className="mb-16"
      >
        <h2 className="text-3xl font-bold text-gradient text-center mb-12">
          Zespół Rocket Fuel Girls
        </h2>
        
        <div className="grid md:grid-cols-3 gap-8">
          {teamMembers.map((member, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.2, duration: 0.5 }}
              className="cosmic-card text-center group"
            >
              <motion.div
                className="text-6xl mb-4"
                whileHover={{ scale: 1.2, rotate: 360 }}
                transition={{ duration: 0.8 }}
              >
                {member.emoji}
              </motion.div>
              <h3 className="text-xl font-bold text-white mb-2">{member.name}</h3>
              <div className="text-cosmic-purple font-medium mb-3">{member.role}</div>
              <p className="text-cosmic-blue text-sm leading-relaxed">
                {member.description}
              </p>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Contact & Links */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8, delay: 1 }}
        className="cosmic-card text-center"
      >
        <div className="text-4xl mb-4">🌌</div>
        <h2 className="text-3xl font-bold text-gradient mb-6">
          Dołącz do Galaktycznej Przygody!
        </h2>
        <p className="text-cosmic-blue mb-8 max-w-2xl mx-auto">
          Gotowa na eksplorację kosmosu z Rocket Fuel Girls? 
          Rozpocznij swoją podróż już dziś i odkryj wszystkie sekrety galaktyki!
        </p>
        
        <div className="flex flex-wrap justify-center gap-4">
          <motion.button
            className="px-8 py-3 bg-gradient-to-r from-cosmic-purple to-cosmic-pink rounded-xl font-bold text-white hover:shadow-lg hover:shadow-cosmic-purple/50 transition-all duration-300 flex items-center space-x-2"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Rocket size={20} />
            <span>Rozpocznij Misję</span>
          </motion.button>
          
          <motion.button
            className="px-8 py-3 border-2 border-cosmic-blue rounded-xl font-bold text-cosmic-blue hover:bg-cosmic-blue hover:text-white transition-all duration-300 flex items-center space-x-2"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Heart size={20} />
            <span>Obserwuj Projekt</span>
          </motion.button>
        </div>
      </motion.div>

      {/* Footer */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8, delay: 1.2 }}
        className="text-center mt-16 py-8 border-t border-white/10"
      >
        <p className="text-cosmic-blue text-sm">
          Stworzone z ❤️ dla wszystkich marzycieli kosmicznych
        </p>
        <p className="text-cosmic-blue/60 text-xs mt-2">
          © 2024 Rocket Fuel Girls. Wszystkie prawa zastrzeżone w tej galaktyce.
        </p>
      </motion.div>
    </div>
  )
}

export default About