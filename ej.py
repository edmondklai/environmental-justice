from censusAPI import my_Census
from config import API_KEY
import pandas as pd

def main():
    c = my_Census(API_KEY)
    c.set_year("2015")
    c.set_survey("acs5")
    c.set_field(["NAME",
                 "GEOID",
                 "B17017_001E",
                 "B17017_002E",
                 "B02001_001E",
                 "B02001_003E",
                 "B02001_004E",
                 "B02001_005E",
                 "B02001_006E",
                 "B02001_007E",
                 "B02001_008E",
                 "B03003_001E",
                 "B03003_003E"
                 ])

    c.set_geoFilter(["for=block+group:*",
                     "in=tract:*",
                     "in=county:19",
                     "in=state:17"])

    c.contruct_query()
    cesnus_frame = c.get()
    print(a.head())
    censsu_frame.to_csv("outFile", sep=',', header=True)


if __name__ == '__main__':
    main()
