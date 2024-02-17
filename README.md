![alt text](https://static.wixstatic.com/media/236165_07b8ad912dc74d848eeb5b4643061277~mv2.jpg/v1/fit/w_2500,h_1330,al_c/236165_07b8ad912dc74d848eeb5b4643061277~mv2.jpg)

# PAINTED DOG RESEARCH TRUST DATA PIPELINE



## INTRODUCTION

This is the  Github repository for the collabation project between Statistics Without Borders (SWB) and Painted Dog Research Trust (PDRT).

The main goal of this repository is to show how to build a data pipeline that would allow PDRT to obtain easily insights from the data they collect on field.

The main assumption behind this repository is that the *data that will be used would look like the ones that are in the data folder** (provided by the PDRT team). 

This means that if the data collected by PDRT changes in structure (e.g. new column names) in the future the scripts provided here must be modified in order to run. However, the change should be minimal.

All scripts were written in Python (version 3.10.12) and therefore the user needs Python to be [installed on their machine](https://www.python.org/downloads/). 

Moreover, in order to easily install all the needed libraries, the user might want to [install pip too](https://pip.pypa.io/en/stable/installation/).


## INSTALL LIBRARIES

All needed libraries can be installed via pip
```
pip install -r requirements.txt
```
this will install some common libraries for data analysis.

## CLEANING DATA

All data cleaning should be carried in a [Jupyter notebook](https://jupyter.org/) an interactive development environment used often for data analysis. 

To open a new jupyter notebook, just run in the terminal
```
jupyter notebook
```
Once this is done, go in the **src** folder and run the following notebooks (from beginning to the end):
- **cleaning_speed_data.ipynb** ,  which cleans **"TEST SPEED SUPPLIED WITH SOFTWARE V4.xls"** file containg wildlife data and saves several files called **"cleaned_speed_{n}.csv"** with n representing a spreadsheet 
- **cleaning_traffic_data.ipynb** ,  which cleans **"Traffic Data Master 2022-2 Billy.xlsx"** file containg traffic data and saves a new file **"cleaned_traffic_sept.csv"**  
- **cleaning_wildlife_data.ipynb** , which cleans **"GR merged  CT All with OC Master PDRT  Camera Trap Data Sheet.xlsx"** file containg wildlife data and saves a new file **"cleaned_wildlife_1722.csv"**

## DATA ANALYSIS ON CLEAN DATA

The **src** folder cointains also two notebooks for data analysis using cleaned data:
- **eda_traffic.ipynb** , which performs data analysis about traffic overall and per company 
- **eda_wildlife.ipynb** , which performs data analysis about animal activity per specie, day, ...


 ## INTERACTIVE DASHBOARD

All the results above can be also found in an [interactive dashboard](https://wildlife-and-traffic-dashboard-demo.streamlit.app/)  PDRT using synthetic data, which allows the user to play with data without having to run the Python scripts.

The link above requires Internet connection but a local version can be run by going in the folder **src/demo_app** and run
```
streamlit run Wildlife_and_Traffic_Demo.py 
```

If the users wishes to modify the dashboard can go to the **src/demo_app/pages** folder where all the pages of the dashboard are saved.
