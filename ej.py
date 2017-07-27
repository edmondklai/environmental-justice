from censusAPI import my_Census
from config import API_KEY
import pandas as pd

def main():
    c = my_Census(API_KEY)
    c.set_year("2015")
    c.set_survey("acs5")
    c.set_field(["NAME",
                 "GEOID",
                 "B05010_001E",
                 "B01001_001E"])

    c.set_geoFilter(["for=block+group:*",
                     "in=tract:*",
                     "in=county:19",
                     "in=state:17"])

    c.contruct_query()
    a = c.get()
    print(a.head())
    a.to_csv("file", sep=',', header=True)


if __name__ == '__main__':
    main()
