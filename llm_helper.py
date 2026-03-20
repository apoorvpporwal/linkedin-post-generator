from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv(override=True)


llm = ChatGroq(model = "llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are")
    print(response.content)

