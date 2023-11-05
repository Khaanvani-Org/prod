import pytest


#@pytest.fixture

def chatbot_fixture():
    return main()

def test_greeting(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Hello, chatbot!")
    assert response == "Hi there!"

def test_non_greeting(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("How's the weather?")
    assert response == "I don't understand."


def test_empty_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("")
    assert response == "Please provide a valid input."
    
def test_basic(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What steps should I take if I have been injured in a mine site?")
    assert response == "Ensure Immediate Safety: Prioritize your safety and the safety of others. If you are injured, seek medical attention immediately. If it is safe to do so, move to a secure location within the mine."

def test_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Who should I contact for help and assistance?")
    assert response == " If you have been injured in a mine due to inadequate safety measures, you should consider seeking help and assistance from the following: Workers' Union: Contact your workers' union, if applicable, as they can provide guidance and support in dealing with the situation. Support Groups: Reach out to support groups or organizations that specialize in mine safety and workers' rights. They can offer advice and assistance in navigating the process of claiming compensation. Attorney: Consult with an attorney who specializes in labor and mining laws. They can provide legal advice, assess your case, and guide you through the process of claiming compensation from the government or authorities. It is important to seek professional advice and support to ensure that your rights are protected and that you follow the appropriate steps for your specific situation."

def test_goodbye(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What medical treatment is available for mining accident injuries?")
    assert response == "Initial stabilization: This may involve procedures to stop bleeding, immobilize fractures, or address any life-threatening conditions.Surgical intervention: If necessary, surgery may be performed to repair fractures, treat internal injuries, or address other significant injuries.Wound care: Proper cleaning, dressing, and care of wounds are essential to prevent infection and promote healing.Pain management: Medications or other interventions may be provided to manage pain and discomfort associated with the injury."

def test_long_query(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Can I file a workers' compensation claim if I'm injured in a mining accident?")
    assert response == "Yes, you can file a workers' compensation claim if you are injured in a mining accident. Workers' compensation is a type of insurance that provides benefits to employees who suffer work-related injuries or illnesses. It is designed to cover medical expenses, lost wages, and rehabilitation costs for injured workers."

def test_emoticons(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("I'm feeling happy today!")
    assert response == "I'm glad to hear that!"

def test_insult(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("You're a terrible chatbot!")
    assert response == "I'm here to help. If you have any concerns, please let me know."

def test_custom_commands(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("/help")
    assert response == "Available commands: /start, /stop, /help"

def test_multiline_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Can you help me with the following? filling of the form ")
    assert "I can assist with your tasks" in response

def test_special_characters(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What's 2 + 2?")
    assert response == "The result of 2 + 2 is 4."

def test_case_insensitivity(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("i am not fine ")
    assert response == "Sorry to hear that what are the possible ways we can help you ! feel free to ask any question"

def test_unknown_command(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("/unknown")
    assert response == "Unknown command. Type /help for available commands."



def test_empty_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Can miners receive psychological support after a traumatic accident?")
    assert response == "I don't know. The provided context does not mention whether miners can receive psychological support after a traumatic accident."

def test_help_command(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What should I do if a coworker is injured in a mine?")
    assert response == "Seek immediate medical attention for the injured coworker.Report the accident to your supervisor or mine management.Document the accident by taking photos or videos of the accident scene, the coworker's injuries, and any hazardous conditions that may have contributed to the incident.Collect contact information of any witnesses to the accident.Encourage the injured coworker to seek legal advice from an attorney who specializes in labor and mining laws.Ensure that the injured coworker is aware of their rights to a safe working environment and appropriate compensation under the relevant acts and regulations, such as the Mines Act, 1952 and the Workmen's Compensation Act, 1923.Offer emotional support to the injured coworker and encourage them to seek any necessary psychological support to cope with the traumatic experience."

def test_urgent_request(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("I need immediate help!")
    assert "emergency" in response  # Check if the response includes a reference to emergency assistance.

def test_question_about_safety(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("How can I stay safe in a mine?")
    assert "safety measures" in response  # Check if the response provides safety information.

def test_positive_feedback(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("How are mine accidents investigated, and what happens afterward?")
    assert response == "The provided context does not specify how mine accidents are investigated or what happens afterward. Therefore, I don't know the details of the investigation process or the subsequent steps taken after a mine accident."

def test_unknown_command(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Are there any support services for the families of miners involved in accidents?")
    assert response == "The provided context does not mention specific support services for the families of miners involved in accidents. However, it is common for mining companies or organizations to provide support services for the families of injured or deceased miners. These services may include counseling, financial assistance, and other forms of support to help families cope with the emotional and financial challenges they may face. It is advisable to consult with the mine management or relevant authorities to inquire about the specific support services available in such situations.."



def test_chatbot_response():
    query = "Hello, chatbot!"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response  # Add your assertion logic here

def test_non_greeting_response():
    query = "How's the weather?"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response  # Add your assertion logic here
