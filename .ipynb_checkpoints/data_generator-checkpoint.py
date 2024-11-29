import pandas as pd
from faker import Faker
import random

class DatasetGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate(self, rows, columns, file_format, file_path):
        data = []
        for _ in range(rows):
            row = {}
            for name, col_type in columns:
                row[name] = self.generate_data(col_type)
            data.append(row)

        df = pd.DataFrame(data)

        if file_format == "CSV":
            df.to_csv(file_path, index=False)
        elif file_format == "JSON":
            df.to_json(file_path, orient="records", indent=4)
        elif file_format == "TXT":
            df.to_csv(file_path, index=False, sep="\t")


    def generate_data(self, col_type):
        if col_type == "Name":
            return self.fake.name()
        elif col_type == "Age":
            return random.randint(18, 80)
        elif col_type == "Datetime":
            return self.fake.date_time_this_decade()
        elif col_type == "Phone":
            return self.fake.phone_number()
        elif col_type == "Email":
            return self.fake.email()
        elif col_type == "Address":
            return self.fake.address()
        elif col_type == "City":
            return self.fake.city()
        elif col_type == "Country":
            return self.fake.country()
        elif col_type == "Zip Code":
            return self.fake.zipcode()
        elif col_type == "Company":
            return self.fake.company()
        elif col_type == "Job Title":
            return self.fake.job()
        elif col_type == "Salary":
            return round(random.uniform(30000, 200000), 2)
        elif col_type == "Integer":
            return random.randint(0, 100)
        elif col_type == "Float":
            return round(random.uniform(0, 100), 2)
        elif col_type == "Boolean":
            return random.choice([True, False])
        elif col_type == "Date":
            return self.fake.date_this_decade()
        elif col_type == "Text":
            return self.fake.text(max_nb_chars=50)
        elif col_type == "Random String":
            return self.fake.lexify(text="?????")
        elif col_type == "URL":
            return self.fake.url()
        elif col_type == "IPAddress":
            return self.fake.ipv4()
        elif col_type == "Credit Card":
            return self.fake.credit_card_number()
        elif col_type == "SSN":
            return self.fake.ssn()
        elif col_type == "Latitude":
            return round(random.uniform(-90, 90), 6)
        elif col_type == "Longitude":
            return round(random.uniform(-180, 180), 6)
        else:
            return None
