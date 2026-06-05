from typing import Any, Dict, Iterable, cast

import pandas as pd

from ..i18n import get_language, gettext_


def _get_unique_values(series: pd.Series) -> Iterable:
    """Extracts unique values from a series, handling unhashable types."""
    try:
        return series.unique()
    except TypeError:
        # Fallback for columns containing unhashable types (e.g., lists)
        unique_values = []
        seen = set()
        for item in series:
            h_item = tuple(item) if isinstance(item, list) else item
            if h_item not in seen:
                seen.add(h_item)
                unique_values.append(item)
        return unique_values


def _build_translation_map(unique_values: Iterable) -> Dict[Any, Any]:
    """Builds a mapping from original values to translated ones."""
    translation_map = {}
    for val in unique_values:
        if isinstance(val, list):
            translation_map[tuple(val)] = [gettext_(item) for item in val]
        elif isinstance(val, str):
            translation_map[val] = gettext_(val)
        else:
            translation_map[val] = val
    return translation_map


def _apply_translation(series: pd.Series, translation_map: Dict) -> pd.Series:
    """Applies the translation map to a series."""
    # Check if we have any list keys in the map
    has_list = any(isinstance(k, tuple) for k in translation_map.keys())

    if has_list:
        # Lists are not hashable, so we use tuples for the mapping but still
        # need to handle input list types correctly in apply.
        return cast(
            pd.Series,
            series.apply(
                lambda x: (
                    translation_map[tuple(x)]
                    if isinstance(x, list)
                    else translation_map.get(x, x)
                )
            ),
        )
    else:
        return cast(pd.Series, series.apply(lambda x: translation_map.get(x, x)))


def translate_events(df: pd.DataFrame) -> pd.DataFrame:
    """
    Translates event data in a DataFrame to the current language.
    Optimized for large datasets with repeated strings.
    """
    if df.empty:
        return df

    # Optimization: Early return if language is English (no translation needed)
    if get_language() == "en":
        return df

    columns_to_translate = [
        "event",
        "type",
        "shower_name",
        "phase",
        "object",
        "object1",
        "object2",
        "planets",
    ]

    for col in columns_to_translate:
        if col in df.columns:
            col_series = cast(pd.Series, df[col])
            unique_values = _get_unique_values(col_series)
            translation_map = _build_translation_map(unique_values)
            df[col] = _apply_translation(col_series, translation_map)

    return df
