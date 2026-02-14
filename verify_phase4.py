import sys
import os

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage Predictive Modeling Engine...")

try:
    from app.core.predictions.growth_model import growth_predictor
    from app.core.predictions.simulator import strategy_simulator
    
    print("✅ Prediction modules loaded")
    
    # Test Prediction (Linear)
    # y = x. 0->0, 100->100
    history = [(0, 0), (100, 100)]
    # Predict next 1 day (86400 seconds)
    # Slope should be 1.0. Next value at 100+86400 should be ~86500
    future = growth_predictor.predict_views(history, days=1)
    print(f"Test Prediction (1 day out): {future[0][1]}")
    
    # Test Simulation
    stats = {"avg_views": 1000}
    # Double uploads -> Expect ~1.8x growth (80% elasticity)
    changes = {"upload_frequency_multiplier": 2.0}
    sim = strategy_simulator.simulate_scenario(stats, changes)
    print(f"Test Simulation (2x uploads): {sim}")
    
except Exception as e:
    print(f"❌ Verification failed: {e}")
    raise e
