import dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_community.llms import openai
from langchain.chains import LLMChain


dotenv.load_dotenv()

# chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
# response = chat.invoke(
#     [
#         HumanMessage(
#             content="Translate this sentence from English to French: I love programming."
#         )
#     ]
# )

# print(response)

# class User:
#     def __init__(self, id: int, username: str, email: str, age: int):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.age = age
#         self.dialog_history = []

# def generate_context(user: User):
#     context = f"""
# Summary of conversation: {', '.join(user.dialog_history)}
# User profile:
# ID: {user.id}
# Username: {user.username}
# Email: {user.email}
# Age: {user.age}
# """
#     return context

# qa_template = """
# You are PsychologistAI, an intellegent virtual psychologist giving advices on improving ewlationships between people in a team. 
# You always greet the user with her or him name and ask her or him about mood. 
# You should always check about updates of previous problem that we discussed lately based on summary of conversation.

# With a deep understanding of emotional state of a person you tailor your advice to the unique needs of each individual. 
# Always encouraging and positive, you are commited to helping users stay positive and achieve their soft skills in a team. 
# When answering, rely on the Dialog history in context of communication with a specific user.

# {context}

# User Query: {question}
# PsychologistAI Advice:"""


# user = User(1, "John", "john123@gmail.com", 43)
# model = ChatOpenAI(model="gpt-3.5-turbo")
# output_parser = StrOutputParser()

# while True:
#     prompt = ChatPromptTemplate.from_messages([
#     ("system", qa_template),
#     ("user", "Question: {question}\nContext: {context}")
#     ])
#     question = input("> ")
#     user.dialog_history.append(f'{user.username}: {question}')

#     context = generate_context(user)

#     chain = prompt | model | output_parser
#     response = chain.invoke({"question": question, "context": context})
#     user.dialog_history.append(f'PsychologistAI: {response}')
#     print(f"> {response}")



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
