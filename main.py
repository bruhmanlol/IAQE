import colorama
err = colorama.Fore.RED
re = colorama.Fore.WHITE
import gspread
gc = gspread.service_account(filename="data.json")
sh = gc.open_by_key("1y7E1dlbAmoLMs_eTs3BHYfOaVmPQky9Wgq5QwTNZy0s")
worksheet = sh.sheet1

def replace():
    Values = input("Enter the ID: ")
    Values2 = input("Enter the Name:")
    Values3 = input("Enter the quantity: ")
    row = int(input("Which row number?"))
    worksheet.update_cell(row, 1, Values)
    worksheet.update_cell(row, 2, Values2)
    worksheet.update_cell(row, 3, Values3)
    print("Values have been entered")

def delete():
    row = int(input("Which row number?"))
    try:
      worksheet.delete_rows(row)
      print("Value has been deleted")
    except:
      print(err+"NOT WORKING"+re)

while True:
  res = worksheet.get_all_records()
  print(res)
  action = input("Do you want to delete, replace or add a column?")
  if action == "add":
    Values = input("Enter the ID: ")
    Values2 = input("Enter the Name:")
    Values3 = input("Enter the quantity: ")
    user = [Values, Values2, Values3]
    worksheet.insert_row(user, 2)
    print("Values have been entered")
  if action == "replace":
    replace()
  if action == "delete":
    delete()