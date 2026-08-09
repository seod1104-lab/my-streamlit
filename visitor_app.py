import streamlit as st
from supabase import create_client

# Supabase 연결
SUPABASE_URL = st.secrets["sb_publishable_aLkrm5Uzj3RxBdCZKWyiBw_D7OwveHw"]
SUPABASE_KEY = st.secrets["https://vxfzsenvzgqzdwdibfjm.supabase.co/rest/v1/"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 화면
st.title("방명록")

st.info("이 페이지에 접속하면 접속 IP 주소와 작성 시간이 기록됩니다.")

# 접속자의 IP
ip = st.context.ip_address

# 메시지 입력
message = st.text_area("메시지를 입력하세요")

if st.button("등록"):

    if message.strip():

        supabase.table("visitor_logs").insert({
            "ip_address": ip,
            "message": message
        }).execute()

        st.success("등록되었습니다!")

    else:
        st.warning("메시지를 입력해주세요.")
