#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."
cd backend
python -m venv .venv
source .venv/bin/activate || .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
uvicorn app.main:app --reload
