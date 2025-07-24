import streamlit as st

# Title and greeting
st.title("💖 Relationship Agreement App")
st.write("Made with love by Ayush 💌")

# Slider: Years to be together
age = st.slider("How many years you want us to be together:", 0, 100, 25)
st.write(f"📝 Agreement of love is for: **{age} years**")

# Selectbox: Type of relationship
options = ["First Date", "Pehle jaan lete hain", "Do you like me?", "Your phone number"]
choice = st.selectbox("Choose your relation you want with me:", options)  # ✅ FIXED here
st.write(f"💌 You selected: **{choice}**")

# Text input: Message
message = st.text_input("Write a message to me (optional):")

# Submit button
if st.button("Send 💘"):
    if message.strip() == "":
        st.warning("You didn't write a message, but your love is still felt 😊")
    else:
        st.success("Message received! ❤️")
        st.write(f"💌 Your message: _{message}_")

    # Special response if user picks "Do you like me?"
    if choice.lower() == "do you like me?":
        st.balloons()
        st.write("🥰 Of course I do... forever and always! 💖")
    else:
        st.snow()

# Title and greeting
st.title("💖 Relationship Agreement App")
st.write("Made with love by Ayush 💌")

# Slider: Years to be together
age = st.slider("How many years you want us to be together:", 0, 100, 25)
st.write(f"📝 Agreement of love is for: **{age} years**")

# Selectbox: Type of relationship
options = ["First Date", "Pehle jaan lete hain", "Do you like me?", "Your phone number"]
choice = st.selectbox("Choose your relation you want with me:", options)  # ✅ FIXED here
st.write(f"💌 You selected: **{choice}**")

# Text input: Message
message = st.text_input("Write a message to me (optional):")

# Submit button
if st.button("Send 💘"):
    if message.strip() == "":
        st.warning("You didn't write a message, but your love is still felt 😊")
    else:
        st.success("Message received! ❤️")
        st.write(f"💌 Your message: _{message}_")

    # Special response if user picks "Do you like me?"
    if choice.lower() == "do you like me?":
        st.balloons()
        st.write("🥰 Of course I do... forever and always! 💖")
    else:
        st.snow()

