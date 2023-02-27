import streamlit as st
import time

def main():
    st.title("时长管理器")
    add_time = st.session_state.add_time or 0
    subtract_time = st.session_state.subtract_time or 0
    total_time = add_time - subtract_time
    st.write(f"累计时长为：{total_time} 秒")
    start_time = None
    end_time = None
    
    if st.button('开始增加'):
        start_time = time.time()

    if st.button('结束增加'):
        end_time = time.time()

    if start_time is not None and end_time is not None:
        duration = int(end_time - start_time)
        add_time += duration
        st.session_state.add_time = add_time
        total_time = add_time - subtract_time
        st.write(f"累计时长为：{total_time} 秒")

    if st.button('开始扣减'):
        start_time = time.time()

    if st.button('结束扣减'):
        end_time = time.time()

    if start_time is not None and end_time is not None:
        duration = int(end_time - start_time)
        subtract_time += duration
        st.session_state.subtract_time = subtract_time
        total_time = add_time - subtract_time
        st.write(f"累计时长为：{total_time} 秒")

if __name__ == '__main__':
    main()
