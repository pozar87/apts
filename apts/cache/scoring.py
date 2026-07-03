_SCORE_CACHE = {}


def get_cached_score(scorer_id, object_id, timestamp):
    """
    Retrieves a cached score result.
    """
    return _SCORE_CACHE.get((scorer_id, object_id, timestamp))


def set_cached_score(scorer_id, object_id, timestamp, result):
    """
    Caches a score result.
    """
    _SCORE_CACHE[(scorer_id, object_id, timestamp)] = result


def clear_scoring_cache():
    """
    Clears the scoring cache.
    """
    global _SCORE_CACHE
    _SCORE_CACHE = {}
