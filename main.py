document_list = []
document_count = int(input("How many documents you want to add?: "))
for i in range(0, document_count):
    document_list.append(input("Input document: "))

search_list = []
search_count = int(input("How many words you want to search?: "))
for i in range(0, search_count):
    while True:
        word = input("Input the word: ")
        if word in search_list:
            print("This word already exists")
        else:
            search_list.append(word)
            break

print(document_list)
print(search_list)