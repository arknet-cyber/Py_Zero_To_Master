from translate import Translator

translator =  Translator(to_lang='iu') #iu = inuktitut lang from eskimo

try:
    with open('189-tr-textfile.txt', mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('189-iu-tr-file.txt', mode='w') as my_file2:
          my_file2.write(translation)  
except FileNotFoundError as e:
    print('file does not exist') 
