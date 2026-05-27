
book = {"name":"1 Nephi", "chapters": 20}


print(book['name'])

#editing the value 
book["name"] = "Mosiah"

#adding and ittem 
#just creating a new key and value   book = {key:value}
book["book"] = "Book Of Mormon"

#deleting items
del book["book"] 
print(book)
