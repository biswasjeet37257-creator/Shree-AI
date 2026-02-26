#!/bin/sh
set -e

echo "🔷 Initializing Shree AI Platform..."

# Initialize database tables
cd /app/backend
python initialize_db.py

# Start backend (FastAPI)
echo "🔷 Starting Shree Backend on port 8000..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start frontend (Next.js)
echo "🔷 Starting Shree Frontend on port 3000..."
cd /app/frontend
npx next start --port 3000 &

# Wait for any process to exit
wait -n
exit $?
