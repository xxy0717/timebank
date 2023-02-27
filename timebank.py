import streamlit as st
import time


def main():
    st.set_page_config(page_title='Time Bank', page_icon=':money_with_wings:')
    st.title('Time Bank')

    add_time = 0
    deduct_time = 0
    is_adding = False
    is_deducting = False

    if 'add_time' in st.session_state:
        add_time = st.session_state.add_time

    if 'deduct_time' in st.session_state:
        deduct_time = st.session_state.deduct_time

    if 'is_adding' in st.session_state:
        is_adding = st.session_state.is_adding

    if 'is_deducting' in st.session_state:
        is_deducting = st.session_state.is_deducting

    add_button = st.button('开始增加')
    deduct_button = st.button('开始扣减')

    if add_button and not is_adding:
        is_adding = True
        st.session_state.is_adding = is_adding
        with st.empty():
            t0 = time.time()
            while is_adding:
                t1 = time.time()
                add_time += t1 - t0
                t0 = t1
                st.session_state.add_time = add_time
                st.session_state.is_adding = is_adding
                st.write(f'累计时长：{add_time:.2f}秒')
                time.sleep(0.1)

    if deduct_button and not is_deducting:
        is_deducting = True
        st.session_state.is_deducting = is_deducting
        with st.empty():
            t0 = time.time()
            while is_deducting:
                t1 = time.time()
                deduct_time += t1 - t0
                t0 = t1
                st.session_state.deduct_time = deduct_time
                st.session_state.is_deducting = is_deducting
                st.write(f'累计时长：{add_time - deduct_time:.2f}秒')
                time.sleep(0.1)

    if is_adding:
        end_add_button = st.button('结束增加')
        if end_add_button:
            is_adding = False
            st.session_state.is_adding = is_adding

    if is_deducting:
        end_deduct_button = st.button('结束扣减')
        if end_deduct_button:
            is_deducting = False
            st.session_state.is_deducting = is_deducting

    st.write(f'累计时长：{add_time - deduct_time:.2f}秒')


if __name__ == '__main__':
    main()
