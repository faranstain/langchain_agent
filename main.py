from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os


os.environ["GROQ_API_KEY"] = "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"

chat_model = ChatOpenAI(
    openai_api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    model_name="llama3-8b-8192"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{text}")
])

user=input("Ask anything")

formatted_prompt = prompt.format(text=user)


response = chat_model.invoke(formatted_prompt)

print("\nAi Response:", response.content)
