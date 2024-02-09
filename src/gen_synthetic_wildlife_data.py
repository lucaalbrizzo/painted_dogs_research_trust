import os
import pandas as pd
import helper
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

cols_date = ["image_date", "date_time"]
newdata_tidy = helper.upload_csv("tidy_wildlife_newdata.csv", cols_date)
cols_to_drop = ["image_date", "image_yr", "image_hr"]
newdata_tidy = newdata_tidy.drop(columns=cols_to_drop)

# make image_date as primary key
newdata_tidy = newdata_tidy.drop_duplicates("image_name", ignore_index=True)

anim_diet = newdata_tidy[["anim_type", "anim_spotted"]]
anim_diet = anim_diet.drop_duplicates(ignore_index=True)

newdata_tidy = newdata_tidy.drop(columns=["anim_type"])

NUM_ROWS = 20000

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(newdata_tidy)

metadata.update_column(
    column_name="image_name",
    sdtype="id",
    regex_format="CT1[2-7]_[1-9]{6}_[0-9]{4}\.JPG",
)

metadata.update_column(
    column_name="date_time", sdtype="datetime", datetime_format="%Y-%m-%d %H:%M:%S"
)

metadata.update_column(
    column_name="temperature", sdtype="numerical", computer_representation="Float"
)

metadata.set_primary_key(column_name="image_name")


synthesizer_gauss = GaussianCopulaSynthesizer(metadata)
synthesizer_gauss.fit(newdata_tidy)
synthetic_data_gauss = synthesizer_gauss.sample(num_rows=NUM_ROWS)


synthetic_wildlife_data = pd.merge(
    synthetic_data_gauss, anim_diet, how="left", on="anim_spotted"
)
synthetic_wildlife_data["image_date"] = synthetic_wildlife_data["date_time"].dt.date
synthetic_wildlife_data["image_hr"] = synthetic_wildlife_data["date_time"].dt.hour
synthetic_wildlife_data["image_yr"] = synthetic_wildlife_data["date_time"].dt.year
synthetic_wildlife_data["temperature"] = (
    pd.to_numeric(synthetic_wildlife_data["temperature"], errors="coerce")
    .round(0)
    .astype("Int64")
)

SAVE_DIR = "../data"
os.makedirs(SAVE_DIR, exist_ok=True)
FILE_NAME = "synthetic_wildlife.csv"
path = os.path.join(SAVE_DIR, FILE_NAME)
synthetic_wildlife_data.to_csv(path, index=False, date_format="%Y-%m-%d %H:%M:%S")
