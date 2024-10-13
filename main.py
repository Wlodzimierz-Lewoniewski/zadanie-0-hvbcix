document_list = []
document_count = int(input("How many documents you want to add?: "))
for i in range(0, document_count):
    document_list.append(input("Input document: ").strip())

search_list = []
search_count = int(input("How many words you want to search?: "))
for i in range(0, search_count):
    while True:
        word = input("Input the word: ").strip()
        if word in search_list:
            print("This word already exists")
        else:
            search_list.append(word)
            break

def count_word_in_document(word, document):
    return document.lower().split().count(word.lower())

for word in search_list:
    document_word_count = []
    for idx, doc in enumerate(document_list):
        word_count = count_word_in_document(word, doc)
        if word_count > 0:
            document_word_count.append((idx, word_count))
    
    sorted_documents = sorted(document_word_count, key=lambda x: x[1], reverse=True)
    
    sorted_document_indices = [doc[0] for doc in sorted_documents]
    

    print(sorted_document_indices)