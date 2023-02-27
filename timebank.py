import streamlit as st

def main():
    st.set_page_config(page_title='时长银行')
    st.title('时长银行')
    
    add_time = 0
    minus_time = 0
    total_time = 0

    if st.button('开始增加', key='add_start'):
        add_time = st.session_state.add_time or 0
        add_time -= st.session_state.minus_time or 0
        add_time -= st.session_state.add_end_time or 0
        st.session_state.add_start_time = st.session_state.time_elapsed or 0
    if st.button('结束增加', key='add_end'):
        add_end_time = st.session_state.time_elapsed or 0
        st.session_state.add_end_time = add_end_time
        total_time += max(0, add_end_time - st.session_state.add_start_time)
        st.session_state.add_time = add_time
    if st.button('开始扣减', key='minus_start'):
        minus_time = st.session_state.minus_time or 0
        minus_time -= st.session_state.add_time or 0
        minus_time -= st.session_state.minus_end_time or 0
        st.session_state.minus_start_time = st.session_state.time_elapsed or 0
    if st.button('结束扣减', key='minus_end'):
        minus_end_time = st.session_state.time_elapsed or 0
        st.session_state.minus_end_time = minus_end_time
        total_time -= min(0, minus_end_time - st.session_state.minus_start_time)
        st.session_state.minus_time = minus_time
        
    st.write(f'累计时长: {total_time}秒')
    
if __name__ == '__main__':
    main()
