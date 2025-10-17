#!/usr/bin/env python3
"""
MÓZG BOGA - DEVELOPMENT STARTUP SCRIPT
Uruchamia cały ekosystem w trybie deweloperskim
"""
import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def print_banner():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    🧠 MÓZG BOGA                           ║
    ║              Zintegrowany Ekosystem AI                    ║
    ║                                                           ║
    ║  🚀 Development Startup Script                            ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

def check_dependencies():
    """Sprawdza czy wymagane zależności są zainstalowane"""
    print("🔍 Sprawdzanie zależności...")
    
    # Check Python packages
    required_packages = [
        'fastapi', 'uvicorn', 'sqlalchemy', 'bcrypt', 
        'python-jose', 'passlib', 'python-dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Brakujące pakiety: {', '.join(missing_packages)}")
        print("📦 Instalowanie...")
        subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing_packages)
    else:
        print("✅ Wszystkie zależności są dostępne")

def check_environment():
    """Sprawdza konfigurację środowiska"""
    print("🔧 Sprawdzanie środowiska...")
    
    env_file = Path('.env')
    if not env_file.exists():
        print("⚠️ Brak pliku .env, kopiuję z .env.master")
        if Path('.env.master').exists():
            import shutil
            shutil.copy('.env.master', '.env')
            print("✅ Plik .env utworzony")
        else:
            print("❌ Brak pliku .env.master - uruchom setup.py")
            return False
    
    return True

def start_database():
    """Inicjalizuje bazę danych"""
    print("🗄️ Inicjalizacja bazy danych...")
    
    try:
        sys.path.append(os.path.join('6_USER_AUTH_SYSTEM', 'backend'))
        from models import create_tables
        create_tables()
        print("✅ Baza danych gotowa")
        return True
    except Exception as e:
        print(f"❌ Błąd bazy danych: {e}")
        return False

def start_backend():
    """Uruchamia backend FastAPI"""
    print("🚀 Uruchamianie backend...")
    
    try:
        # Start server in background
        process = subprocess.Popen([
            sys.executable, 'server.py'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit and check if it's running
        time.sleep(3)
        if process.poll() is None:
            print("✅ Backend uruchomiony na http://localhost:4000")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Backend nie uruchomiony: {stderr.decode()}")
            return None
    except Exception as e:
        print(f"❌ Błąd uruchamiania backend: {e}")
        return None

def start_frontend():
    """Uruchamia frontend (http-server lub simple server)"""
    print("🌐 Uruchamianie frontend...")
    
    # Check if http-server is available
    try:
        subprocess.run(['http-server', '--version'], 
                      capture_output=True, check=True)
        use_http_server = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        use_http_server = False
    
    if use_http_server:
        try:
            process = subprocess.Popen([
                'http-server', '6_USER_AUTH_SYSTEM/frontend', 
                '-p', '8080', '--cors'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            time.sleep(2)
            if process.poll() is None:
                print("✅ Frontend uruchomiony na http://localhost:8080")
                return process
        except Exception as e:
            print(f"⚠️ http-server błąd: {e}")
    
    # Fallback to Python simple server
    try:
        os.chdir('6_USER_AUTH_SYSTEM/frontend')
        process = subprocess.Popen([
            sys.executable, '-m', 'http.server', '8080'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        os.chdir('../..')
        time.sleep(2)
        if process.poll() is None:
            print("✅ Frontend uruchomiony na http://localhost:8080 (Python server)")
            return process
    except Exception as e:
        print(f"❌ Błąd uruchamiania frontend: {e}")
        return None

def show_status():
    """Pokazuje status systemu"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    🎉 SYSTEM GOTOWY                       ║
    ╠═══════════════════════════════════════════════════════════╣
    ║                                                           ║
    ║  🔗 LINKI:                                                ║
    ║     • API Docs:    http://localhost:4000/docs            ║
    ║     • Health:      http://localhost:4000/health          ║
    ║     • Login:       http://localhost:8080/login.html      ║
    ║     • Dashboard:   http://localhost:8080/dashboard.html  ║
    ║                                                           ║
    ║  📊 ENDPOINTS:                                            ║
    ║     • POST /auth/register - Rejestracja                  ║
    ║     • POST /auth/login    - Logowanie                    ║
    ║     • POST /api/run_task  - SYNERGY                      ║
    ║     • POST /api/migi_7g   - MIGI 7G Network              ║
    ║                                                           ║
    ║  🎮 UŻYTKOWNICY:                                          ║
    ║     • observer - Konserwatywny (wagi 2,3,5,5,3,2)       ║
    ║     • creator  - Kreatywny (wagi 4,5,7,7,5,4)           ║
    ║     • editor   - Zbalansowany (wagi 3,4,6,6,4,3)        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    💡 Tip: Otwórz http://localhost:8080/login.html aby zacząć!
    
    ⏹️  Naciśnij Ctrl+C aby zatrzymać wszystkie serwisy
    """)

def main():
    """Główna funkcja startowa"""
    print_banner()
    
    # Checks
    if not check_environment():
        return 1
    
    check_dependencies()
    
    if not start_database():
        return 1
    
    # Start services
    backend_process = start_backend()
    if not backend_process:
        return 1
    
    frontend_process = start_frontend()
    
    # Show status
    show_status()
    
    # Auto-open browser
    try:
        time.sleep(2)
        webbrowser.open('http://localhost:8080/login.html')
    except:
        pass
    
    # Wait for interrupt
    try:
        print("🔄 Serwisy działają... (Ctrl+C aby zatrzymać)")
        while True:
            time.sleep(1)
            
            # Check if processes are still running
            if backend_process.poll() is not None:
                print("❌ Backend process died")
                break
                
            if frontend_process and frontend_process.poll() is not None:
                print("⚠️ Frontend process died")
    
    except KeyboardInterrupt:
        print("\n🛑 Zatrzymywanie serwisów...")
        
        if backend_process:
            backend_process.terminate()
            backend_process.wait()
            print("✅ Backend zatrzymany")
        
        if frontend_process:
            frontend_process.terminate()
            frontend_process.wait()
            print("✅ Frontend zatrzymany")
        
        print("👋 Mózg Boga wyłączony. Do zobaczenia!")

if __name__ == "__main__":
    sys.exit(main())