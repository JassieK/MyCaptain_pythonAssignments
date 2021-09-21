filename = input("Input the filename : ")
extension ={"c":"C", "cpp":"C++" , "java":"Java" , "py":"Python" , "html":"HTML" , "css":"Cascading Style Sheet" , "docx":"Microsoft word file" , "pdf":"PDF" , "sql":"SQL database" , "js":"Javascript" , "php":"PHP"}
ex = filename.split(".")[-1]
print("The extension of the file is " , ex)
print("It's a ", extension.get(ex), "file")