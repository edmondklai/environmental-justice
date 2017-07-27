import urllib.request
import pandas as pd


class my_Census:
    def __init__(self, API_KEY):
        self.key = API_KEY
        self.year = ""
        self.survey = ""
        self.fields = []
        self.filter = []
        self.query = ""


    def get_API_KEY(self):
        print(self.key)


    def set_year(self, year):
        self.year = year


    def set_survey(self, survey):
        self.survey = survey


    def set_field(self, fields):
        for field in fields:
            self.fields.append(field)


    def set_geoFilter(self, filter):
        for criteria in filter:
            self.filter.append(criteria)


    def contruct_query(self):
        self._checkError()

        fields = ",".join(self.fields)
        criteria = "&".join(self.filter)
        baseQuery = "https://api.census.gov/data/{}/{}?get={}&{}&key={}".format(
            self.year,
            self.survey,
            fields,
            criteria,
            self.key
        )
        self.query = baseQuery
        print(self.query)


    def download_data(self):
        self._checkError()

        request = urllib.request.Request(self.query)
        response = urllib.request.urlopen(request)
        return(pd.read_json(response))


    def _checkError(self):
        if self.year == ""
            raise ValueError("Year has not been set")
        elif self.survey == ""
            raise ValueError("Survey has not been set")
        elif self.fields == []
            raise ValueError("Fields have not been set")
        elif self.set_geoFilter == []
            raise ValueError("Geofilter has not been set")
        elif self.query == ""
            raise ValueError("Query has not been set")





