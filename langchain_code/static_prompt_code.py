#Code Documentation : 23-10-26

#To pass the prompt to the llm in our local coding environment 

#First import the required package to run in jupiter notebook for this i am using free version gemini ai 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

#now after importing we have to say what model we wanted to import i am here using the "gemini-3-flash-preview"

llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

#in the format_messages why it is named as format_messages means it expects 2 arguments one is system prompt and another is user prompt

# but what is system prompt it means explaining act as a set of person it might be a programmer or teacher what ever 

#user prompt means main intent what user is expecting 
final_prompts=prompts.format_messages(systemprompt, userprompt)

#now we have both the user and system prompt we now just invoke the final_prompts into the llm

res=llm.invoke(final_prompts)
print(res)


#This is the static and very lengthy way of prompting the code like for every set of prompt we have to write that line 

final_prompts=prompts.format_messages(systemprompt, userprompt)
res=llm.invoke(final_prompts)

 
