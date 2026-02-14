import sys
import os
import time

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage Trend Detection Engine...")

try:
    from app.core.trends.velocity import velocity_calculator
    from app.core.trends.detector import trend_detector, TrendState
    
    print("✅ Trend modules loaded")
    
    # Test Velocity
    # Simple linear growth: y = 2x
    series = [(0, 0), (1, 2), (2, 4)]
    vel = velocity_calculator.calculate_velocity(series)
    print(f"Test Velocity (Expected ~2.0): {vel}")
    
    # Test Detector
    # Accelerating series
    acc_series = [(0, 10), (1, 12), (2, 16), (3, 25)] 
    signal, conf = trend_detector.detect_trend(acc_series)
    print(f"Test Detection (Accelerating): {signal} (Conf: {conf})")
    
except Exception as e:
    print(f"❌ Verification failed: {e}")
    raise e
