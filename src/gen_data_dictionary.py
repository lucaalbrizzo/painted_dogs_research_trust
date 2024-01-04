from helper import DatasetVariable
import pandas as pd
import os

newdata = []

record_number = DatasetVariable(
    name="record_number",
    data_type="int",
    description="unclear description",
    example_values="604, 1680",
    comments="Duplicates exist. This variable doesn't seeem to an id",
)
newdata.append(record_number)


camera_trap = DatasetVariable(
    name="camera_trap",
    data_type="str",
    description="types of camera trap",
    example_values="CT17, PTC07 PANDA, 8KF OPEN, 5A PM CLOSED",
    comments="Some entries, like '5A PM CLOSED', may not be type of camera trap ",
)
newdata.append(camera_trap)


entered_date = DatasetVariable(
    name="entered_date",
    data_type="datetime",
    description="date when the image was coded into the spreadsheet",
    example_values="2020-05-01, 2021-08-03",
    comments="",
)
newdata.append(entered_date)


student_or_volunteer = DatasetVariable(
    name="student_or_volunteer",
    data_type="str",
    description="name of student or volunteer who coded the image into the spredsheet",
    example_values="FIRSTNAME LASTNAME",
    comments="",
)
newdata.append(student_or_volunteer)


first_image = DatasetVariable(
    name="first_image",
    data_type="str",
    description="?",
    example_values="PTO 02 310723_0127.JPG, CT13B 020323 0004.JPG, 24/06/2023 03:57AM",
    comments="Some values look like datetime (e.g., 24/06/2023 03:57AM)",
)
newdata.append(first_image)


open_or_closed = DatasetVariable(
    name="open_or_closed",
    data_type="str",
    description="?",
    example_values="OPEN, CLOSED",
    comments="",
)
newdata.append(open_or_closed)


image_name = DatasetVariable(
    name="image_name",
    data_type="str",
    description="image name",
    example_values="CT30 140323 0013.JPG, ZXCPL CT26 140323 0740.JPG",
    comments="",
)
newdata.append(image_name)


date_time = DatasetVariable(
    name="date_time",
    data_type="datetime",
    description="date and time of observation",
    example_values="2019-09-30 00:05:00, 2019-08-07 00:08:00",
    comments="",
)
newdata.append(date_time)


am_pm_ml = DatasetVariable(
    name="am_pm_ml",
    data_type="str",
    description="?",
    example_values="AM, PM, ML, 3, 2",
    comments="Values of 3 and 2 may have corresponding values to AM/PM/ML",
)
newdata.append(am_pm_ml)


temperature = DatasetVariable(
    name="temperature",
    data_type="float",
    description="temperature (in Celcius) when the image was taken?",
    example_values="-1, 7, 68",
    comments="",
)
newdata.append(temperature)


moon_phase = DatasetVariable(
    name="moon_phase",
    data_type="str",
    description="moon phase",
    example_values="WAXING CRESCENT, NEW MOON",
    comments="",
)
newdata.append(moon_phase)


species_category = DatasetVariable(
    name="species_category",
    data_type="str",
    description="species category",
    example_values="herbivore, omnivore, bird, unknown",
    comments="",
)
newdata.append(species_category)

species_category_2 = DatasetVariable(
    name="species_category_2",
    data_type="str",
    description="species category",
    example_values="herbivore, omnivore, bird, unknown",
    comments="",
)
newdata.append(species_category_2)


carnivore = DatasetVariable(
    name="carnivore",
    data_type="str",
    description="types of carnivore spotted in the image",
    example_values="104=side-striped jackal, 103=painted dog",
    comments="",
)
newdata.append(carnivore)


herbivore = DatasetVariable(
    name="herbivore",
    data_type="str",
    description="types of herbivore spotted in the image",
    example_values="201=elephant, 210=waterbuck",
    comments="",
)
newdata.append(herbivore)


insectivore = DatasetVariable(
    name="insectivore",
    data_type="str",
    description="types of insectivore spotted in the image",
    example_values="302=aardvark, 301=aardwolf",
    comments="",
)
newdata.append(insectivore)

omnivore = DatasetVariable(
    name="omnivore",
    data_type="str",
    description="types of omnivore spotted in the image",
    example_values="401=baboon, 402=vervet monkey",
    comments="",
)
newdata.append(omnivore)

bird = DatasetVariable(
    name="bird",
    data_type="str",
    description="types of bird spotted in the image",
    example_values="502=guinea fowl, 503=dove",
    comments="",
)
newdata.append(bird)


non_animal = DatasetVariable(
    name="non_animal",
    data_type="str",
    description="types of non_animal spotted in the image",
    example_values="601=people, 602=vehicles",
    comments="",
)
newdata.append(non_animal)

license_plate = DatasetVariable(
    name="license_plate",
    data_type="str",
    description="vehicles license plates",
    example_values="ADZ 5141, blurred, AxC 21xx",
    comments="Some values are unidentified",
)
newdata.append(license_plate)


unknown = DatasetVariable(
    name="unknown",
    data_type="str",
    description="?",
    example_values="white truck, Yes, X",
    comments="",
)
newdata.append(unknown)

other = DatasetVariable(
    name="other",
    data_type="str",
    description="?",
    example_values="night jar, squirrel",
    comments="",
)
newdata.append(other)

unidentified_animal = DatasetVariable(
    name="unidentified_animal",
    data_type="str",
    description="whether there was any unidentified animal, possibly unidentified animal?",
    example_values="yes, no, jackal",
    comments="",
)
newdata.append(unidentified_animal)


comments = DatasetVariable(
    name="comments",
    data_type="str",
    description="comments on the image, if any",
    example_values="picture seems dark for the time",
    comments="",
)
newdata.append(comments)


checker_initials_and_date = DatasetVariable(
    name="checker_initials_and_date",
    data_type="str",
    description="checker initials and date",
    example_values="jps 5/16/20",
    comments="",
)
newdata.append(checker_initials_and_date)

newdata_dict = [vars(x) for x in newdata]
newdata_df = pd.DataFrame(newdata_dict)

SAVE_DIR = "./data"
os.makedirs(SAVE_DIR, exist_ok=True)
FILE_NAME = "datadictionary_newdata.csv"
path = os.path.join(SAVE_DIR, FILE_NAME)
newdata_df.to_csv(path, index=False)
