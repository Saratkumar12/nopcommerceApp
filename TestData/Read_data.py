import execel_utils

file = r"C:\Users\DELL\PycharmProjects\nopcommerceApp\TestData\Test_Data.xlsx"

username = execel_utils.read_data(file, "Sheet1", 2, 1)
password = execel_utils.read_data(file, "Sheet1", 2, 2)

print(username)
print(password)

execel_utils.write_data(file, "Sheet1", 3, 1, "Rama")
execel_utils.write_data(file, "Sheet1", 3, 2, "S@rat")


