import requests
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

INTAKES_URL = "https://data.austintexas.gov/resource/wter-evkm.json"
PARAMS = {
    "animal_type": "Dog",
    "$$app_token": "aBq5AbxH1zKfProvzcMh0h4Dm"
}

def request_intake_data():
    r = requests.get(INTAKES_URL, params=PARAMS)
    df1 = pd.DataFrame(r.json())
    df1 = df1.drop(columns=['datetime2']).fillna('None')
    return df1

def clean_intake_data():
    df = request_intake_data()
    # =============
    # DATA CLEANING
    # =============
    
    # Create empty lists for new columns
    intake_datetime = []
    found_address = []
    found_city = []
    found_state = []
    sex = []
    birthday = []
    # mongoDB won't accept a relative delta variable type
    # age = []
    # instead, this will create the components of the relative delta
    # and store them individually
    age_years = []
    age_months = []
    age_days = []
    primary_breed = []
    secondary_breed = []
    mixed_breed = []
    primary_color = []
    secondary_color = []
    name = []

    for i in df.index:
        # Clean datetime column
        intake_dt = datetime.strptime(df.iloc[i]['datetime'].replace(".000", ""), '%Y-%m-%dT%H:%M:%S')
        intake_datetime.append(intake_dt)

        # Clean location column
        if len(df.iloc[i]['found_location'].split(" in ")) > 1:
            found_address.append(df.iloc[i]['found_location'].split(" in ")[0])
            found_city.append(df.iloc[i]['found_location'].split(" in ")[1].split(" (")[0])
            found_state.append(df.iloc[i]['found_location'].split(" in ")[1].split(" (")[1].replace(")", ""))
        elif "(TX)" in df.iloc[i]['found_location'].split(" in ")[0]:
            found_address.append('None')
            found_city.append(df.iloc[i]['found_location'].split(" in ")[0].split(" (")[0])
            found_state.append(df.iloc[i]['found_location'].split(" in ")[0].split(" (")[1].replace(")", ""))
        else:
            found_address.append(df.iloc[i]['found_location'])
            found_city.append('None')
            found_state.append('None')

        # Clean sex column
        sex.append(df.iloc[i]['sex_upon_intake'].replace("Intact ", "").replace("Neutered ", "").replace("Spayed ", ""))

        # Clean age upon intake column
        intake_age = df.iloc[i]['age_upon_intake'].split(" ")
        if intake_age[0].isnumeric():
            num = int(intake_age[0])
        else:
            num = "Unknown"
        if len(intake_age) > 1:
            duration = (
                intake_age[1]
                .replace("years", "year").replace("year", "years")
                .replace("months", "month").replace("month", "months")
                .replace("weeks", "week").replace("week", "weeks")
                .replace("days", "day").replace("day", "days")
                )
        else:
            duration = "Unknown"
        # Determine birthday
        if num == "Unknown" or duration == "Unknown":
            bday = "Unknown"
            birthday.append(bday)
        else:
            bday = intake_dt - relativedelta(**{duration: num})
            birthday.append(bday)
        # Determine age as of today's date
        if isinstance(bday, datetime):
            age_today = relativedelta(datetime.today(), bday)
            # age.append(age_today)
            age_years.append(age_today.years)
            age_months.append(age_today.months)
            age_days.append(age_today.days)
        else:
            # age.append("Unknown")
            age_years.append("Unknown")
            age_months.append("Unknown")
            age_days.append("Unknown")
        
        # Clean breed column
        if len(df.iloc[i]['breed'].split("/")) > 1:
            primary_breed.append(df.iloc[i]['breed'].split("/")[0].replace(" Mix", ""))
            secondary_breed.append(df.iloc[i]['breed'].split("/")[1].replace(" Mix", ""))
            mixed_breed.append(True)
        else:
            if "Mix" in df.iloc[i]['breed']:
                primary_breed.append(df.iloc[i]['breed'].replace(" Mix", ""))
                secondary_breed.append('Mix')
                mixed_breed.append(True)
            else:
                primary_breed.append(df.iloc[i]['breed'])
                secondary_breed.append('None')
                mixed_breed.append(False)

        # Clean color column
        if len(df.iloc[i]['color'].split("/")) > 1:
            primary_color.append(df.iloc[i]['color'].split("/")[0])
            secondary_color.append(df.iloc[i]['color'].split("/")[1])
        else:
            primary_color.append(df.iloc[i]['color'])
            secondary_color.append('None')

        # Clean name column
        name.append(df.iloc[i]['name'].replace("*", ""))

    # Compile clean dataframe
    df2 = pd.DataFrame({
        "animal_id": df["animal_id"],
        "intake_datetime": intake_datetime,
        "found_address": found_address,
        "found_city": found_city,
        "found_state": found_state,
        "intake_type": df["intake_type"],
        "intake_condition": df["intake_condition"],
        "sex": sex,
        "birthday": birthday,
        # commenting out the age column because mongoDB can't deal with this data type
        # will write a script to extract age on the pull side
        # "age": age,
        # instead storing components of age (relative delta) individually
        "age_years": age_years,
        "age_months": age_months,
        "age_days": age_days,
        "mixed_breed": mixed_breed, 
        "primary_breed": primary_breed, 
        "secondary_breed": secondary_breed,
        "primary_color": primary_color,
        "secondary_color": secondary_color,
        "name": name, 
        })

    return df2

dogs_df = clean_intake_data()

print("""
========================================
SAMPLE OF DOG INTAKES (FIRST 20 ENTRIES)
========================================
""")

print(dogs_df.head(20))
