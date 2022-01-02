### Basic functions 

def saveText(text, file, mode, encoding = 'utf-8') -> int:
    return open(file = file, mode = mode, encoding = encoding).write(text)