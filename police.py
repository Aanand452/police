import numpy as np
import pandas as pd


def police():

    police_df = pd.read_csv("/Users/anandkumar/Downloads/data/police.csv")

    print(police_df)

#    Before Analayzing the data go through the whole dataframe

    print(police_df.head())

    print(police_df.columns)

    print(police_df.shape)

    print(police_df.index)

    print(police_df.value_counts())

    print(police_df.dtypes)

    print(police_df.nunique())

    print(police_df.isnull().sum())

    # Remove the column that only contains missing values
    print(police_df.isnull().sum())

    print(police_df.drop(columns="country_name", inplace=False))
    print(police_df)

   # For speeding,were Men or Women stooped more often
    print(police_df[police_df.violation ==
          "Speeding"].driver_gender.value_counts())

    # Does gender affect who gets searched during stop?

    print(police_df.groupby('driver_gender').search_conducted.sum())
    print(police_df.search_conducted.value_counts())

    # what is the mean stop duration

    print(police_df.stop_duration.value_counts())

    # print(police_df["stop_duration"]=police_df["stop_duration"].map({"0-15 Min": 7.5, "16-30 Min": 24, "30+ Min": 45}))
    #
    print(police_df['stop_duration'].mean())

    # compare the age distrubation of each voilation
    print(police_df.groupby('violation').driver_age.describe())


police()
