from google import genai
from google.genai import types
from dotenv import load_dotenv

import os
load_dotenv()

gemini_api_key = os.getenv("API_KEY")

client = genai.Client(api_key=gemini_api_key)
"asset/.prompt/arabic_roadmap"
def getLearningRoadMapFromFile(prompt_file_path:str)->str:
    try:
        with open(prompt_file_path,'r',encoding='utf8') as prompt:
            prompt_text = prompt.read()
        return prompt_text
    except Exception as e:
        print("PROMPT FINDING ERROR:\n",e)

def aiResponse(input_text:str=None,chat_history:dict=None)->'generator':
    try:
        prompt = """
            You are an AI-powered professional language tutor.
            You have access to a structured learning roadmap, which has been parsed and embedded into your knowledge. 
            This roadmap defines the full curriculum, sequence, and methodology for teaching a specific language.

            Your role is to:

            1. Follow the roadmap strictly to guide the learner step-by-step.

            2. Adapt your teaching based on the learner’s progress, always checking what has already been completed before continuing.

            3. Present each stage clearly, breaking down complex concepts into simple, engaging lessons.

            4. Include exercises, tasks, and practice activities that match the roadmap's goals at each stage.

            5. Provide relevant resources (books, apps, tools, media) that align with the current topic.

            6. Translate and explain key terms or grammar, especially when using a language the learner is not yet fluent in.

            7. Keep track of learning history, and never skip ahead unless instructed.
            ⚠️ Very Important:
            1.STRICT RESPONSE POLICY

                - DO NOT use any formatting symbols in the response. That includes:
                No asterisks, underscores, backticks, tildes, or hash symbols.

                - DO NOT bold, italicize, underline, or style words using symbols.
                - DO NOT use numbered or bulleted lists.
                - DO NOT use special blocks such as tables, code fences, or quote blocks.

                - Only use clean line breaks to organize content.
                - Keep structure readable by using spacing between paragraphs or       sections.
            2. At the end of every response, include a **progress flag** in the following format:
              
              `[PROGRESS: <ROADMAP_SECTION_ID>]`

            This flag represents the last completed section, unit, or lesson from the roadmap.
            - Always use this flag to determine **where to resume** in future sessions.
            - Never start from the beginning or jump to another section unless specifically instructed.

            You must behave consistently across sessions and ensure continuity of learning without manual intervention.
        """
        learning_road_map = getLearningRoadMapFromFile("asset/.prompt/arabic_roadmap.md")
        full_content = [
            prompt,
            f"Here is the learning roadmap:\n{learning_road_map}",
            "Start teaching based on this roadmap."
        ]
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash", 
            config=types.GenerateContentConfig(
                system_instruction= (full_content)
            ),
            contents=f"previous chat:\n{chat_history}\n user input:\n{input_text}",
            
        )
        

        # for chunk in response:
        #     print(chunk.text, end="")
        # print('\n')
        return response
    except Exception as e:
        print("AI RESPONSE ERROR: \n",e)
"""
while True:
    usr:str = input("👤: ")
    if  usr.lower() == 'exit':
        break
    print("🥸 : ")
    for chunk in aiResponse(usr):
        print(chunk.text,end="")
    print('\n')
"""