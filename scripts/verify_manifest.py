#!/usr/bin/env python3
import json, sys, os
from datetime import datetime

MANIFEST = "migi_manifest.json"

def load():
    if not os.path.exists(MANIFEST):
        print("Brak pliku", MANIFEST); sys.exit(2)
    return json.load(open(MANIFEST, "r", encoding="utf-8"))

def basic_check(m):
    missing = [k for k in ("name","version","commit_hash","modules","transmissions") if k not in m]
    if missing:
        print("Brakuje kluczy w manifeście:", missing); return False
    if not isinstance(m["transmissions"], list):
        print("transmissions musi być listą"); return False
    return True

def print_summary(m):
    print("=== MIGI Manifest ===")
    print("Project:", m.get("project") or m.get("name"))
    print("Version:", m["version"])
    print("Commit:", m["commit_hash"])
    print("Modules:", ", ".join(f"{k}={v}" for k,v in m["modules"].items()))
    print("Transmissions:", len(m["transmissions"]))
    for t in m["transmissions"]:
        print("-", t.get("id"), t.get("date"), "P(S)=", t.get("P_S_percent"))

if __name__ == "__main__":
    man = load()
    ok = basic_check(man)
    if not ok:
        sys.exit(3)
    print_summary(man)
    print("Checked at", datetime.utcnow().isoformat()+"Z")