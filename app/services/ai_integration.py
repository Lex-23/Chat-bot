import dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


config = dotenv.dotenv_values(".env")


async def send_message_to_ai(chatbot, question: str) -> str:
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=config.get("OPENAI_API_KEY"), temperature=0)
    output_parser = StrOutputParser()
    qa_template = chatbot.generate_qa_template(question=question)

    prompt = ChatPromptTemplate.from_messages([
    ("system", qa_template),
    ("user", "Question: {question}\nContext: {context}")
    ])

    context = await chatbot.get_context()
    chain = prompt | model | output_parser
    response = chain.invoke({"question": question, "context": context})
    return response
