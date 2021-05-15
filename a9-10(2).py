amt = 0
def input_data():
    global amt
    fileObj = open("text.txt", "r")
    line = fileObj.readlines()
    for entry in line:
        list = entry.split(",")
        cost = list[2]
        cost = cost.lstrip("$")
        cost = cost.rstrip("\n")
        amt = amt + float(cost)
    fileObj.close()


def out_data():
   fileWriteObj = open("text.txt", "a")
   fileWriteObj.write("\nTotal amount spend : $"+str(amt))
   fileWriteObj.close()

def main():
    input_data()
    out_data()

main()