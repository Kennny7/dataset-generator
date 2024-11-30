import pandas as pd
from faker import Faker
import random

class DatasetGenerator:
    def __init__(self):
        self.fake = Faker()  # Initialize Faker instance

    def generate(self, rows: int, columns: list, file_format: str, file_path: str) -> None:
        data = []  # List to store generated rows of data
        
        for _ in range(rows):
            row = {}
            
            for name, col_type in columns:
                row[name] = self.generate_data(col_type)
                
            data.append(row)

        df = pd.DataFrame(data)  # Convert list of dictionaries to DataFrame

        if file_format == "CSV":
            df.to_csv(file_path, index=False)  # Save as CSV without row indices
        elif file_format == "JSON":
            df.to_json(file_path, orient="records", indent=4)  # Save as JSON with pretty formatting
        elif file_format == "TXT":
            df.to_csv(file_path, index=False, sep="\t")  # Save as TXT with tab-separated values

    def generate_data(self, col_type: str):
        if col_type == "Name":
            return self.fake.name()  # Random name
        elif col_type == "Age":
            return random.randint(18, 80)  # Random age between 18 and 80
        elif col_type == "Datetime":
            return self.fake.date_time_this_decade()  # Random date-time in this decade
        elif col_type == "Phone":
            return self.fake.phone_number()  # Random phone number
        elif col_type == "Email":
            return self.fake.email()  # Random email address
        elif col_type == "Address":
            return self.fake.address()  # Random address
        elif col_type == "City":
            return self.fake.city()  # Random city name
        elif col_type == "Country":
            return self.fake.country()  # Random country name
        elif col_type == "Zip Code":
            return self.fake.zipcode()  # Random zip code
        elif col_type == "Company":
            return self.fake.company()  # Random company name
        elif col_type == "Job Title":
            return self.fake.job()  # Random job title
        elif col_type == "Salary":
            return round(random.uniform(30000, 200000), 2)  # Random salary between 30,000 and 200,000
        elif col_type == "Integer":
            return random.randint(0, 100)  # Random integer between 0 and 100
        elif col_type == "Float":
            return round(random.uniform(0, 100), 2)  # Random float between 0 and 100
        elif col_type == "Boolean":
            return random.choice([True, False])  # Random boolean value
        elif col_type == "Date":
            return self.fake.date_this_decade()  # Random date within this decade
        elif col_type == "Text":
            return self.fake.text(max_nb_chars=50)  # Random text (max 50 chars)
        elif col_type == "Random String":
            return self.fake.lexify(text="?????")  # Random string of 5 characters
        elif col_type == "URL":
            return self.fake.url()  # Random URL
        elif col_type == "IPAddress":
            return self.fake.ipv4()  # Random IP address
        elif col_type == "Credit Card":
            return self.fake.credit_card_number()  # Random credit card number
        elif col_type == "SSN":
            return self.fake.ssn()  # Random SSN
        elif col_type == "Latitude":
            return round(random.uniform(-90, 90), 6)  # Random latitude between -90 and 90
        elif col_type == "Longitude":
            return round(random.uniform(-180, 180), 6)  # Random longitude between -180 and 180
        else:
            return None  # If an invalid type is provided, return None
