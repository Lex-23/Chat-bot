from models import Message, User, Chat


def create_message(user: User, text: str, chat: Chat):
    message = Message(
        user=user,
        username=user.username,
        text=text,
        chat=chat
    )

    message.save()

def process_question(user: User, question: str, chat: Chat):
    text = f'{user.username} asked {question}.'
    create_message(user, text, chat)

def process_answer(user: User, answer: str, chat: Chat):
    text = f'{chat.name}AI answered {answer}.'
    create_message(user, text, chat)
