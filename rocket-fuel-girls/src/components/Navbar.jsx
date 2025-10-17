import { Link, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { Home, Users, Flame, Target, Info, Palette } from 'lucide-react'

const Navbar = ({ currentTheme, onThemeChange }) => {
  const location = useLocation()

  const navItems = [
    { path: '/', icon: Home, label: 'Główna', color: 'cosmic-blue' },
    { path: '/gallery', icon: Users, label: 'Galeria', color: 'cosmic-purple' },
    { path: '/fuel-lab', icon: Flame, label: 'Laboratorium', color: 'cosmic-red' },
    { path: '/missions', icon: Target, label: 'Misje', color: 'cosmic-orange' },
    { path: '/about', icon: Info, label: 'O nas', color: 'cosmic-green' }
  ]

  const themes = [
    { id: 'nebula', name: 'Nebula', icon: '🌌' },
    { id: 'cosmic', name: 'Cosmic', icon: '✨' },
    { id: 'space', name: 'Deep Space', icon: '🌌' }
  ]

  return (
    <motion.nav 
      className="glass-effect sticky top-0 z-50 border-b border-cosmic-purple/20"
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      <div className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3 group">
            <motion.div
              className="text-3xl"
              whileHover={{ 
                rotate: 360,
                scale: 1.2
              }}
              transition={{ duration: 0.5 }}
            >
              🚀
            </motion.div>
            <div>
              <h1 className="text-xl font-orbitron font-bold text-gradient group-hover:neon-glow transition-all">
                ROCKET FUEL GIRLS
              </h1>
              <p className="text-xs text-cosmic-blue">Galaktyczne Bohaterki</p>
            </div>
          </Link>

          {/* Navigation Items */}
          <div className="hidden md:flex items-center space-x-1">
            {navItems.map((item) => {
              const isActive = location.pathname === item.path
              const Icon = item.icon
              
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className="group relative"
                >
                  <motion.div
                    className={`
                      flex items-center space-x-2 px-4 py-2 rounded-xl transition-all duration-300
                      ${isActive 
                        ? 'bg-cosmic-purple/20 text-cosmic-purple shadow-lg' 
                        : 'hover:bg-white/10 text-gray-300 hover:text-white'
                      }
                    `}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                  >
                    <Icon size={18} />
                    <span className="font-medium">{item.label}</span>
                  </motion.div>
                  
                  {isActive && (
                    <motion.div
                      className="absolute bottom-0 left-0 right-0 h-0.5 bg-cosmic-purple rounded-full"
                      layoutId="activeIndicator"
                      initial={false}
                    />
                  )}
                </Link>
              )
            })}
          </div>

          {/* Theme Switcher */}
          <div className="flex items-center space-x-2">
            <div className="hidden sm:flex items-center space-x-1 bg-white/5 rounded-lg p-1">
              {themes.map((theme) => (
                <motion.button
                  key={theme.id}
                  onClick={() => onThemeChange(theme.id)}
                  className={`
                    flex items-center space-x-1 px-3 py-1 rounded-md text-sm transition-all
                    ${currentTheme === theme.id 
                      ? 'bg-cosmic-purple text-white' 
                      : 'text-gray-400 hover:text-white hover:bg-white/10'
                    }
                  `}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <span>{theme.icon}</span>
                  <span className="hidden lg:inline">{theme.name}</span>
                </motion.button>
              ))}
            </div>

            {/* Mobile Menu Button */}
            <motion.button 
              className="md:hidden flex items-center justify-center w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <div className="w-5 h-5 flex flex-col justify-center space-y-1">
                <div className="w-full h-0.5 bg-current rounded"></div>
                <div className="w-full h-0.5 bg-current rounded"></div>
                <div className="w-full h-0.5 bg-current rounded"></div>
              </div>
            </motion.button>
          </div>
        </div>

        {/* Mobile Navigation */}
        <motion.div 
          className="md:hidden mt-4 pt-4 border-t border-white/10"
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          transition={{ duration: 0.3 }}
        >
          <div className="grid grid-cols-2 gap-2">
            {navItems.map((item) => {
              const isActive = location.pathname === item.path
              const Icon = item.icon
              
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`
                    flex items-center space-x-2 p-3 rounded-lg transition-all
                    ${isActive 
                      ? 'bg-cosmic-purple/20 text-cosmic-purple' 
                      : 'bg-white/5 text-gray-300 hover:bg-white/10 hover:text-white'
                    }
                  `}
                >
                  <Icon size={18} />
                  <span className="font-medium">{item.label}</span>
                </Link>
              )
            })}
          </div>
        </motion.div>
      </div>
    </motion.nav>
  )
}

export default Navbar