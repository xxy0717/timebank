import streamlit as st

def main():
    st.title('时长管理系统')

    add_time = st.session_state.get('add_time', 0)
    sub_time = st.session_state.get('sub_time', 0)

    if st.button('开始增加'):
        st.session_state.add_time = add_time + st.session_state.time if 'time' in st.session_state else add_time

    if st.button('结束增加'):
        st.session_state.add_time = add_time + st.session_state.time - st.session_state.get('start_time', 0) if 'time' in st.session_state and 'start_time' in st.session_state else add_time

    if st.button('开始扣减'):
        st.session_state.sub_time = sub_time + st.session_state.time if 'time' in st.session_state else sub_time

    if st.button('结束扣减'):
        st.session_state.sub_time = sub_time + st.session_state.time - st.session_state.get('start_time', 0) if 'time' in st.session_state and 'start_time' in st.session_state else sub_time

    st.write(f'累计时长：{add_time - sub_time} 秒')

    if st.button('重置'):
        st.session_state.clear()

if __name__ == '__main__':
    main()
