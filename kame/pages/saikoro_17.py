import random
import streamlit as st
import pandas as pd
import requests
import io

st.title("おみくじ")

if st.button("おみくじをひく"):
    suuji = random.randint(1, 100)
    if suuji %  17 == 16:
        st.write(f"{suuji}番 凶後大吉です。")
    elif suuji % 17 == 15:
        st.write(f"{suuji}番 凶後吉です。")
    elif suuji % 17 == 14:
        st.write(f"{suuji}番 小吉後吉です。")
    elif suuji % 17 == 13:
        st.write(f"{suuji}番 吉凶相央です。")
    elif suuji % 17 == 12:
        st.write(f"{suuji}番 吉凶相半です。")
    elif suuji % 17 == 11:
        st.write(f"{suuji}番 吉凶相交末吉です。")
    elif suuji % 17 == 10:
        st.write(f"{suuji}番 吉凶不分末吉です。")
    elif suuji % 17 == 9:
        st.write(f"{suuji}番 末吉です。")
    elif suuji % 17 == 8:
        st.write(f"{suuji}番 後凶です。")
    elif suuji % 17 == 7:
        st.write(f"{suuji}番 小吉です。")
    elif suuji % 17 == 6:
        st.write(f"{suuji}番 中吉です。")
    elif suuji % 17 == 5:
        st.write(f"{suuji}番 吉です。")
    elif suuji % 17 == 4:
        st.write(f"{suuji}番 吉凶末分末大吉です。")
    elif suuji % 17 == 3:
        st.write(f"{suuji}番 末大吉です。")
    elif suuji % 17 == 2:
        st.write(f"{suuji}番 向大吉です。")
    elif suuji % 17 == 1:
        st.write(f"{suuji}番 大吉です。")
    else: st.write(f"{suuji}番 大大吉です。")


from PIL import Image
url='https://www.omikuji-do.com/wordpress/wp-content/uploads/2021/05/35b5ad9d93b9b21f190cc99ebeb42fe1.png'
img = Image.open(io.BytesIO(requests.get(url).content))

st.image(img, use_container_width=True)
