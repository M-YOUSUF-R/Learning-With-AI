from docsApi import *
from dotenv import load_dotenv,find_dotenv,set_key
import os
load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/documents"]
client = "credentials/credentials.json"
token = "tokens/token.json"

def main():
    try:
        
        DOCUMENT_ID = os.getenv('DOCUMENT_ID')
        if(DOCUMENT_ID):
            doc = OpenExistingDoc(SCOPES=SCOPES,DOCUMENT_ID=DOCUMENT_ID,clien_credential=client,token_json=token)
            
        else:
            print('creating a docs for you...')
            title:str = input("enter the docs title: ")
            doc = createDocument(title=title,SCOPES=SCOPES,client_credential=client,token_name=token)
            
            dotenv_path = find_dotenv()
            load_dotenv(dotenv_path=dotenv_path)
            key_to_update = "DOCUMENT_ID"
            value = doc.get("documentId")
            
            set_key(dotenv_path=dotenv_path,key_to_set=key_to_update,value_to_set=value)

        with open('user_input.txt','r') as user_input:
            # print(user_input.read())
            usr_input = user_input.read()
            insertText(SCOPES,DOCUMENT_ID,usr_input,client,token,endline=True)
        insertText(SCOPES,DOCUMENT_ID,"I have to do this \n please work.",client,token,endline=True)
        var = (readText(SCOPES=SCOPES,DOCUMENT_ID=DOCUMENT_ID,client_credential=client,token_name=token,))
        print(var)
        
    except Exception as err:
        print("ERROR:\n",err)


if __name__=="__main__":
    main()
