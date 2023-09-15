import pandas 

# Creating a Dataframe 

data_dict = {
    "workers": ['Priscilla', 'David', 'Lionel', 'Gayheart', 'Ucal'],
    "Positions": ["General Secretary", "Adminstrator", "Financial Secretary", "Data Analyst", "C# Developer"],
    "salaries": [2000, 3000, 2500, 4000, 1500]
}

# Dataframe 

data = pandas.DataFrame(data_dict)
print(data)

# create a csv file out of the dictionary above 
data.to_csv("workers_data.csv") # this line of code will automatically create a csv file named "workers_data.csv" when the programme is runned
