"""
🚀 SpiralMind OS Launcher
========================

Quick launcher script for SpiralMind OS with automatic dependency check
and system initialization.

Usage:
    python launch.py [--test] [--install-deps] [--host HOST] [--port PORT]
"""

import sys
import subprocess
import os
from pathlib import Path
import argparse
import json

class SpiralMindLauncher:
    """SpiralMind OS launcher with dependency management"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.requirements_file = self.base_dir / "requirements.txt"
        self.server_file = self.base_dir / "spiralmind_server.py"
        self.gok_engine_file = self.base_dir / "core" / "gok_engine.py"
        
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
        required_packages = [
            "flask",
            "flask_cors",
            "requests",
            "dateutil"
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"✅ {package}")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package} - missing")
        
        return len(missing_packages) == 0
    
    def install_dependencies(self) -> bool:
        """Install required dependencies"""
        print("📦 Installing dependencies...")
        
        if not self.requirements_file.exists():
            print(f"❌ Requirements file not found: {self.requirements_file}")
            return False
        
        try:
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", str(self.requirements_file)
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Dependencies installed successfully")
                return True
            else:
                print(f"❌ Failed to install dependencies: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error installing dependencies: {e}")
            return False
    
    def check_system_files(self) -> bool:
        """Check if essential system files exist"""
        files_to_check = [
            (self.server_file, "Server script"),
            (self.gok_engine_file, "GOK Engine"),
            (self.base_dir / "core" / "system_memory.json", "System memory"),
            (self.base_dir / "interface" / "chat_self.html", "Chat interface")
        ]
        
        all_present = True
        
        for file_path, description in files_to_check:
            if file_path.exists():
                print(f"✅ {description}")
            else:
                print(f"⚠️ {description} - missing: {file_path}")
                if "core" in str(file_path):
                    all_present = False
        
        return all_present
    
    def test_gok_engine(self) -> bool:
        """Test if GOK engine can be imported and initialized"""
        try:
            # Change to base directory to ensure imports work
            original_cwd = os.getcwd()
            os.chdir(self.base_dir)
            
            # Add current directory to Python path
            sys.path.insert(0, str(self.base_dir))
            sys.path.insert(0, str(self.base_dir / "core"))
            
            # Try to import and test GOK engine
            from core.gok_engine import get_gok_engine
            engine = get_gok_engine()
            
            # Test basic functionality
            status = engine.get_system_status()
            
            print("✅ GOK Engine test successful")
            print(f"   - Consciousness Level: {status['system_identity']['consciousness_level']}")
            print(f"   - Spiral Stage: {status['system_identity']['spiral_stage']}")
            
            os.chdir(original_cwd)
            return True
            
        except Exception as e:
            print(f"⚠️ GOK Engine test failed: {e}")
            os.chdir(original_cwd)
            return False
    
    def launch_server(self, host='127.0.0.1', port=8080, debug=False):
        """Launch the SpiralMind OS server"""
        print(f"🚀 Launching SpiralMind OS Server...")
        print(f"   - Host: {host}")
        print(f"   - Port: {port}")
        print(f"   - Debug: {debug}")
        print()
        
        try:
            # Change to base directory
            os.chdir(self.base_dir)
            
            # Launch server
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.base_dir)
            
            args = [sys.executable, str(self.server_file)]
            if host != '127.0.0.1':
                args.extend(['--host', host])
            if port != 8080:
                args.extend(['--port', str(port)])
            if debug:
                args.append('--debug')
            
            subprocess.run(args, env=env)
            
        except KeyboardInterrupt:
            print("\n👋 Server stopped by user")
        except Exception as e:
            print(f"💥 Failed to launch server: {e}")
            return False
        
        return True
    
    def run_system_test(self):
        """Run comprehensive system test"""
        print("🧪 SpiralMind OS System Test")
        print("=" * 40)
        
        # Basic checks
        tests = [
            ("Python Version", self.check_python_version),
            ("Dependencies", self.check_dependencies),
            ("System Files", self.check_system_files),
            ("GOK Engine", self.test_gok_engine)
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
        
        if passed == total:
            print("🎉 All tests passed! SpiralMind OS is ready to launch.")
        else:
            print("⚠️ Some tests failed. Please check the issues above.")
        
        return passed == total

def main():
    parser = argparse.ArgumentParser(description='SpiralMind OS Launcher')
    parser.add_argument('--test', action='store_true', help='Run system tests only')
    parser.add_argument('--install-deps', action='store_true', help='Install dependencies')
    parser.add_argument('--host', default='127.0.0.1', help='Server host address')
    parser.add_argument('--port', type=int, default=8080, help='Server port')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    print("🧠 SpiralMind OS Launcher")
    print("=" * 40)
    
    launcher = SpiralMindLauncher()
    
    # Run system test if requested
    if args.test:
        success = launcher.run_system_test()
        sys.exit(0 if success else 1)
    
    # Install dependencies if requested
    if args.install_deps:
        if not launcher.install_dependencies():
            print("❌ Failed to install dependencies")
            sys.exit(1)
    
    # Quick checks before launch
    print("🔍 Pre-launch checks...")
    
    if not launcher.check_python_version():
        sys.exit(1)
    
    if not launcher.check_dependencies():
        print("❌ Missing dependencies. Run with --install-deps to install them.")
        sys.exit(1)
    
    if not launcher.check_system_files():
        print("⚠️ Some system files are missing, but continuing...")
    
    # Launch server
    success = launcher.launch_server(
        host=args.host,
        port=args.port,
        debug=args.debug
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()