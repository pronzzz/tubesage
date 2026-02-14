from typing import List, Tuple
import numpy as np

class VelocityCalculator:
    def calculate_velocity(self, time_series: List[Tuple[float, int]]) -> float:
        """
        Calculates the average velocity (views per hour/unit time) over the series.
        Input: List of (timestamp_unix, metric_value)
        """
        if len(time_series) < 2:
            return 0.0
            
        times, values = zip(*time_series)
        times = np.array(times)
        values = np.array(values)
        
        # Simple slope of linear regression
        if np.max(times) - np.min(times) == 0:
            return 0.0
            
        slope = np.polyfit(times, values, 1)[0]
        return float(slope)

    def calculate_acceleration(self, velocity_series: List[Tuple[float, float]]) -> float:
        """
        Calculates acceleration (change in velocity over time).
        Input: List of (timestamp_unix, velocity_value)
        """
        if len(velocity_series) < 2:
            return 0.0
            
        times, velocities = zip(*velocity_series)
        times = np.array(times, dtype=float)
        velocities = np.array(velocities, dtype=float)
        
        if np.max(times) - np.min(times) == 0:
            return 0.0

        # Slope of velocity -> Acceleration
        slope = np.polyfit(times, velocities, 1)[0]
        return float(slope)

velocity_calculator = VelocityCalculator()
