#!/bin/bash

# Kill existing processes
pkill -f "uvicorn"
pkill -f "vite"

# Start Backend
echo "Starting Backend..."
cd backend
# Using python -m uvicorn to avoid path issues
nohup python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 > ../backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend running (PID: $BACKEND_PID)"

# Start Frontend
echo "Starting Frontend..."
cd ../frontend
nohup npm run dev -- --host > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend running (PID: $FRONTEND_PID)"

echo "TubeSage started!"
echo "Backend logging to backend.log"
echo "Frontend logging to frontend.log"
