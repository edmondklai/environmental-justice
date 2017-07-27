from censusAPI import my_Census
from config import API_KEY


def main():
    year = "2015"
    survey = "acs5"
    fields = ["NAME",
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
              "B03003_003E"]
    geoFilter = ["for=block+group:*",
                 "in=tract:*",
                 "in=county:19",
                 "in=state:17"]


    c = my_Census(API_KEY)
    c.set_year(year)
    c.set_survey(survey)
    c.set_field(fields)
    c.set_geoFilter(geoFilter)
    c.contruct_query()
    census_frame = c.get()

    print(census_frame.head())
    census_frame.to_csv("outFile.csv", sep=',', header=True)


if __name__ == '__main__':
    main()
