SOURCE="./source.txt"
LIST="./list.txt"


with open(SOURCE) as source_file:
    contents = source_file.read()

with open(LIST) as list:
    list_contents = list.readlines()


for item in list_contents:
    new_item = item.replace("\n","")
    if new_item != "":
        new_letter=contents.replace("[name]", new_item)
        with open("letter_for_" + new_item + ".txt", mode="w") as file_letter:
            file_letter.write(new_letter)


