import streamlit as st
import time
from PIL import Image
a,b,c=st.columns([0.5,0.1,0.4])

with a:
    img=Image.open("ojhajee.jpg")
    st.image(img,width=40)
lst=['HAPPY','BIRTHDAY','OJHA JEE ']
clr=['orange','blue','green']
with c:
    for i in range(len(lst)):
        time.sleep(1)
        st.balloons()
        time.sleep(1)
        st.markdown(f""" # :{clr[i]}[{lst[i]}] 🎉🎉🎉""")
        
    st.markdown("""# 🎇🎇🎇🎆🎆🎇🎇""")
