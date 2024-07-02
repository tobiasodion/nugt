def indexFile(filePath):
    # load the file using langchain loader
    # embed the file using langchain embedder and openAI
    # index the file on qdrant
    return "Indexed"

print(indexFile("file.txt"))