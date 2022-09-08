from databuilder.query_language import Dataset

from lib import pick_backend_tables

patients, = pick_backend_tables()

index_year = 2022
min_age = 18
max_age = 80

year_of_birth = patients.date_of_birth.year
age = index_year - year_of_birth

dataset = Dataset()
dataset.set_population((age >= min_age) & (age <= max_age))
dataset.age = age
