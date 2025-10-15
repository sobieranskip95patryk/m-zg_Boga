#!/bin/bash

# MTA Platform Stop Script
echo "🛑 Stopping MTA Platform..."

if [ -f .mta_pids ]; then
    PIDS=$(cat .mta_pids)
    IFS=',' read -ra PID_ARRAY <<< "$PIDS"
    
    for pid in "${PID_ARRAY[@]}"; do
        if kill -0 $pid 2>/dev/null; then
            echo "Stopping process $pid..."
            kill $pid
        fi
    done
    
    rm .mta_pids
    echo "✅ All services stopped!"
else
    echo "❌ No PID file found. Services may already be stopped."
fi