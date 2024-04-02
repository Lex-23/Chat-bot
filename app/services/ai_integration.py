import dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


dotenv.load_dotenv()


async def send_message_to_ai(chatbot, question: str) -> str:
    model = ChatOpenAI(model="gpt-3.5-turbo")
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
