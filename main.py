import pandas

data = pandas.read_csv("student_data.csv")
data_dict = data.to_dict()
data_list = data["Marks"].to_list()
data_mean = data.Marks.mean()
data_max = data.Marks.max()


# Get row for data 

# Gayheart_data = data[data.Students == "Gayheart"]
# k_data = data[data.Students == "Kister"]
# print(Gayheart_data.Rank)
# print(k_data.Marks)

# Individual with the highest mark 
print(f"Individual with Highest marks :\n {data[data.Marks == data.Marks.max()]}")

print(f"The mean of the data is : {data_mean}")
print(f"The maximum marks in the data is : {data_max}")