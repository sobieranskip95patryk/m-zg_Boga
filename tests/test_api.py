import sys, pathlib, os
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fastapi.testclient import TestClient

sys.path.insert(0, str(ROOT / "apps" / "api"))
import main as api

client = TestClient(api.app)

def test_sgok():
    r = client.post('/api/gokai/sgok', json={'n': 10})
    assert r.status_code == 200
    assert r.json()['S'] > 0

def test_chat_fallback():
    api.os.environ['PROVIDER'] = 'unknown'  # force fallback
    r = client.post('/api/chat', json={'messages':[{'role':'user','content':'x=5 n=8'}]})
    assert r.status_code == 200
    assert 'Fallback' in r.json()['content']

def test_hiphop_upload_and_list(tmp_path):
    content = b'abc123'
    files = {'file': ('beat.wav', content, 'audio/wav')}
    r = client.post('/api/hiphop/upload', files=files, data={'author':'test'})
    assert r.status_code == 200
    r2 = client.get('/api/hiphop/list')
    assert r2.status_code == 200
    assert any(t['name']=='beat.wav' for t in r2.json()['tracks'])

def test_drift_leaderboard():
    client.post('/api/drift/score', json={'name':'alice','score':5})
    r = client.get('/api/drift/leaderboard')
    assert r.status_code == 200
    assert isinstance(r.json()['leaderboard'], list)

def test_events():
    r = client.post('/api/events/log', json={'event':'ping','user':'tester','meta':{'ok':True}})
    assert r.status_code == 200
    r = client.get('/api/events/export.csv')
    assert r.status_code == 200
    assert 'text/csv' in r.headers.get('content-type','')
