import streamlit as st
import time


def main():
    add_time = st.session_state.add_time or 0
    sub_time = st.session_state.sub_time or 0
    start_add = st.session_state.start_add or False
    start_subtract = st.session_state.start_subtract or False
    stop_add = st.session_state.stop_add or False
    stop_subtract = st.session_state.stop_subtract or False

    st.header('时长记录')
    st.subheader(f'累计时长: {add_time - sub_time:.2f}s')

    if not start_add and not stop_add:
        if st.button('开始增加'):
            start_add = True
            st.session_state.start_add = True
            st.session_state.add_time = add_time
    elif start_add and not stop_add:
        if st.button('结束增加'):
            start_add = False
            stop_add = True
            st.session_state.start_add = False
            st.session_state.stop_add = True
            st.session_state.add_time = add_time + time.time() - st.session_state.start_time

    if not start_subtract and not stop_subtract:
        if st.button('开始扣减'):
            start_subtract = True
            st.session_state.start_subtract = True
            st.session_state.sub_time = sub_time
    elif start_subtract and not stop_subtract:
        if st.button('结束扣减'):
            start_subtract = False
            stop_subtract = True
            st.session_state.start_subtract = False
            st.session_state.stop_subtract = True
            st.session_state.sub_time = sub_time + time.time() - st.session_state.start_time

    if start_add:
        st.write(f"已增加: {add_time + time.time() - st.session_state.start_time - sub_time:.2f}s")

    if start_subtract:
        st.write(f"已扣减: {sub_time + time.time() - st.session_state.start_time - add_time:.2f}s")


if __name__ == '__main__':
    if 'add_time' not in st.session_state:
        st.session_state.add_time = 0
    if 'sub_time' not in st.session_state:
        st.session_state.sub_time = 0
    if 'start_add' not in st.session_state:
        st.session_state.start_add = False
    if 'start_subtract' not in st.session_state:
        st.session_state.start_subtract = False
    if 'stop_add' not in st.session_state:
        st.session_state.stop_add = False
    if 'stop_subtract' not in st.session_state:
        st.session_state.stop_subtract = False
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()

    main()
