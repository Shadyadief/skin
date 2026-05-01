from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# 1. Diagnosis
diagnosis_prompt = PromptTemplate.from_template("""
You are a dermatologist assistant.
Analyze the skin condition based on:
Skin type: {skin_type}
Symptoms: {symptoms}

Give a short diagnosis.
""")

def diagnosis_agent(skin_type, symptoms):
    return llm.invoke(diagnosis_prompt.format(
        skin_type=skin_type,
        symptoms=symptoms
    )).content


# 2. Recommendation
recommend_prompt = PromptTemplate.from_template("""
Based on this diagnosis:
{diagnosis}

Suggest:
- Morning routine
- Night routine
Keep it simple.
""")

def recommendation_agent(diagnosis):
    return llm.invoke(recommend_prompt.format(
        diagnosis=diagnosis
    )).content


# 3. Follow-up
followup_prompt = PromptTemplate.from_template("""
User feedback:
{feedback}

Adjust the skincare routine.
""")

def followup_agent(feedback):
    return llm.invoke(followup_prompt.format(
        feedback=feedback
    )).content
