import streamlit as st
# from langchain.llms import OpenAI
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
client= OpenAI()

st.title('멋진 이미지를 만들어볼까요?')
st.subheader('_Your Images_ are SO :blue[cool]:star: :sunglasses::heart:')

with st.sidebar:
    """
    🤝Tip:\n
    _:heart:컨셉아트종류_:건축,캐릭터,배경,무기및 소품,기계및 차량,애니메이션\n
    _:star:브러쉬_:연필,잉크,펜,컬러잉크,수채,유채,먹,텍스쳐\n
    _:rose:화풍_:사진화풍,추상화풍,고전모던화풍,아르누보화풍,인상화풍,동양화풍,극사실화풍,팝아트화풍,초현실화풍,점묘화풍,픽셀화풍

    """


# def generate_images(image_description,num_images):
#     img_response=client.images.generate(
#             model="dall-e-3",
#             prompt=image_description,
#             size="1024x1024",
#             quality="standard",
#             n=1,
              
#             )
#     image_url = img_response.data[0].url
#     return image_url

# img_description=st.text_input( "prompt"  )
# # num_of_images=st.number_input("select",min_value=1,max_value=5,value=1)

# if st.button("Generate Images"):
#     # for _ in range(num_of_images):
#     #     generate_image=generate_images( img_description,num_of_images)
#     #     st.image(generate_image)
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
#     )
#     print(completion.choices[0].message) # Object
#     st.write(completion.choices[0].message.content)
    

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "천재음악가로서 , 아름다운 가사를 만들어드리겠습니다."}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)




