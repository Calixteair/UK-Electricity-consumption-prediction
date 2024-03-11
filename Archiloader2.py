import pandas as pd


def loaderData():
    df2009 = pd.read_csv("./archive/historic_demand_year_2009.csv")
    df2010 = pd.read_csv("./archive/historic_demand_year_2010.csv")
    df2011 = pd.read_csv("./archive/historic_demand_year_2011.csv")
    df2012 = pd.read_csv("./archive/historic_demand_year_2012.csv")
    df2013 = pd.read_csv("./archive/historic_demand_year_2013.csv")
    df2014 = pd.read_csv("./archive/historic_demand_year_2014.csv")
    df2015 = pd.read_csv("./archive/historic_demand_year_2015.csv")
    df2016 = pd.read_csv("./archive/historic_demand_year_2016.csv")
    df2017 = pd.read_csv("./archive/historic_demand_year_2017.csv")
    df2018 = pd.read_csv("./archive/historic_demand_year_2018.csv")
    df2019 = pd.read_csv("./archive/historic_demand_year_2019.csv")
    df2020 = pd.read_csv("./archive/historic_demand_year_2020.csv")
    df2021 = pd.read_csv("./archive/historic_demand_year_2021.csv")
    df2022 = pd.read_csv("./archive/historic_demand_year_2022.csv")
    df2023 = pd.read_csv("./archive/historic_demand_year_2023.csv")
    df2024 = pd.read_csv("./archive/historic_demand_year_2024.csv")

    df = [df2009, df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021,
          df2022, df2023, df2024]

    for frame in df:
        print(frame.shape)


    df2023_2024 = pd.DataFrame()
    df2019_2024 = pd.DataFrame()
    df2009_2024 = pd.DataFrame()

    list_of_2009_2024 = []
    list_of_2019_2024 = []
    list_of_2023_2024 = []

    columns_to_drop = ['viking_flow', 'scottish_transfer', 'nsl_flow', 'eleclink_flow']
    columns_to_drop2 = ['viking_flow', 'scottish_transfer']
    columns_to_drop3 = ['nsl_flow', 'eleclink_flow']

    for frame in range(0,len(df)):
        print(frame)
        df[frame] = df[frame].rename(columns=str.lower)
        df[frame]['settlement_date'] = pd.to_datetime(df[frame]['settlement_date'], errors='coerce')


    for frame in range(0,len(df)):
        if all(col in df[frame].columns for col in columns_to_drop):
            list_of_2023_2024.append(df[frame])
        if all(col in df[frame].columns for col in columns_to_drop3):
            list_of_2019_2024.append(df[frame])
        list_of_2009_2024.append(df[frame])

    print("list_of_2009_2024", len(list_of_2009_2024))
    print("list_of_2019_2024", len(list_of_2019_2024))
    print("list_of_2023_2024", len(list_of_2023_2024))

    df2009_2024 = pd.concat(list_of_2009_2024, ignore_index=True)
    df2019_2024 = pd.concat(list_of_2019_2024, ignore_index=True)
    df2023_2024 = pd.concat(list_of_2023_2024, ignore_index=True)

    df2019_2024 = df2019_2024.drop(columns=columns_to_drop2, errors='ignore')
    df2009_2024 = df2009_2024.drop(columns=columns_to_drop, errors='ignore')

    print("df2009_2024.shape , expected : 280320   =>", df2009_2024.shape)
    print("df2019_2024.shape , expected : 88012    =>", df2019_2024.shape)
    print("df2023_2024.shape , expected : 18384    =>", df2023_2024.shape)







loaderData()