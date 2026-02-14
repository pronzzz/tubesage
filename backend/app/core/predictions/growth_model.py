from typing import List, Tuple
import numpy as np

class GrowthPredictor:
    def predict_views(self, history: List[Tuple[float, int]], days: int = 7) -> List[Tuple[float, int]]:
        """
        Predicts future views based on historical data.
        Input: List of (timestamp_unix, view_count)
        Output: List of (future_timestamp_unix, predicted_view_count)
        """
        if len(history) < 2:
            return []

        times, values = zip(*history)
        times = np.array(times)
        values = np.array(values)

        # MVP: Linear Regression
        # In production, use Prophet or Gradient Boosting
        slope, intercept = np.polyfit(times, values, 1)

        last_time = times[-1]
        future_points = []
        
        # Predict for next 'days'
        seconds_per_day = 86400
        for i in range(1, days + 1):
            future_time = last_time + (i * seconds_per_day)
            predicted_value = slope * future_time + intercept
            future_points.append((future_time, int(max(0, predicted_value))))

        return future_points

growth_predictor = GrowthPredictor()
