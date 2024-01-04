import pandas as pd
import numpy as np
import datetime


class DatasetVariable(object):
    def __init__(
        self,
        name: str,
        data_type: str,
        description: str,
        example_values: str,
        comments="",
    ):
        self.name = name
        self.data_type = data_type
        self.description = description
        self.example_values = example_values
        self.comments = comments


def drop_cols_with_prefix(df, prefix_to_drop):
    columns_to_drop = [col for col in df if col.startswith(prefix_to_drop)]
    return df.drop(columns=columns_to_drop)


def remove_spaces_in_colnames(df):
    """A function that removes special character and trailing spaces in column names"""
    df.columns = df.columns.str.replace("  ", " ")
    df_clean = df.rename(columns=lambda x: x.strip())
    return df_clean


def snake_style_colnames(df):
    """A function that convert column names into snake style"""
    df.columns = df.columns.str.lower()
    df_clean = df.rename(columns=lambda x: x.replace(" ", "_"))
    return df_clean


def check_range(series):
    min_series = series.min()
    max_series = series.max()
    range_series = max_series - min_series
    print(f"min: {min_series}\nmax: {max_series}\nrange: {range_series}")


def check_missing_values(series):
    num_obs = len(series)
    num_missing = series.isnull().sum()
    pct_missing = np.round((num_missing / num_obs) * 100, decimals=4)
    print(
        f"number of observations: {num_obs}\nnumber of missing values: {num_missing}\npct of missing values: {pct_missing}%"
    )


def find_duplicate_rows(df, colnames=None):
    duplicates = df.duplicated(subset=colnames, keep=False)
    return df[duplicates]


def clean_camera_trap(value):
    if pd.isna(value):
        return value
    value = value.strip()
    value = value.upper()
    value = value.replace("CT ", "CT")
    value = value.replace("PTC ", "PTC")
    value = value.replace("PTO ", "PTO")
    value = value.replace("HOT SPOT", "HOTSPOT")
    value = value.replace("  ", " ")
    return value


def remove_nondatetime(value):
    if pd.isna(value) or isinstance(value, datetime.datetime):
        return value
    return np.nan


def strip_upper(value):
    """A function to remove trailing spaces, make upper cases"""
    if not isinstance(value, str):
        return value
    value = value.strip()
    value = value.upper()
    return value


def strip_lower_equalsign(value):
    if pd.isna(value):
        return value
    value = value.strip()
    value = value.lower()
    value = value.replace(" =", "=")
    value = value.replace("= ", "=")
    return value


def clean_temperature(value):
    if not isinstance(value, str):
        return value
    value = value.replace("F", "")
    value = value.replace("`", "")  # assumption: all values in string are in Fahrenheit
    value = int(value)
    value = (value - 32) * (5 / 9)  # convert Fahrenheit to Celcius
    return value


def clean_moon_phase(value):
    if pd.isna(value):
        return value
    value = value.strip()
    value = value.upper()
    value = value.replace("= ", "=")
    value = value[2:]
    return value


def clean_species_category(value):
    if pd.isna(value):
        return value
    elif not isinstance(value, str):
        values_mapping = {
            1: "carnivore",
            2: "herbivore",
            3: "unknown",  # assumption: 3 is unknown
            4: "omnivore",
            5: "bird",
            6: "unknown",  # assumption: 6 is unknown
        }
        return values_mapping[value]
    else:
        value = value.lower()
        value = value.replace("birds", "bird")
        value = value.replace(" ", "unknown")
        value = value[2:]
        value = value.replace("known", "unknown")
        return value


def clean_insectivore(value):
    if pd.isna(value):
        return value
    elif not isinstance(value, str):
        return np.nan
    else:
        value = value.strip()
        value = value.lower()
        value = value.replace(" =", "=")
        value = value.replace("= ", "=")
        return value
