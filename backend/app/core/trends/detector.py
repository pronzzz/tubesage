from enum import Enum
from typing import List, Tuple
from .velocity import velocity_calculator

class TrendState(str, Enum):
    EMERGING = "Emerging"       # Low views, high acceleration
    TRENDING = "Trending"       # High views, positive velocity
    SATURATING = "Saturating"   # High views, slowing velocity (neg acceleration)
    DECLINING = "Declining"     # Dropping views (neg velocity)
    STAGNANT = "Stagnant"       # Low activity
    UNKNOWN = "Unknown"

class TrendDetector:
    def detect_trend(self, view_series: List[Tuple[float, int]]) -> Tuple[TrendState, float]:
        """
        Analyzes a time series of (timestamp, views) and returns the TrendState and Confidence.
        """
        if len(view_series) < 3:
            return TrendState.UNKNOWN, 0.0

        # 1. Calculate Velocity (rate of view growth)
        # We can calculate rolling velocity behavior if we had more granular data.
        # For now, simplistic approach:
        
        # Linear fit to get overall velocity
        current_velocity = velocity_calculator.calculate_velocity(view_series)
        
        # Split series in half to estimate acceleration (v2 - v1)
        mid = len(view_series) // 2
        v1 = velocity_calculator.calculate_velocity(view_series[:mid])
        v2 = velocity_calculator.calculate_velocity(view_series[mid:])
        
        # Acceleration approximation
        acceleration = v2 - v1
        
        # Normalize/Heuristics (These thresholds would need tuning with real data)
        # Assuming views per hour as unit if input timestamps are seconds, this will be small.
        # Let's assume input timestamps are seconds.
        
        is_high_velocity = current_velocity > 0.1  # Arbitrary threshold
        is_accelerating = acceleration > 0.01
        
        if is_high_velocity and is_accelerating:
            return TrendState.TRENDING, 0.9
        elif not is_high_velocity and is_accelerating:
            return TrendState.EMERGING, 0.7
        elif is_high_velocity and not is_accelerating:
            return TrendState.SATURATING, 0.6
        elif current_velocity < 0:
            return TrendState.DECLINING, 0.8
        
        return TrendState.STAGNANT, 0.5

trend_detector = TrendDetector()
