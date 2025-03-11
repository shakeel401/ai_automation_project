from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Initialize GPT-4 model
llm = ChatOpenAI(model="gpt-4o-mini")

def process_query(user_input):
    """
    Processes user input using GPT-4 to generate structured responses.

    :param user_input: User query
    :return: AI-generated structured response
    """
    messages = [
       SystemMessage(content="You are an advanced AI automation agent designed to process large data inputs, generate structured PDF reports, and handle voice input using speech-to-text models. You autonomously analyze information, make data-driven decisions, and personalize responses based on user preferences. Maintain accuracy, efficiency, and clarity in all outputs while ensuring a user-friendly experience."),
        HumanMessage(content=user_input),
    ]
    return llm(messages).content
