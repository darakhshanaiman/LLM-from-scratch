import urllib.request
url=("https://raw.githubusercontent.com/rasbt/" "LLMs-from-scratch/main/ch02/01_main-chapter-code/" "the-verdict.txt")
file_path="the-verdict.txt"
urllib.request.urlretrieve(url,file_path)
############### Making Tokenizer ###################
with open("the-verdict.txt","r",encoding="utf-8") as f:
    raw_text=f.read()
print("total num of character:",len(raw_text))
print(raw_text[:99])
#using regex lib to make list of tokens
import re
text= "Hello, world. this is a test"
result=re.split(r'(\s)',text)
print(result)
#removing white spaces
result= [item for item in result if item.strip()]
print(result)
#removing the symbols
text = "Hello, world. is this-- a test?"
result= re.split(r'([,.:?;_!"()\']|--\s)',text)
result = [item.strip() for item in result if item.strip()]
print (result)

#Making tokenizer for the text
preprocessed=re.split(r'([,.:?;_!"()\']|--\s)',raw_text)
preprocessed =[item.strip() for item in preprocessed if item.strip()]
print (preprocessed)