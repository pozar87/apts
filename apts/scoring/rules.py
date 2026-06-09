import numpy as np


class ThresholdRule:
    """
    Scoring rule based on descending thresholds (e.g., >= 65, >= 50, etc.).
    """

    def __init__(self, thresholds: list[float], points: list[int]):
        self.thresholds = thresholds
        self.points = points

    def score(self, value: float) -> int:
        for t, p in zip(self.thresholds, self.points):
            if value >= t:
                return p
        return 0

    def score_bulk(self, values: np.ndarray) -> np.ndarray:
        conditions = [values >= t for t in self.thresholds]
        return np.select(conditions, self.points, default=0)


class RangeRule:
    """
    Scoring rule based on inclusive ranges (e.g., 30 <= x <= 110).
    """

    def __init__(self, ranges: list[tuple[float, float]], points: list[int]):
        self.ranges = ranges
        self.points = points

    def score(self, value: float) -> int:
        for (low, high), p in zip(self.ranges, self.points):
            if low <= value <= high:
                return p
        return 0

    def score_bulk(self, values: np.ndarray) -> np.ndarray:
        conditions = [(values >= low) & (values <= high) for low, high in self.ranges]
        return np.select(conditions, self.points, default=0)


class InverseThresholdRule:
    """
    Scoring rule based on ascending thresholds (e.g., < 5, < 8, etc.).
    Useful for values where lower is better, like magnitude.
    """

    def __init__(self, thresholds: list[float], points: list[int], default_points: int = 1):
        self.thresholds = thresholds
        self.points = points
        self.default_points = default_points

    def score(self, value: float) -> int:
        for t, p in zip(self.thresholds, self.points):
            if value < t:
                return p
        return self.default_points

    def score_bulk(self, values: np.ndarray) -> np.ndarray:
        conditions = [values < t for t in self.thresholds]
        return np.select(conditions, self.points, default=self.default_points)


class MoonPenaltyRule:
    """
    Special rule for Moon Penalty scoring.
    """

    @staticmethod
    def score(separation: float, is_narrowband: bool) -> float:
        if is_narrowband:
            return 20.0
        return float(max(0.0, 20.0 - (separation * 0.22)))

    @staticmethod
    def score_bulk(separations: np.ndarray, is_narrowband: bool) -> np.ndarray:
        if is_narrowband:
            return np.full(len(separations), 20.0)
        return np.maximum(0.0, 20.0 - (separations * 0.22))


# Defined Scoring Rules
ALTITUDE_RULE = ThresholdRule([65, 50, 35, 20], [30, 25, 18, 10])
WINDOW_RULE = ThresholdRule([5, 3, 2, 1], [20, 16, 12, 8])
FOV_RULE = RangeRule([(30, 110), (10, 200)], [30, 18])
BRIGHTNESS_RULE = InverseThresholdRule([5, 8, 11], [10, 7, 4])
MOON_RULE = MoonPenaltyRule()
