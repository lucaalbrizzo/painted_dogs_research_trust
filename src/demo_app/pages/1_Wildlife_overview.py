import streamlit as st
import os
import pandas as pd
import seaborn as sns

st.title("Overview of animal activity")


@st.cache_data
def upload_csv(filename, date_list=None):
    FILE_PATH = os.path.join("..", "..", "data", filename)
    df = pd.read_csv(FILE_PATH, parse_dates=date_list)
    return df


cols_date = ["image_date", "date_time"]
newdata_tidy = upload_csv("tidy_wildlife_newdata.csv", cols_date)

st.sidebar.info("Enter your preferences below")
unique_anim_type = sorted(newdata_tidy["anim_type"].unique())
selected_anim_types = st.sidebar.multiselect(
    "Select one or multiple animal types", unique_anim_type, unique_anim_type
)

unique_image_yr = sorted(newdata_tidy["image_yr"].unique())
selected_image_yr = st.sidebar.multiselect(
    "Select one or multiple years", unique_image_yr, unique_image_yr
)

sns.set_style("whitegrid")
g = sns.catplot(
    data=newdata_tidy.query(
        "anim_type in @selected_anim_types and image_yr in @selected_image_yr"
    ),
    kind="count",
    y="anim_spotted",
    col="anim_type",
    col_wrap=2,
    sharey=False,
    sharex=False,
    color="#8BADE1",
)
(
    g.set_axis_labels("Count of species spotted", "Species spotted").set_titles(
        "Animal type: {col_name}", weight="bold"
    )
)

st.pyplot(g)
