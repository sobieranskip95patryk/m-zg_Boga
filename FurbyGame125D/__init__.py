"""
AI Furby 1.25D: San Andreas Edition - Complete Game Package
Main launcher and package initialization
MTAQuestWebsideX.com integration ready
"""

import sys
import os
import logging
import argparse
from pathlib import Path

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('furby_game.log', encoding='utf-8')
        ]
    )

def check_dependencies():
    """Check if all required dependencies are available"""
    required_modules = [
        'flask',
        'typing',
        'json',
        'random',
        'time',
        'datetime',
        'pathlib'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"❌ Missing required modules: {', '.join(missing_modules)}")
        print("📦 Install them with: pip install flask")
        return False
    
    return True

def display_banner():
    """Display game banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                    🎮 AI FURBY 1.25D: SAN ANDREAS EDITION 🎮                 ║
    ║                                                                              ║
    ║  🌟 ASCII Art Gaming     🪙 FURBX Token Integration     🚗 Vehicle System   ║
    ║  🎯 Progressive Gameplay 🔥 Heat Mechanics             💎 Premium Features  ║
    ║  🏆 Achievement System   📊 Statistics Tracking        💾 Save/Load System  ║
    ║                                                                              ║
    ║                          MTAQuestWebsideX.com Platform                      ║
    ║                         Powered by Meta-Geniusz-mózg_Boga                  ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(description='AI Furby 1.25D: San Andreas Edition')
    parser.add_argument('--mode', choices=['console', 'web', 'test'], default='console',
                       help='Game mode: console (terminal), web (browser), or test')
    parser.add_argument('--host', default='127.0.0.1', help='Web server host (web mode only)')
    parser.add_argument('--port', type=int, default=5000, help='Web server port (web mode only)')
    parser.add_argument('--player', default=None, help='Player name/ID')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    # Setup
    setup_logging()
    logger = logging.getLogger(__name__)
    
    display_banner()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    try:
        if args.mode == 'console':
            # Console/Terminal mode
            print("🎮 Starting Console Mode...")
            
            from furby_san_andreas import FurbyGame125D
            
            player_id = args.player or input("👤 Enter your player name: ").strip()
            if not player_id:
                player_id = "furby_player"
            
            print(f"🚀 Initializing game for player: {player_id}")
            
            game = FurbyGame125D(player_id)
            game.start_game()
            
        elif args.mode == 'web':
            # Web/Browser mode
            print("🌐 Starting Web Server Mode...")
            print(f"🔗 Server will run on http://{args.host}:{args.port}")
            print("🎮 Open your browser and navigate to the URL above")
            print("⏹️  Press Ctrl+C to stop the server")
            
            from furby_server import FurbyGameServer
            
            server = FurbyGameServer()
            server.run(host=args.host, port=args.port, debug=args.debug)
            
        elif args.mode == 'test':
            # Test mode
            print("🧪 Starting Test Mode...")
            
            # Test web interface generation
            from furby_web_interface import FurbyGameWebInterface
            
            web_interface = FurbyGameWebInterface()
            test_html = web_interface.render_game_dashboard("test_player")
            
            test_file = "furby_game_test.html"
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(test_html)
            
            print(f"✅ Web interface test completed: {test_file}")
            
            # Test game engine
            from furby_san_andreas import FurbyGame125D
            
            test_game = FurbyGame125D("test_player")
            print("✅ Game engine test completed")
            
            # Test token system integration
            try:
                sys.path.append(str(Path(__file__).parent.parent / "TokenSystem"))
                from token_logic import FurbyToken
                
                token_system = FurbyToken()
                print("✅ Token system integration test completed")
            except ImportError:
                print("⚠️  Token system not available (optional)")
            
            print("🎉 All tests completed successfully!")
            
    except KeyboardInterrupt:
        print("\n👋 Game terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Game error: {e}")
        print(f"💥 Game error: {e}")
        sys.exit(1)

def launch_console_game(player_name=None):
    """Quick launcher for console mode"""
    from furby_san_andreas import FurbyGame125D
    
    setup_logging()
    display_banner()
    
    if not check_dependencies():
        return False
    
    player_id = player_name or "furby_player"
    
    try:
        game = FurbyGame125D(player_id)
        game.start_game()
        return True
    except Exception as e:
        print(f"💥 Game error: {e}")
        return False

def launch_web_server(host='127.0.0.1', port=5000, debug=False):
    """Quick launcher for web server"""
    from furby_server import FurbyGameServer
    
    setup_logging()
    display_banner()
    
    if not check_dependencies():
        return False
    
    try:
        print(f"🌐 Starting web server on http://{host}:{port}")
        server = FurbyGameServer()
        server.run(host=host, port=port, debug=debug)
        return True
    except Exception as e:
        print(f"💥 Server error: {e}")
        return False

def create_desktop_shortcut():
    """Create desktop shortcut for easy game access"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "AI Furby 1.25D.lnk")
        target = sys.executable
        wDir = str(Path(__file__).parent)
        icon = str(Path(__file__).parent / "furby_icon.ico")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.Arguments = f'"{__file__}" --mode console'
        shortcut.WorkingDirectory = wDir
        shortcut.WindowStyle = 1
        
        if os.path.exists(icon):
            shortcut.IconLocation = icon
        
        shortcut.save()
        
        print(f"🔗 Desktop shortcut created: {path}")
        return True
        
    except ImportError:
        print("⚠️  Desktop shortcut creation requires: pip install winshell pywin32")
        return False
    except Exception as e:
        print(f"⚠️  Failed to create desktop shortcut: {e}")
        return False

if __name__ == "__main__":
    main()