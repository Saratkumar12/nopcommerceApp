import excel_utlts

file = "D:\ManoharSir_SeleniumWithJava_Class\Batch8AM_Automation\InterviwPre\Python_data_driven_testing\My_utils_file.xlsx"

# Writing data
excel_utlts.write_data(file, "Sheet1", 1, 1, "Name")
excel_utlts.write_data(file, "Sheet1", 1, 2, "Age")
excel_utlts.write_data(file, "Sheet1", 1, 3, "Mobile")

excel_utlts.write_data(file, "Sheet1", 2, 1, "RK")
excel_utlts.write_data(file, "Sheet1", 2, 2, "45")
excel_utlts.write_data(file, "Sheet1", 2, 3, "99883837373")

# Row and column count
print(excel_utlts.get_row_count(file, "Sheet1"))
print(excel_utlts.get_coloumn_count(file, "Sheet1"))

# Fill colors
excel_utlts.fill_red(file, "Sheet1", 1, 1)
excel_utlts.fill_green(file, "Sheet1", 1, 2)

# Read data
print(excel_utlts.read_data(file, "Sheet1", 1, 1))
print(excel_utlts.read_data(file, "Sheet1", 1, 2))
print(excel_utlts.read_data(file, "Sheet1", 1, 3))