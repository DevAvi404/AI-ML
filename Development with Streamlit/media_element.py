import streamlit as st

st.title("Basic media I/o section.", anchor=False)
st.divider()
st.header("Input your files", divider=True)

# image 
images = st.file_uploader("Enter your picture",
                  type=['jpg', 'jpeg', 'png'],
                  accept_multiple_files=False
                 )

st.divider()

# audio
audio = st.file_uploader("Enter your voice",
                  type=['mp3', 'ogg', 'flac'],
                  accept_multiple_files=False
                 )

st.divider()

# video
video = st.file_uploader("Enter your voice",
                  type=['mp4', 'mkv'],
                  accept_multiple_files=False
                 )

st.divider()

# submit
pressed = st.button("Submit", type="primary")

if pressed:
    
    if images and audio and video:
        col = st.columns(len(images))

        for i, j in enumerate(images):
            with col[i]:
                st.image(j) # showing image in columns

        st.audio(audio)
        st.video(video)

        st.success("Your file  is uploaded successfully")
    
    else:
        st.error("You must upload these file properly")
