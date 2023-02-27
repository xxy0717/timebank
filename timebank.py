import streamlit as st

def main():
    add_time = st.session_state.get('add_time', 0) # 使用get方法获取变量，如果不存在则返回默认值0
    subtract_time = st.session_state.get('subtract_time', 0)
    
    if st.button('开始增加'):
        st.session_state.add_time = add_time
        st.session_state.start_time = st.session_state.time if 'time' in st.session_state else 0
    if st.button('结束增加'):
        add_time += st.session_state.time - st.session_state.start_time
        st.session_state.add_time = add_time
    
    if st.button('开始扣减'):
        st.session_state.subtract_time = subtract_time
        st.session_state.start_time = st.session_state.time if 'time' in st.session_state else 0
    if st.button('结束扣减'):
        subtract_time += st.session_state.time - st.session_state.start_time
        st.session_state.subtract_time = subtract_time
    
    total_time = add_time - subtract_time
    st.write(f'累计时长: {total_time} 秒')
