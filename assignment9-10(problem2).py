amt = 0
def main():
    input_data()
    output_data()

def input_data():
    global amt
    object_file = open("text.txt", "r")
    line = object_file.readlines()
    for entry in line:
        list = entry.split(",")
        amount = list[2]
        amount = amount.lstrip("$")
        amount = amount.rstrip("\n")
        amt = amt + float(amount)
    object_file.close()


def output_data():
   file_object = open("text.txt", "a")
   file_object.write("\nTotal amount spend : $"+str(amt))
   file_object.close()

main()
