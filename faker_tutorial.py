# -*- coding: utf-8 -*-
"""faker_tutorial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c2roTh4mDJVPCW82t7A8lcAhv7thfI3z
"""

pip install faker

from faker import Faker
fake= Faker()

print(fake.name())           # Generates a random name
print(fake.first_name())     # Random first name
print(fake.last_name())      # Random last name
print(fake.email())          # Random email address
print(fake.job())            # Random job title
print(fake.phone_number())   # Random phone number

print(fake.address())        # Random full address
print(fake.city())           # Random city name
print(fake.country())        # Random country name
print(fake.zipcode())        # Random zip code

fake = Faker('en_IN')   # For Indian locale
print(fake.name())      # Generates a name in the Indian format
print(fake.address())
print(fake.city())
print(fake.country())
print(fake.postcode())

# Create a list of fake user profiles
for _ in range(5):
    print(fake.profile())

"""Creating a List of Fake Data"""

import pandas as pd

data = {
    'Name': [fake.name() for _ in range(10)],
    'Email': [fake.email() for _ in range(10)],
    'Address': [fake.address() for _ in range(10)],
    'Job': [fake.job() for _ in range(10)]
}

df = pd.DataFrame(data)
df.head()

