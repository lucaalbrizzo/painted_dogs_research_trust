import os
import pandas as pd
import helper
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

cols_date = ["date"]
traffic = helper.upload_csv("cleaned_traffic_sept.csv", cols_date)

cols_to_keep = ["date", "company", "country", "speed"]
traffic = traffic[cols_to_keep]

NUM_ROW_STG_1 = 90
NUM_ROW_STG_2 = 550

metadata_stg01 = SingleTableMetadata()
metadata_stg01.detect_from_dataframe(traffic)

metadata_stg01.update_column(
    column_name="date", sdtype="datetime", datetime_format="%Y-%m-%d"
)

metadata_stg01.update_column(column_name="company", sdtype="company", pii=True)

metadata_stg01.update_column(
    column_name="speed", sdtype="numerical", computer_representation="Float"
)

synthesizer_stg01 = GaussianCopulaSynthesizer(
    metadata_stg01, numerical_distributions={"speed": "beta"}
)
synthesizer_stg01.fit(traffic)
synthetic_data_stg01 = synthesizer_stg01.sample(num_rows=NUM_ROW_STG_1)

company_unique = synthetic_data_stg01[["company", "country"]].drop_duplicates(
    subset="company"
)
synthetic_data_stg01 = synthetic_data_stg01.drop(columns="country")

metadata_stg02 = SingleTableMetadata()
metadata_stg02.detect_from_dataframe(synthetic_data_stg01)

metadata_stg02.update_column(
    column_name="date", sdtype="datetime", datetime_format="%Y-%m-%d"
)

metadata_stg02.update_column(column_name="company", sdtype="categorical")

metadata_stg02.update_column(
    column_name="speed", sdtype="numerical", computer_representation="Float"
)

synthesizer_stg02 = GaussianCopulaSynthesizer(
    metadata_stg02, numerical_distributions={"speed": "beta"}
)
synthesizer_stg02.fit(synthetic_data_stg01)
synthetic_data_stg02 = synthesizer_stg02.sample(num_rows=NUM_ROW_STG_2)

synthetic_traffic_data = pd.merge(
    synthetic_data_stg02, company_unique, how="left", on="company"
)

SAVE_DIR = "../data"
os.makedirs(SAVE_DIR, exist_ok=True)
FILE_NAME = "synthetic_traffic.csv"
path = os.path.join(SAVE_DIR, FILE_NAME)
synthetic_traffic_data.to_csv(path, index=False, date_format="%Y-%m-%d")
