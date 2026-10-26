# from langchain_openai import ChatOpenAI

# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# import streamlit as st

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv(), override=True)

# st.set_page_config(
#     page_title='Your Custom Assistant',
#     page_icon='🤖'
# )

# st.subheader('Your Custom ChatGPT 🤖')

# chat = ChatOpenAI(model_name='gpt-6-luna', temperature=1)

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# with st.sidebar:

#     system_message = st.text_input(label='System role')

#     user_prompt = st.text_input(label='Send a meassage')


# if system_message:
#     if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
#         st.session_state.messages.append(
#             SystemMessage(content=user_prompt)
#         )

# if user_prompt:
#     st.session_state.messages.append(
#         HumanMessage(content=user_prompt)
#     )

#     with st.spinner('Working on your request ...'):
#         response = chat.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))

# if len(st.session_state.messages) >= 1:
#     if not isinstance(st.session_state.messages[0], SystemMessage):
#         st.session_state.messages.insert(0, SystemMessage(content='You are a helpful assistant'))


# for msg in st.session_state.messages[1:]:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("human"):
#             st.write(msg.content)
#     elif isinstance(msg, AIMessage):
#         with st.chat_message("ai"):
#             st.write(msg.content)


# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# import streamlit as st
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# st.set_page_config(
#     page_title='Your Custom Assistant',
#     page_icon='🤖'
# )

# st.subheader('Your Custom ChatGPT 🤖')

# chat = ChatOpenAI(model_name='gpt-6-luna', temperature=1)

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# with st.sidebar:
#     system_message = st.text_input(label='System role')
#     # user_prompt input yahan se remove kar diya gaya hai

# if system_message:
#     if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
#         # Purane code ki galti (content=user_prompt) ko system_message se theek kar diya gaya hai
#         st.session_state.messages.append(
#             SystemMessage(content=system_message)
#         )

# if len(st.session_state.messages) >= 1:
#     if not isinstance(st.session_state.messages[0], SystemMessage):
#         st.session_state.messages.insert(0, SystemMessage(content='You are a helpful assistant'))

# # 1. Pehle purane messages ko screen par render karein
# for msg in st.session_state.messages[1:]:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("human"):
#             st.write(msg.content)
#     elif isinstance(msg, AIMessage):
#         with st.chat_message("ai"):
#             st.write(msg.content)

# # 2. Main page par bottom mein naya Chat Input bar lagayein
# user_prompt = st.chat_input("Send a message")

# # 3. Jab user naya message send kare toh usay handle karein
# if user_prompt:
#     st.session_state.messages.append(
#         HumanMessage(content=user_prompt)
#     )
    
#     # User ka naya message foran screen par show karein
#     with st.chat_message("human"):
#         st.write(user_prompt)

#     with st.spinner('Working on your request ...'):
#         response = chat.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))
    
#     # AI ka naya message foran screen par show karein
#     with st.chat_message("ai"):
#         st.write(response.content)

# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# import streamlit as st
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# st.set_page_config(
#     page_title='Your Custom Assistant',
#     page_icon='🤖'
# )

# st.subheader('Your Custom ChatGPT 🤖')

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# with st.sidebar:
#     # 1. System role ke upar API Key ka input field add kiya gaya hai
#     api_key = st.text_input(label='Enter API Key', type='password', help='Chat shuru karne ke liye API key daalein')
    
#     system_message = st.text_input(label='System role')

# if system_message:
#     if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
#         st.session_state.messages.append(
#             SystemMessage(content=system_message)
#         )

# if len(st.session_state.messages) >= 1:
#     if not isinstance(st.session_state.messages[0], SystemMessage):
#         st.session_state.messages.insert(0, SystemMessage(content='You are a helpful assistant'))

# # Pehle messages ko screen par render karein
# for msg in st.session_state.messages[1:]:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("human"):
#             st.write(msg.content)
#     elif isinstance(msg, AIMessage):
#         with st.chat_message("ai"):
#             st.write(msg.content)

# # 2. Agar API key field khali hai toh input disable ho jayega
# is_chat_disabled = not api_key 

# if is_chat_disabled:
#     st.info("Chat enable karne ke liye sidebar mein apni API Key enter karein.")

# # 3. Chat input par disabled parameter apply kiya gaya hai
# user_prompt = st.chat_input("Send a message", disabled=is_chat_disabled)

# if user_prompt:
#     st.session_state.messages.append(
#         HumanMessage(content=user_prompt)
#     )
    
#     with st.chat_message("human"):
#         st.write(user_prompt)

#     with st.spinner('Working on your request ...'):
#         # 4. ChatOpenAI ko ab user ki daali hui API key assign ki ja rahi hai
#         chat = ChatOpenAI(model_name='gpt-6-luna', temperature=1, api_key=api_key)
#         response = chat.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))
    
#     with st.chat_message("ai"):
#         st.write(response.content)

# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# import streamlit as st
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# st.set_page_config(
#     page_title='Your Custom Assistant',
#     page_icon='🤖'
# )

# st.subheader('Your Custom ChatGPT 🤖')

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# with st.sidebar:
#     api_key = st.text_input(label='Enter API Key', type='password', help='Chat shuru karne ke liye API key daalein')
#     system_message = st.text_input(label='System role')
    
#     st.divider()
#     st.markdown("### 🕒 Chat History")
#     # 1. Ek empty container banayenge taake history hamesha latest messages ke sath update ho
#     history_container = st.container()

# if system_message:
#     if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
#         st.session_state.messages.append(
#             SystemMessage(content=system_message)
#         )

# if len(st.session_state.messages) >= 1:
#     if not isinstance(st.session_state.messages[0], SystemMessage):
#         st.session_state.messages.insert(0, SystemMessage(content='You are a helpful assistant'))

# # Main page par purane messages render karein
# for msg in st.session_state.messages[1:]:
#     if isinstance(msg, HumanMessage):
#         with st.chat_message("human"):
#             st.write(msg.content)
#     elif isinstance(msg, AIMessage):
#         with st.chat_message("ai"):
#             st.write(msg.content)

# is_chat_disabled = not api_key 

# if is_chat_disabled:
#     st.info("Chat enable karne ke liye sidebar mein apni API Key enter karein.")

# user_prompt = st.chat_input("Send a message", disabled=is_chat_disabled)

# if user_prompt:
#     st.session_state.messages.append(
#         HumanMessage(content=user_prompt)
#     )
    
#     with st.chat_message("human"):
#         st.write(user_prompt)

#     with st.spinner('Working on your request ...'):
#         chat = ChatOpenAI(model_name='gpt-6-luna', temperature=1, api_key=api_key)
#         response = chat.invoke(st.session_state.messages)

#     st.session_state.messages.append(AIMessage(content=response.content))
    
#     with st.chat_message("ai"):
#         st.write(response.content)

# # 2. Sath sath history update karne ke liye history_container ko yahan sabse end mein fill karenge
# with history_container:
#     # History mein SystemMessage ko ignore karke sirf You aur AI ki chat show karein
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             st.markdown(f"*👤 You:* {msg.content}")
#             st.markdown("") # Thori space ke liye
#         elif isinstance(msg, AIMessage):
#             st.markdown(f"*🤖 AI:* {msg.content}")
#             st.divider() # Har chat pair ke baad ek line lagane ke liye




# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# # Page Configuration
# st.set_page_config(
#     page_title='Custom ChatGPT',
#     page_icon='🤖',
#     layout='wide'
# )

# # 1. Session State Initialization
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = None
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Helper Functions
# def login():
#     st.session_state.api_key = st.session_state.api_key_input

# def logout():
#     st.session_state.api_key = None
#     st.session_state.messages = []

# def clear_chat():
#     st.session_state.messages = []

# # ==========================================
# # STATE 1: LOGIN PAGE
# # ==========================================
# if not st.session_state.api_key:
#     st.markdown("<h1 style='text-align: center;'>Welcome to Custom ChatGPT</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center;'>Please enter your API Key to access the chat.</p>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         with st.form("login_form"):
#             st.text_input("OpenAI API Key", type="password", key="api_key_input", placeholder="sk-...")
#             submit_button = st.form_submit_button("Login", use_container_width=True, on_click=login)

# # ==========================================
# # STATE 2: CHAT PAGE (ChatGPT UI)
# # ==========================================
# else:
#     # Sidebar Setup (Matching the provided image)
#     with st.sidebar:
#         st.button("+ New chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("### CHATS")
#         st.markdown("💬 Current Chat Session")
        
#         # Spacer for pushing account details to bottom
#         for _ in range(15):
#             st.markdown("") 
            
#         st.markdown("---")
#         st.markdown("### SETTINGS")
#         st.markdown("⚙️ Model & behavior")
        
#         st.markdown("### ACCOUNT")
#         # Masking the API key just like "Key: sk-...RTAA" in the image
#         masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
#         st.markdown(f"🔑 Key: {masked_key}")
        
#         st.button("🔄 Change API key", on_click=logout, use_container_width=True)

#     # Main Chat Area
#     if len(st.session_state.messages) == 0:
#         st.session_state.messages.append(SystemMessage(content="You are a helpful assistant."))

#     # Render previous messages
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             with st.chat_message("user"):
#                 st.write(msg.content)
#         elif isinstance(msg, AIMessage):
#             with st.chat_message("assistant"):
#                 st.write(msg.content)

#     # Bottom Chat Input
#     user_prompt = st.chat_input("Message your assistant ...")

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))
        
#         with st.chat_message("user"):
#             st.write(user_prompt)

#         with st.spinner("Thinking..."):
#             try:
#                 # Using the API key from session state
#                 chat = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.7, api_key=st.session_state.api_key)
#                 response = chat.invoke(st.session_state.messages)
                
#                 st.session_state.messages.append(AIMessage(content=response.content))
                
#                 with st.chat_message("assistant"):
#                     st.write(response.content)
#             except Exception as e:
#                 st.error(f"API Error: Please check your API key. ({e})")


# import streamlit as st
# import json
# import os
# from datetime import datetime
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# # File jahan chats save hongi
# HISTORY_FILE = "chat_history.json"

# # Page Configuration
# st.set_page_config(
#     page_title='Custom ChatGPT',
#     page_icon='🤖',
#     layout='wide'
# )

# # ==========================================
# # HELPER FUNCTIONS FOR HISTORY
# # ==========================================
# def load_all_chats():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as f:
#             try:
#                 return json.load(f)
#             except:
#                 return {}
#     return {}

# def save_all_chats():
#     with open(HISTORY_FILE, "w") as f:
#         json.dump(st.session_state.all_chats, f)

# def convert_to_dict_msgs(lc_msgs):
#     msgs = []
#     for m in lc_msgs:
#         if isinstance(m, SystemMessage): msgs.append({"role": "system", "content": m.content})
#         elif isinstance(m, HumanMessage): msgs.append({"role": "user", "content": m.content})
#         elif isinstance(m, AIMessage): msgs.append({"role": "assistant", "content": m.content})
#     return msgs

# def convert_to_langchain_msgs(dict_msgs):
#     msgs = []
#     for m in dict_msgs:
#         if m["role"] == "system": msgs.append(SystemMessage(content=m["content"]))
#         elif m["role"] == "user": msgs.append(HumanMessage(content=m["content"]))
#         elif m["role"] == "assistant": msgs.append(AIMessage(content=m["content"]))
#     return msgs

# # 1. Session State Initialization
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = None
# if 'all_chats' not in st.session_state:
#     st.session_state.all_chats = load_all_chats()
# if 'current_chat_id' not in st.session_state:
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # ==========================================
# # ACTION HANDLERS
# # ==========================================
# def login():
#     st.session_state.api_key = st.session_state.api_key_input

# def logout():
#     st.session_state.api_key = None
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def clear_chat():
#     st.session_state.messages = []
#     # Nayi chat ke liye naya ID (timestamp) generate karein
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def load_chat(chat_id):
#     st.session_state.current_chat_id = chat_id
#     st.session_state.messages = convert_to_langchain_msgs(st.session_state.all_chats[chat_id])

# def save_current_chat():
#     if len(st.session_state.messages) > 1: # Kam az kam 1 user message ho tabhi save karein
#         st.session_state.all_chats[st.session_state.current_chat_id] = convert_to_dict_msgs(st.session_state.messages)
#         save_all_chats()

# # ==========================================
# # STATE 1: LOGIN PAGE
# # ==========================================
# if not st.session_state.api_key:
#     st.markdown("<h1 style='text-align: center;'>Welcome to Custom ChatGPT</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center;'>Please enter your API Key to access the chat.</p>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         with st.form("login_form"):
#             st.text_input("OpenAI API Key", type="password", key="api_key_input", placeholder="sk-...")
#             st.form_submit_button("Login", use_container_width=True, on_click=login)

# # ==========================================
# # STATE 2: CHAT PAGE (ChatGPT UI)
# # ==========================================
# else:
#     # Sidebar Setup
#     with st.sidebar:
#         st.button("+ New chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("### CHATS")
        
#         # Saved Chats list in Sidebar
#         for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
#             # Title ke liye pehla User message dhundhein
#             chat_title = "New Chat"
#             for m in msgs_dict:
#                 if m["role"] == "user":
#                     chat_title = m["content"][:25] + "..." # Limit title length
#                     break
            
#             # History button click karne par history load hogi
#             st.button(f"💬 {chat_title}", key=f"btn_{chat_id}", on_click=load_chat, args=(chat_id,), use_container_width=True)
        
#         # Spacer
#         for _ in range(5):
#             st.markdown("") 
            
#         st.markdown("---")
#         st.markdown("### SETTINGS")
#         st.markdown("⚙️ Model & behavior")
        
#         st.markdown("### ACCOUNT")
#         masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
#         st.markdown(f"🔑 Key: {masked_key}")
        
#         st.button("🔄 Change API key", on_click=logout, use_container_width=True)

    
#     # ==========================================
# # STATE 2: CHAT PAGE (ChatGPT UI)
# # ==========================================

#     # Sidebar Setup
#     with st.sidebar:
        
#         # === Naya Logo aur Text Design Yahan Add Kiya Gaya Hai ===
#         st.markdown("""
#         <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; margin-top: 5px;">
#             <div style="background-color: #1E88E5; border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);">
#                 <span style="color: white; font-size: 16px;">🤖</span> 
#             </div>
#             <span style="font-size: 18px; font-weight: bold; font-family: sans-serif;">Custom ChatGPT</span>
#         </div>
#         """, unsafe_allow_html=True)
#         # =========================================================

#         # Ye pehle wala button hai
#         st.button("+ New chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("### CHATS")
        
#         # Baaki ka sidebar code neeche same rahega...
#         # for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
#         # ...

#     # Main Chat Area
#     if len(st.session_state.messages) == 0:
#         st.session_state.messages.append(SystemMessage(content="You are a helpful assistant."))

#     # Render previous messages
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             with st.chat_message("user"):
#                 st.write(msg.content)
#         elif isinstance(msg, AIMessage):
#             with st.chat_message("assistant"):
#                 st.write(msg.content)

#     # Bottom Chat Input
#     user_prompt = st.chat_input("Message your assistant ...")

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))
        
#         with st.chat_message("user"):
#             st.write(user_prompt)

#         with st.spinner("Thinking..."):
#             try:
#                 # API Key and updated model (gpt-4o-mini)
#                 chat = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.7, api_key=st.session_state.api_key)
#                 response = chat.invoke(st.session_state.messages)
                
#                 st.session_state.messages.append(AIMessage(content=response.content))
                
#                 with st.chat_message("assistant"):
#                     st.write(response.content)
                
#                 # Chat file mein save karein
#                 save_current_chat()
#                 st.rerun() # UI refresh karne ke liye taake sidebar mein nayi chat show ho
                
#             except Exception as e:
#                 st.error(f"API Error: ({e})")




# import streamlit as st
# import json
# import os
# from datetime import datetime
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# # File jahan chats save hongi
# HISTORY_FILE = "chat_history.json"

# # Page Configuration
# st.set_page_config(
#     page_title='Custom ChatGPT',
#     page_icon='🤖',
#     layout='wide'
# )

# # ==========================================
# # HELPER FUNCTIONS FOR HISTORY
# # ==========================================
# def load_all_chats():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as f:
#             try:
#                 return json.load(f)
#             except:
#                 return {}
#     return {}

# def save_all_chats():
#     with open(HISTORY_FILE, "w") as f:
#         json.dump(st.session_state.all_chats, f)

# def convert_to_dict_msgs(lc_msgs):
#     msgs = []
#     for m in lc_msgs:
#         if isinstance(m, SystemMessage): msgs.append({"role": "system", "content": m.content})
#         elif isinstance(m, HumanMessage): msgs.append({"role": "user", "content": m.content})
#         elif isinstance(m, AIMessage): msgs.append({"role": "assistant", "content": m.content})
#     return msgs

# def convert_to_langchain_msgs(dict_msgs):
#     msgs = []
#     for m in dict_msgs:
#         if m["role"] == "system": msgs.append(SystemMessage(content=m["content"]))
#         elif m["role"] == "user": msgs.append(HumanMessage(content=m["content"]))
#         elif m["role"] == "assistant": msgs.append(AIMessage(content=m["content"]))
#     return msgs

# # 1. Session State Initialization
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = None
# if 'all_chats' not in st.session_state:
#     st.session_state.all_chats = load_all_chats()
# if 'current_chat_id' not in st.session_state:
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # ==========================================
# # ACTION HANDLERS
# # ==========================================
# def login():
#     st.session_state.api_key = st.session_state.api_key_input

# def logout():
#     st.session_state.api_key = None
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def clear_chat():
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def load_chat(chat_id):
#     st.session_state.current_chat_id = chat_id
#     st.session_state.messages = convert_to_langchain_msgs(st.session_state.all_chats[chat_id])

# def save_current_chat():
#     if len(st.session_state.messages) > 1:
#         st.session_state.all_chats[st.session_state.current_chat_id] = convert_to_dict_msgs(st.session_state.messages)
#         save_all_chats()

# # ==========================================
# # STATE 1: LOGIN PAGE
# # ==========================================
# if not st.session_state.api_key:
#     st.markdown("<h1 style='text-align: center;'>Welcome to Custom ChatGPT</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center;'>Please enter your API Key to access the chat.</p>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         with st.form("login_form"):
#             st.text_input("OpenAI API Key", type="password", key="api_key_input", placeholder="sk-...")
#             st.form_submit_button("Login", use_container_width=True, on_click=login)

# # ==========================================
# # STATE 2: CHAT PAGE (ChatGPT UI)
# # ==========================================
# else:
#     # Sidebar Setup
#     with st.sidebar:
        
#         # 1. Yeh naya hissa hai jisme Logo aur Custom ChatGPT likha hai
#         st.markdown("""
#         <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; margin-top: 5px;">
#             <div style="background-color: #1E88E5; border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);">
#                 <span style="color: white; font-size: 16px;">🤖</span> 
#             </div>
#             <span style="font-size: 18px; font-weight: bold; font-family: sans-serif;">Custom ChatGPT</span>
#         </div>
#         """, unsafe_allow_html=True)

#         # 2. New chat button
#         st.button("+ New chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("### CHATS")
        
#         # 3. Chat History ki list
#         for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
#             chat_title = "New Chat"
#             for m in msgs_dict:
#                 if m["role"] == "user":
#                     chat_title = m["content"][:25] + "..." 
#                     break
            
#             st.button(f"💬 {chat_title}", key=f"btn_{chat_id}", on_click=load_chat, args=(chat_id,), use_container_width=True)
        
#         for _ in range(5):
#             st.markdown("") 
            
#         st.markdown("---")
#         st.markdown("### SETTINGS")
#         st.markdown("⚙️ Model & behavior")
        
#         st.markdown("### ACCOUNT")
#         masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
#         st.markdown(f"🔑 Key: {masked_key}")
        
#         st.button("🔄 Change API key", on_click=logout, use_container_width=True)

#     # Main Chat Area
#     if len(st.session_state.messages) == 0:
#         st.session_state.messages.append(SystemMessage(content="You are a helpful assistant."))

#     # Render previous messages
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             with st.chat_message("user"):
#                 st.write(msg.content)
#         elif isinstance(msg, AIMessage):
#             with st.chat_message("assistant"):
#                 st.write(msg.content)

#     # Bottom Chat Input
#     user_prompt = st.chat_input("Message your assistant ...")

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))
        
#         with st.chat_message("user"):
#             st.write(user_prompt)

#         with st.spinner("Thinking..."):
#             try:
#                 # Chat processing with GPT model
#                 chat = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.7, api_key=st.session_state.api_key)
#                 response = chat.invoke(st.session_state.messages)
                
#                 st.session_state.messages.append(AIMessage(content=response.content))
                
#                 with st.chat_message("assistant"):
#                     st.write(response.content)
                
#                 save_current_chat()
#                 st.rerun() 
                
#             except Exception as e:
#                 st.error(f"API Error: ({e})")




# import streamlit as st
# import json
# import os
# from datetime import datetime
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# # File jahan chats save hongi
# HISTORY_FILE = "chat_history.json"

# # Page Configuration
# st.set_page_config(
#     page_title='Custom ChatGPT',
#     page_icon='🤖',
#     layout='wide'
# )

# # ==========================================
# # HELPER FUNCTIONS FOR HISTORY
# # ==========================================
# def load_all_chats():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as f:
#             try:
#                 return json.load(f)
#             except:
#                 return {}
#     return {}

# def save_all_chats():
#     with open(HISTORY_FILE, "w") as f:
#         json.dump(st.session_state.all_chats, f)

# def convert_to_dict_msgs(lc_msgs):
#     msgs = []
#     for m in lc_msgs:
#         if isinstance(m, SystemMessage): msgs.append({"role": "system", "content": m.content})
#         elif isinstance(m, HumanMessage): msgs.append({"role": "user", "content": m.content})
#         elif isinstance(m, AIMessage): msgs.append({"role": "assistant", "content": m.content})
#     return msgs

# def convert_to_langchain_msgs(dict_msgs):
#     msgs = []
#     for m in dict_msgs:
#         if m["role"] == "system": msgs.append(SystemMessage(content=m["content"]))
#         elif m["role"] == "user": msgs.append(HumanMessage(content=m["content"]))
#         elif m["role"] == "assistant": msgs.append(AIMessage(content=m["content"]))
#     return msgs

# # 1. Session State Initialization
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = None
# if 'all_chats' not in st.session_state:
#     st.session_state.all_chats = load_all_chats()
# if 'current_chat_id' not in st.session_state:
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# if 'messages' not in st.session_state:
#     st.session_state.messages = []
    
# # Nayi session states model aur temperature ke liye
# if 'selected_model' not in st.session_state:
#     st.session_state.selected_model = 'gpt-4o-mini'
# if 'temperature' not in st.session_state:
#     st.session_state.temperature = 0.7

# # ==========================================
# # ACTION HANDLERS
# # ==========================================
# def login():
#     st.session_state.api_key = st.session_state.api_key_input

# def logout():
#     st.session_state.api_key = None
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def clear_chat():
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def load_chat(chat_id):
#     st.session_state.current_chat_id = chat_id
#     st.session_state.messages = convert_to_langchain_msgs(st.session_state.all_chats[chat_id])

# def save_current_chat():
#     if len(st.session_state.messages) > 1:
#         st.session_state.all_chats[st.session_state.current_chat_id] = convert_to_dict_msgs(st.session_state.messages)
#         save_all_chats()

# # ==========================================
# # STATE 1: LOGIN PAGE
# # ==========================================
# if not st.session_state.api_key:
#     st.markdown("<h1 style='text-align: center;'>Welcome to Custom ChatGPT</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center;'>Please enter your API Key to access the chat.</p>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         with st.form("login_form"):
#             st.text_input("OpenAI API Key", type="password", key="api_key_input", placeholder="sk-...")
#             st.form_submit_button("Login", use_container_width=True, on_click=login)

# # ==========================================
# # STATE 2: CHAT PAGE (ChatGPT UI)
# # ==========================================
# else:
#     # Sidebar Setup
#     with st.sidebar:
        
#         # Logo aur Custom ChatGPT Title
#         st.markdown("""
#         <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; margin-top: 5px;">
#             <div style="background-color: #1E88E5; border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 2px 5px rgba(0,0,0,0.2);">
#                 <span style="color: white; font-size: 16px;">🤖</span> 
#             </div>
#             <span style="font-size: 18px; font-weight: bold; font-family: sans-serif;">Custom ChatGPT</span>
#         </div>
#         """, unsafe_allow_html=True)

#         # New chat button
#         st.button("+ New chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("### CHATS")
        
#         # Chat History list
#         for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
#             chat_title = "New Chat"
#             for m in msgs_dict:
#                 if m["role"] == "user":
#                     chat_title = m["content"][:25] + "..." 
#                     break
            
#             st.button(f"💬 {chat_title}", key=f"btn_{chat_id}", on_click=load_chat, args=(chat_id,), use_container_width=True)
        
#         for _ in range(5):
#             st.markdown("") 
            
#         st.markdown("---")
        
#         # ==========================================
#         # UPDATE: Model & Behavior Expander
#         # ==========================================
#         st.markdown("### SETTINGS")
#         with st.expander("⚙️ Model & behavior"):
#             # Model Select Box
#             st.selectbox(
#                 "Select Model", 
#                 options=['gpt-4o-mini', 'gpt-4o', 'gpt-3.5-turbo'], 
#                 key="selected_model" # Ye directly session_state ko update karega
#             )
#             # Temperature Slider (0.0 to 2.0)
#             st.slider(
#                 "Temperature", 
#                 min_value=0.0, 
#                 max_value=2.0, 
#                 step=0.1, 
#                 key="temperature" # Ye directly session_state ko update karega
#             )
        
#         st.markdown("### ACCOUNT")
#         masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
#         st.markdown(f"🔑 Key: {masked_key}")
        
#         st.button("🔄 Change API key", on_click=logout, use_container_width=True)

#     # Main Chat Area
#     if len(st.session_state.messages) == 0:
#         st.session_state.messages.append(SystemMessage(content="You are a helpful assistant."))

#     # Render previous messages
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             with st.chat_message("user"):
#                 st.write(msg.content)
#         elif isinstance(msg, AIMessage):
#             with st.chat_message("assistant"):
#                 st.write(msg.content)

#     # Bottom Chat Input
#     user_prompt = st.chat_input("Message your assistant ...")

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))
        
#         with st.chat_message("user"):
#             st.write(user_prompt)

#         with st.spinner("Thinking..."):
#             try:
#                 # UPDATE: Yahan selected_model aur temperature variable use ho rahe hain
#                 chat = ChatOpenAI(
#                     model_name=st.session_state.selected_model, 
#                     temperature=st.session_state.temperature, 
#                     api_key=st.session_state.api_key
#                 )
#                 response = chat.invoke(st.session_state.messages)
                
#                 st.session_state.messages.append(AIMessage(content=response.content))
                
#                 with st.chat_message("assistant"):
#                     st.write(response.content)
                
#                 save_current_chat()
#                 st.rerun() 
                
#             except Exception as e:
#                 st.error(f"API Error: ({e})")







# import streamlit as st
# import json
# import os
# from datetime import datetime
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(), override=True)

# HISTORY_FILE = "chat_history.json"

# # ==========================================
# # PAGE CONFIGURATION (Expanded layout)
# # ==========================================
# st.set_page_config(
#     page_title='Premium Custom ChatGPT',
#     page_icon='✨',
#     layout='wide',
#     initial_sidebar_state='expanded'
# )

# # ==========================================
# # CUSTOM CSS (UI MAGIC)
# # ==========================================
# st.markdown("""
# <style>
#     /* Google Fonts Import for modern look */
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
#     html, body, [class*="css"] {
#         font-family: 'Inter', sans-serif !important;
#     }
    
#     /* Login Page Premium Title */
#     .main-title {
#         background: -webkit-linear-gradient(45deg, #3b82f6, #9333ea);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 3.5rem;
#         font-weight: 800;
#         text-align: center;
#         margin-bottom: 0px;
#         padding-bottom: 10px;
#     }
#     .sub-title {
#         text-align: center;
#         color: #6b7280;
#         font-size: 1.1rem;
#         margin-bottom: 30px;
#     }

#     /* Button Animations & Hover Effects */
#     div.stButton > button {
#         border-radius: 8px;
#         font-weight: 500;
#         transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
#     }
#     div.stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#     }

#     /* Login Form Beautiful Container */
#     [data-testid="stForm"] {
#         border-radius: 16px;
#         box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.1);
#         padding: 2.5rem !important;
#         border: 1px solid rgba(147, 51, 234, 0.1);
#     }

#     /* Expander Design */
#     .streamlit-expanderHeader {
#         font-weight: 600 !important;
#         border-radius: 8px;
#     }
    
#     /* Input Box styling */
#     .stTextInput > div > div > input {
#         border-radius: 8px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ==========================================
# # HELPER FUNCTIONS FOR HISTORY
# # ==========================================
# def load_all_chats():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as f:
#             try:
#                 return json.load(f)
#             except:
#                 return {}
#     return {}

# def save_all_chats():
#     with open(HISTORY_FILE, "w") as f:
#         json.dump(st.session_state.all_chats, f)

# def convert_to_dict_msgs(lc_msgs):
#     msgs = []
#     for m in lc_msgs:
#         if isinstance(m, SystemMessage): msgs.append({"role": "system", "content": m.content})
#         elif isinstance(m, HumanMessage): msgs.append({"role": "user", "content": m.content})
#         elif isinstance(m, AIMessage): msgs.append({"role": "assistant", "content": m.content})
#     return msgs

# def convert_to_langchain_msgs(dict_msgs):
#     msgs = []
#     for m in dict_msgs:
#         if m["role"] == "system": msgs.append(SystemMessage(content=m["content"]))
#         elif m["role"] == "user": msgs.append(HumanMessage(content=m["content"]))
#         elif m["role"] == "assistant": msgs.append(AIMessage(content=m["content"]))
#     return msgs

# # ==========================================
# # SESSION STATE INITIALIZATION
# # ==========================================
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = None
# if 'all_chats' not in st.session_state:
#     st.session_state.all_chats = load_all_chats()
# if 'current_chat_id' not in st.session_state:
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# if 'messages' not in st.session_state:
#     st.session_state.messages = []
# if 'selected_model' not in st.session_state:
#     st.session_state.selected_model = 'gpt-4o-mini'
# if 'temperature' not in st.session_state:
#     st.session_state.temperature = 0.7

# # ==========================================
# # ACTION HANDLERS
# # ==========================================
# def login():
#     st.session_state.api_key = st.session_state.api_key_input

# def logout():
#     st.session_state.api_key = None
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def clear_chat():
#     st.session_state.messages = []
#     st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def load_chat(chat_id):
#     st.session_state.current_chat_id = chat_id
#     st.session_state.messages = convert_to_langchain_msgs(st.session_state.all_chats[chat_id])

# def save_current_chat():
#     if len(st.session_state.messages) > 1:
#         st.session_state.all_chats[st.session_state.current_chat_id] = convert_to_dict_msgs(st.session_state.messages)
#         save_all_chats()

# # ==========================================
# # STATE 1: PREMIUM LOGIN PAGE
# # ==========================================
# if not st.session_state.api_key:
#     # Spacer
#     st.markdown("<br><br>", unsafe_allow_html=True)
    
#     # Beautiful Title
#     st.markdown("<h1 class='main-title'>Custom ChatGPT</h1>", unsafe_allow_html=True)
#     st.markdown("<p class='sub-title'>Unlock the power of AI. Enter your API Key to continue.</p>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns([1, 1.2, 1])
#     with col2:
#         with st.form("login_form"):
#             st.text_input("OpenAI API Key", type="password", key="api_key_input", placeholder="sk-proj-...", help="Your key is secure and only used for this session.")
#             st.markdown("<br>", unsafe_allow_html=True)
#             st.form_submit_button("🚀 Start Chatting", use_container_width=True, on_click=login)

# # ==========================================
# # STATE 2: CHAT INTERFACE
# # ==========================================
# else:
#     # --- Sleek Sidebar ---
#     with st.sidebar:
#         # Modern Gradient Logo Header
#         st.markdown("""
#         <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1)); padding: 12px; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; gap: 12px; border: 1px solid rgba(147, 51, 234, 0.2);">
#             <div style="background: linear-gradient(135deg, #3b82f6, #9333ea); border-radius: 8px; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
#                 <span style="color: white; font-size: 20px;">✨</span> 
#             </div>
#             <span style="font-size: 1.1rem; font-weight: 700; background: -webkit-linear-gradient(45deg, #3b82f6, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Custom GPT</span>
#         </div>
#         """, unsafe_allow_html=True)

#         st.button("➕ New Chat", on_click=clear_chat, use_container_width=True, type="primary")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         st.markdown("<p style='font-size: 0.8rem; color: #888; font-weight: 600; margin-bottom: -10px;'>RECENT CHATS</p>", unsafe_allow_html=True)
#         st.markdown("---")
        
#         # Chat History List (styled as secondary buttons)
#         for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
#             chat_title = "New Chat"
#             for m in msgs_dict:
#                 if m["role"] == "user":
#                     chat_title = m["content"][:25] + "..." 
#                     break
            
#             st.button(f"💬 {chat_title}", key=f"btn_{chat_id}", on_click=load_chat, args=(chat_id,), use_container_width=True)
        
#         for _ in range(5):
#             st.markdown("") 
            
#         st.markdown("<p style='font-size: 0.8rem; color: #888; font-weight: 600; margin-bottom: -10px;'>SETTINGS</p>", unsafe_allow_html=True)
#         st.markdown("---")
        
#         with st.expander("⚙️ Model & behavior"):
#             st.selectbox("Model", options=['gpt-4o-mini', 'gpt-4o', 'gpt-3.5-turbo'], key="selected_model")
#             st.slider("Temperature", min_value=0.0, max_value=2.0, step=0.1, key="temperature")
        
#         st.markdown("<br>", unsafe_allow_html=True)
#         masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
        
#         # Account info card
#         st.markdown(f"""
#         <div style='background-color: rgba(0,0,0,0.03); padding: 10px; border-radius: 8px; margin-bottom: 10px; text-align: center; border: 1px solid rgba(0,0,0,0.05);'>
#             <span style='font-size: 0.85rem; color: #555;'>Logged in with key:<br><b>{masked_key}</b></span>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.button("🔓 Logout", on_click=logout, use_container_width=True)

#     # --- Main Chat Area ---
#     if len(st.session_state.messages) == 0:
#         st.session_state.messages.append(SystemMessage(content="You are a helpful and intelligent AI assistant."))

#     # Show a beautiful Empty State if no messages yet
#     if len(st.session_state.messages) == 1:
#         st.markdown("""
#         <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh;'>
#             <h2 style='color: #888; font-weight: 600;'>How can I help you today? ✨</h2>
#             <p style='color: #aaa;'>Start typing a message below to begin a conversation.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     # Render chat messages with custom Avatars
#     for msg in st.session_state.messages:
#         if isinstance(msg, HumanMessage):
#             with st.chat_message("user", avatar="👤"):
#                 st.markdown(msg.content)
#         elif isinstance(msg, AIMessage):
#             with st.chat_message("assistant", avatar="✨"):
#                 st.markdown(msg.content)

#     # --- Chat Input ---
#     user_prompt = st.chat_input("Message your Custom AI ...")

#     if user_prompt:
#         st.session_state.messages.append(HumanMessage(content=user_prompt))
        
#         with st.chat_message("user", avatar="👤"):
#             st.markdown(user_prompt)

#         with st.chat_message("assistant", avatar="✨"):
#             with st.spinner("Generating response..."):
#                 try:
#                     chat = ChatOpenAI(
#                         model_name=st.session_state.selected_model, 
#                         temperature=st.session_state.temperature, 
#                         api_key=st.session_state.api_key
#                     )
#                     response = chat.invoke(st.session_state.messages)
                    
#                     st.markdown(response.content)
#                     st.session_state.messages.append(AIMessage(content=response.content))
                    
#                     save_current_chat()
                    
#                 except Exception as e:
#                     st.error(f"API Error: ({e})")



import streamlit as st
import json
import os
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

HISTORY_FILE = "chat_history.json"

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title='Aura AI - Custom ChatGPT',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='expanded'
)

# # Streamlit ke default Header (Fork/GitHub) aur Footer ko hide karne ka CSS
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# Streamlit ke default Header aur Footer ko hide karne ka CSS (Sidebar button ko safe rakhte hue)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Sidebar collapse/expand button ko hamesha visible rakhein */
            [data-testid="collapsedControl"] {
                display: block !important;
                visibility: visible !important;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# ADVANCED CUSTOM CSS FOR PREMIUM GLASSMORPHIC UI
# ==========================================
st.markdown("""
<style>
    /* Global Fonts & Futuristic Dark Backdrop */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #0b0c10 !important;
        color: #e2e8f0 !important;
    }
    
    /* Full App Glass effect */
    .stApp {
        background: radial-gradient(circle at top right, rgba(79, 70, 229, 0.08), transparent), 
                    radial-gradient(circle at bottom left, rgba(147, 51, 234, 0.05), transparent),
                    #0c0d14 !important;
    }

    /* Sidebar Aesthetic customization */
    [data-testid="stSidebar"] {
        background-color: #08090d !important;
        border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
        padding-top: 10px;
    }
    
    /* Branding design matching Aura AI */
    .brand-container {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(139, 92, 246, 0.1));
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        border: 1px solid rgba(99, 102, 241, 0.15);
    }
    .brand-logo {
        background: linear-gradient(135deg, #2563eb, #8b5cf6);
        border-radius: 10px;
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0px 4px 12px rgba(37, 99, 235, 0.3);
    }
    .brand-title {
        font-size: 1.15rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #3b82f6, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Gradient Primary Buttons (New Chat) */
    div.stButton > button[key*="new_chat"] {
        background: linear-gradient(135deg, #312e81, #1e1b4b);
        color: #a5b4fc !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        font-weight: 600;
        border-radius: 10px;
        height: 46px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button[key*="new_chat"]:hover {
        background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
        color: #ffffff !important;
        box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);
        border: 1px solid transparent !important;
        transform: translateY(-1px);
    }

    /* Custom Suggestion cards styling */
    .suggestion-container {
        display: flex;
        gap: 12px;
        justify-content: center;
        margin-top: 24px;
        flex-wrap: wrap;
    }
    
    /* Modern sleek input fields inside sidebar */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background-color: #0f111a !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #e2e8f0 !important;
        border-radius: 8px !important;
    }

    /* Message view bubbles customized padding and card blur */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #4f46e5 !important;
    }
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, #3b82f6, #a855f7) !important;
    }
    
    .stChatMessage {
        border-radius: 12px;
        margin-bottom: 12px;
        border: 1px solid rgba(255,255,255,0.02) !important;
    }

    /* Premium Welcome UI screen styling */
    .welcome-header {
        font-size: 3.8rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 5px;
    }
    .welcome-subtext {
        color: #94a3b8;
        font-size: 1.15rem;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Sidebar elements scroll & spacing */
    .sidebar-section-title {
        font-size: 0.72rem;
        font-weight: 700;
        color: #475569;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 24px;
        margin-bottom: 8px;
    }
    
    /* Login Screen Container styling */
    .login-wrapper {
        border-radius: 20px;
        background: rgba(13, 14, 22, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA HANDLERS
# ==========================================
def load_all_chats():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try: return json.load(f)
            except: return {}
    return {}

def save_all_chats():
    with open(HISTORY_FILE, "w") as f:
        json.dump(st.session_state.all_chats, f)

def convert_to_dict_msgs(lc_msgs):
    msgs = []
    for m in lc_msgs:
        if isinstance(m, SystemMessage): msgs.append({"role": "system", "content": m.content})
        elif isinstance(m, HumanMessage): msgs.append({"role": "user", "content": m.content})
        elif isinstance(m, AIMessage): msgs.append({"role": "assistant", "content": m.content})
    return msgs

def convert_to_langchain_msgs(dict_msgs):
    msgs = []
    for m in dict_msgs:
        if m["role"] == "system": msgs.append(SystemMessage(content=m["content"]))
        elif m["role"] == "user": msgs.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant": msgs.append(AIMessage(content=m["content"]))
    return msgs

# Session States
if 'api_key' not in st.session_state: st.session_state.api_key = None
if 'all_chats' not in st.session_state: st.session_state.all_chats = load_all_chats()
if 'current_chat_id' not in st.session_state: st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if 'messages' not in st.session_state: st.session_state.messages = []
if 'selected_model' not in st.session_state: st.session_state.selected_model = 'gpt-4o-mini'
if 'temperature' not in st.session_state: st.session_state.temperature = 0.7

def login():
    st.session_state.api_key = st.session_state.api_key_input

def logout():
    st.session_state.api_key = None
    st.session_state.messages = []
    st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clear_chat():
    st.session_state.messages = []
    st.session_state.current_chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_chat(chat_id):
    st.session_state.current_chat_id = chat_id
    st.session_state.messages = convert_to_langchain_msgs(st.session_state.all_chats[chat_id])

def save_current_chat():
    if len(st.session_state.messages) > 1:
        st.session_state.all_chats[st.session_state.current_chat_id] = convert_to_dict_msgs(st.session_state.messages)
        save_all_chats()

# Preset input triggered on prompt selection click
def handle_preset_click(preset_text):
    st.session_state.messages.append(HumanMessage(content=preset_text))
    # trigger chatbot request directly (will generate responses)
    st.session_state.preset_triggered = preset_text

# ==========================================
# STATE 1: LOGIN PAGE (STUNNING BLUR CARD)
# ==========================================
if not st.session_state.api_key:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <div style="display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #2563eb, #8b5cf6); border-radius: 16px; width: 60px; height: 60px; margin-bottom: 16px; box-shadow: 0 8px 24px rgba(37,99,235,0.4)">
                <span style="color: white; font-size: 32px;">✨</span>
            </div>
            <h1 style="font-size: 2.8rem; font-weight: 800; margin: 0; background: -webkit-linear-gradient(45deg, #3b82f6, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Aura AI</h1>
            <p style="color: #64748b; font-size: 1.1rem; margin-top: 5px;">Unlock the power of customized conversational intelligence</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form", clear_on_submit=True):
            st.markdown("<p style='font-size:0.9rem; font-weight:600; margin-bottom:-5px; color:#94a3b8;'>OpenAI API Key</p>", unsafe_allow_html=True)
            st.text_input("", type="password", key="api_key_input", placeholder="sk-proj-...", help="Your key runs strictly in your current tab.")
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            st.form_submit_button("🔑 Unlock Assistant", use_container_width=True, on_click=login)

# ==========================================
# STATE 2: THE DIGITAL CHATROOM (CHAT UI)
# ==========================================
else:
    # --- The Cyber Sidebar ---
    with st.sidebar:
        # Logo branding header
        st.markdown("""
        <div class="brand-container">
            <div class="brand-logo">🤖</div>
            <div style="display: flex; flex-direction: column;">
                <span class="brand-title">Aura AI</span>
                <span style="font-size: 0.72rem; color: #64748b; font-weight: 500;">Premium custom assistant</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("➕ New Chat", on_click=clear_chat, use_container_width=True, key="new_chat")
        
        st.markdown("<p class='sidebar-section-title'>History</p>", unsafe_allow_html=True)
        
        # Sidelisted Saved Chats
        history_shown = False
        for chat_id, msgs_dict in reversed(st.session_state.all_chats.items()):
            chat_title = "New Chat"
            for m in msgs_dict:
                if m["role"] == "user":
                    chat_title = m["content"][:24] + "..." 
                    break
            st.button(f"💬 {chat_title}", key=f"btn_{chat_id}", on_click=load_chat, args=(chat_id,), use_container_width=True)
            history_shown = True
            
        if not history_shown:
            st.markdown("<p style='font-size:0.8rem; color:#475569; font-style:italic; padding-left:10px;'>No previous sessions</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='sidebar-section-title'>Settings</p>", unsafe_allow_html=True)
        with st.expander("⚙️ Model & Behavior"):
            st.selectbox("Model", options=['gpt-4o-mini', 'gpt-4o', 'gpt-3.5-turbo'], key="selected_model")
            st.slider("Temperature", min_value=0.0, max_value=2.0, step=0.1, key="temperature")
        
        st.markdown("<p class='sidebar-section-title'>Identity</p>", unsafe_allow_html=True)
        masked_key = f"sk-...{st.session_state.api_key[-4:]}" if len(st.session_state.api_key) > 4 else "sk-..."
        
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.04); padding: 12px; border-radius: 10px; margin-bottom: 12px;'>
            <span style='font-size:0.75rem; color:#64748b; font-weight:600;'>CONNECTED KEY</span><br>
            <span style='font-family:monospace; font-size:0.85rem; color:#38bdf8; font-weight:bold;'>{masked_key}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.button("🔓 End Session", on_click=logout, use_container_width=True)

    # --- Main AI Canvas ---
    if len(st.session_state.messages) == 0:
        st.session_state.messages.append(SystemMessage(content="You are a helpful and intelligent AI assistant."))

    # EMPTY STATE SHOWING HOW CAN I HELP YOU TODAY + PREMIUM CARDS
    if len(st.session_state.messages) == 1:
        st.markdown("<div style='height: 12vh;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 class='welcome-header'>How can I help<br>you today?</h1>", unsafe_allow_html=True)
        st.markdown("<p class='welcome-subtext'>Design your code, solve questions, or explore new ideas</p>", unsafe_allow_html=True)
        
        # Premium clickable card prompts matching the aesthetic
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            if st.button("📝 Draft an email\n\n\n\n\n\nCompose professional text", use_container_width=True):
                handle_preset_click("Draft an email")
                st.rerun()
        with col_c2:
            if st.button("💡 Brainstorm ideas\n\n\n\n\n\nConcept & plan creation", use_container_width=True):
                handle_preset_click("Brainstorm ideas")
                st.rerun()
        with col_c3:
            if st.button("🔬 Explain a concept\n\n\n\n\n\nDetailed walkthroughs", use_container_width=True):
                handle_preset_click("Explain a concept")
                st.rerun()

    # Renders regular stream messages
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(msg.content)

    # Check for click-based presets
    user_prompt = st.chat_input("Message Aura...")
    
    # Check if a preset click was triggered
    preset_triggered = st.session_state.pop("preset_triggered", None)
    prompt_to_use = user_prompt or preset_triggered

    if prompt_to_use:
        if not preset_triggered: # Skip render if it is already done
            st.session_state.messages.append(HumanMessage(content=prompt_to_use))
            with st.chat_message("user"):
                st.markdown(prompt_to_use)

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                try:
                    chat = ChatOpenAI(
                        model_name=st.session_state.selected_model, 
                        temperature=st.session_state.temperature, 
                        api_key=st.session_state.api_key
                    )
                    response = chat.invoke(st.session_state.messages)
                    st.markdown(response.content)
                    st.session_state.messages.append(AIMessage(content=response.content))
                    save_current_chat()
                    st.rerun()
                except Exception as e:
                    st.error(f"API Error: ({e})")
