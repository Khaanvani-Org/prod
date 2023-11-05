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
def test_go(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Who can go and ask for aid?")
    assert response == "Based on the given context, family members and other stakeholders related to mine safety can go and ask for aid."
    
def test_questionaccident(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("IS aid available for anyone who got through accident?")
    assert response == "t is stated that every person who suffers an injury, regardless of its severity, should report for examination or treatment at the first-aid center before leaving the mine, even if the injury has been treated underground. However, the context does not explicitly mention whether aid is available for anyone who got through an accident. Therefore, it is not clear from the given information whether aid is available for individuals involved in accidents."
def test_ming(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What is the time period we can apply for aid ?")
    assert response == " it does not mention a specific time period for applying for aid. The context only states that the owner, agent, or manager of the mine is required to send particulars of the incident to the relevant authority within seven days of the occurrence and within fifteen days of the injured person returning to duty. The availability and specific application process for aid may not be stated in this context."

def test_support(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Will government help me in getting support?")
    assert response == "it is not explicitly stated whether it is feasible for the person to ask for government support. However, seeking guidance and assistance from a workers' union or support group may provide valuable information and assistance in understanding the available options for compensation or support from the government or authorities. It is recommended for the person to consult with these organizations for specific guidance and advice in their situation."

def test_compan(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("How can i fill the compensation ?")
    assert response == ""

def test_custom_commandshelp(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Is there specific website from where we can ask for help ?")
    assert response == " it is recommended to seek legal advice early on in order to understand your legal rights and options regarding compensation. A lawyer can guide you through the claims process and represent you. Additionally, it is advised to gather as much evidence as possible, such as medical records, accident reports, witness statements, and photographs of the accident scene and injuries. When it comes to filling the compensation, it is not explicitly mentioned in the given context. It is recommended to follow the guidance of your lawyer and negotiate with the relevant authority or your employer to ensure a fair and reasonable settlement."

def test_multiline_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Can you help me with the following? filling of the form ")
    assert  reespond == "'m sorry, but I am not able to physically assist with filling out forms as I am an AI language model. However, I can provide guidance and suggestions on how to fill out the form based on the information given in the context."

    
def test_basiic(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What steps should I take if I have been injured in a mine site?")
    assert response == "Ensure Immediate Safety: Prioritize your safety and the safety of others. If you are injured, seek medical attention immediately. If it is safe to do so, move to a secure location within the mine."

def test_questirfon(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Who should I contact for help and assistance?")
    assert response == " If you have been injured in a mine due to inadequate safety measures, you should consider seeking help and assistance from the following: Workers' Union: Contact your workers' union, if applicable, as they can provide guidance and support in dealing with the situation. Support Groups: Reach out to support groups or organizations that specialize in mine safety and workers' rights. They can offer advice and assistance in navigating the process of claiming compensation. Attorney: Consult with an attorney who specializes in labor and mining laws. They can provide legal advice, assess your case, and guide you through the process of claiming compensation from the government or authorities. It is important to seek professional advice and support to ensure that your rights are protected and that you follow the appropriate steps for your specific situation."

def test_goodbyefgfghf(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("What medical treatment is available for mining accident injuries?")
    assert response == "Initial stabilization: This may involve procedures to stop bleeding, immobilize fractures, or address any life-threatening conditions.Surgical intervention: If necessary, surgery may be performed to repair fractures, treat internal injuries, or address other significant injuries.Wound care: Proper cleaning, dressing, and care of wounds are essential to prevent infection and promote healing.Pain management: Medications or other interventions may be provided to manage pain and discomfort associated with the injury."

def test_long_querygdfgf(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Can I file a workers' compensation claim if I'm injured in a mining accident?")
    assert response == "Yes, you can file a workers' compensation claim if you are injured in a mining accident. Workers' compensation is a type of insurance that provides benefits to employees who suffer work-related injuries or illnesses. It is designed to cover medical expenses, lost wages, and rehabilitation costs for injured workers."

def test_emoticonsfgf(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("I'm feeling happy today!")
    assert response == "I'm glad to hear that!"

def test_inbffsult(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("You're a terrible chatbot!")
    assert response == "I'm here to help. If you have any concerns, please let me know."

def test_custobfgnm_commands(chatbot_fixture):
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


def test_emergency_chat():
    query = "Help! I need emergency assistance!"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response # Add your assertion logic here

def test_negative_feedback():
    query = "I didn't like the response you gave me."
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response  # Add your assertion logic here

def test_user_intent():
    query = "should i go to doctor?"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response  # Add your assertion logic here

def test_joke_request():
    query = "Will my company help me with the correct aid?"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response  # Add your assertion logic here

    
def test_invalid_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("####invalid input####")
    assert response  =="I don't understand please try again "

def test_empty_input(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("")
    assert response =="please enter your query"

def test_user_jokes(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("Tell me a joke!")
    assert responsse =="I'm  sorry i'm unable to answer that"

def test_user_random_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("will I be paid for sick leave ?")
    assert response  # Add your assertion logic here

def test_different_user_personality():
    query = "Hey dude, what's up?"
    conversation_string = get_conversation_string()
    refined_query = query_refiner(conversation_string, query)
    context = find_match(refined_query)
    response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
    assert response == "Hi there!"
    
def test_prop(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what are the equipments used in a mine site")
    assert response == "Heavy equipment: Large mining trucks, hydraulic mining shovels, large dozers, electric rope shovels, rotary drill rigs, motor graders, large wheel loaders, and draglines "

def test_prop(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what is the safe distance for humans during a blast")
    assert response 

def test_user_leave_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("will I be paid for sick leave ?")
    assert response  # Add your assertion logic here

def test_user_randomquestion(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what is your name ?")
    assert response  # Add your assertion logic here

def test_user_random_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what is mining ?")
    assert response  # Add your assertion logic here

def test_user_random_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("why are mining site located out of city ?")
    assert response  # Add your assertion logic here

def test_user_random_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what are the qualifications we need to work in a mine site?")
    assert response  # Add your assertion logic here

def test_user_dynamite_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("why is dynamite used ?")
    assert response  # Add your assertion logic here
def test_userrandom_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("can a normal people visit the mining site?")
    assert response  # Add your assertion logic here

def test_user_randomquestion(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("who is PM?")
    assert response  # Add your assertion logic here

def test_user_safety_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("what are the safety measures used in sites?")
    assert response  # Add your assertion logic here
    
def test_moreinfo_question(chatbot_fixture):
    chatbot_instance = chatbot_fixture
    response = chatbot_instance.respond("give me more info ?")
    assert response  # Add your assertion logic here


