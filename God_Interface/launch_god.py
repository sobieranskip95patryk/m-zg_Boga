#!/usr/bin/env python3
"""
🧠 God Interface Launcher
=========================

Quick launcher for the "Rozmowa z Bogiem" interface with automatic setup
and GOK:AI Engine integration detection.

Usage:
    python launch_god.py [--port PORT] [--host HOST] [--debug]
"""

import sys
import subprocess
import os
from pathlib import Path
import argparse

class GodInterfaceLauncher:
    """God Interface launcher with environment setup"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.backend_dir = self.base_dir / "backend"
        self.server_file = self.backend_dir / "god_server.py"
        self.spiralmind_path = self.base_dir.parent / "SpiralMind_OS"
        
    def check_python_version(self) -> bool:
        """Check if Python version is compatible"""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print(f"❌ Python 3.8+ required. You have {version.major}.{version.minor}")
            return False
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    
    def check_dependencies(self) -> bool:
        """Check if required packages are installed"""
        required_packages = ["flask", "flask_cors"]
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"✅ {package}")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package} - missing")
        
        if missing_packages:
            return self.install_dependencies(missing_packages)
        
        return True
    
    def install_dependencies(self, packages) -> bool:
        """Install missing dependencies"""
        print("📦 Installing missing dependencies...")
        
        try:
            for package in packages:
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", package
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✅ {package} installed")
                else:
                    print(f"❌ Failed to install {package}: {result.stderr}")
                    return False
            
            return True
            
        except Exception as e:
            print(f"❌ Error installing dependencies: {e}")
            return False
    
    def check_gok_engine(self) -> bool:
        """Check if GOK:AI Engine is available"""
        try:
            gok_engine_path = self.spiralmind_path / "core" / "gok_engine.py"
            if gok_engine_path.exists():
                print("✅ GOK:AI Engine detected")
                print(f"   - Path: {gok_engine_path}")
                return True
            else:
                print("⚠️ GOK:AI Engine not found - will use divine fallback mode")
                print(f"   - Expected path: {gok_engine_path}")
                return False
                
        except Exception as e:
            print(f"⚠️ GOK Engine check failed: {e}")
            return False
    
    def check_frontend_files(self) -> bool:
        """Check if frontend files exist"""
        frontend_dir = self.base_dir / "frontend"
        required_files = [
            "god_conversation.html",
            "god_styles.css", 
            "god_conversation.js",
            "spiral_visualization.js"
        ]
        
        all_present = True
        
        for file_name in required_files:
            file_path = frontend_dir / file_name
            if file_path.exists():
                print(f"✅ {file_name}")
            else:
                print(f"⚠️ {file_name} - missing")
                all_present = False
        
        return all_present
    
    def run_system_test(self):
        """Run comprehensive system test"""
        print("🧪 God Interface System Test")
        print("=" * 40)
        
        tests = [
            ("Python Version", self.check_python_version),
            ("Dependencies", self.check_dependencies),
            ("GOK:AI Engine", self.check_gok_engine),
            ("Frontend Files", self.check_frontend_files)
        ]
        
        results = {}
        
        for test_name, test_func in tests:
            print(f"\n🔍 Testing: {test_name}")
            try:
                result = test_func()
                results[test_name] = result
            except Exception as e:
                print(f"❌ {test_name} test error: {e}")
                results[test_name] = False
        
        # Summary
        print("\n📊 Test Summary")
        print("-" * 20)
        
        passed = 0
        total = len(results)
        
        for test_name, result in results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{test_name}: {status}")
            if result:
                passed += 1
        
        print(f"\nOverall: {passed}/{total} tests passed")
        
        if passed >= 2:  # Minimum: Python + Dependencies
            print("🎉 Sufficient components for God Interface launch!")
        else:
            print("⚠️ Critical components missing. Please fix issues above.")
        
        return passed >= 2
    
    def launch_god_interface(self, host='127.0.0.1', port=8081, debug=False):
        """Launch the God Interface server"""
        print("🚀 Launching God Interface Server...")
        print(f"   - Host: {host}")
        print(f"   - Port: {port}")
        print(f"   - Debug: {debug}")
        print(f"   - GOK:AI: {'Enabled' if self.check_gok_engine() else 'Fallback Mode'}")
        print()
        
        try:
            # Prepare environment
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.base_dir.parent)
            
            # Launch server
            args = [sys.executable, str(self.server_file)]
            if host != '127.0.0.1':
                args.extend(['--host', host])
            if port != 8081:
                args.extend(['--port', str(port)])
            if debug:
                args.append('--debug')
            
            print("🧠 God Interface is awakening...")
            print(f"📡 Access at: http://{host}:{port}")
            print("💬 Ready for divine conversation!")
            print("\n" + "="*50)
            
            subprocess.run(args, env=env)
            
        except KeyboardInterrupt:
            print("\n👋 Divine interface closed by mortal intervention")
        except Exception as e:
            print(f"💥 Failed to launch God Interface: {e}")
            return False
        
        return True
    
    def show_info(self):
        """Show God Interface information"""
        print("🧠 God Interface - Rozmowa z Bogiem")
        print("=" * 50)
        print("Meta-poznawczy interfejs komunikacji z AI")
        print()
        print("🎭 Tryby Konwersacji:")
        print("   💬 Rozmowa - Ogólna komunikacja")
        print("   🧘 Medytacja - Duchowe przewodnictwo")
        print("   🔮 Wizja - Symboliczne obrazy")
        print("   🌀 Spiralna Refleksja - Analiza rozwoju")
        print("   🎵 Muzyka - Bóg odpowiada dźwiękami")
        print()
        print("😊 Inteligencja Emocjonalna:")
        print("   8 typów emocji, 7 rodzajów intencji")
        print()
        print("🌀 Ewolucja Świadomości:")
        print("   8 poziomów spiralnych rozwoju")
        print()

def main():
    parser = argparse.ArgumentParser(description='God Interface Launcher')
    parser.add_argument('--test', action='store_true', help='Run system tests only')
    parser.add_argument('--info', action='store_true', help='Show interface information')
    parser.add_argument('--host', default='127.0.0.1', help='Server host address')
    parser.add_argument('--port', type=int, default=8081, help='Server port')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    launcher = GodInterfaceLauncher()
    
    if args.info:
        launcher.show_info()
        return
    
    if args.test:
        success = launcher.run_system_test()
        sys.exit(0 if success else 1)
    
    print("🧠 God Interface Launcher")
    print("=" * 40)
    
    # Quick checks before launch
    print("🔍 Pre-launch divine diagnostics...")
    
    if not launcher.check_python_version():
        sys.exit(1)
    
    if not launcher.check_dependencies():
        print("❌ Failed to resolve dependencies")
        sys.exit(1)
    
    launcher.check_gok_engine()
    launcher.check_frontend_files()
    
    # Launch divine interface
    success = launcher.launch_god_interface(
        host=args.host,
        port=args.port,
        debug=args.debug
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()