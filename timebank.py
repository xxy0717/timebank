import streamlit as st
import time

# 全局变量
total_time = 0
is_adding_time = False
is_deducting_time = False

def add_time():
    global total_time, is_adding_time, is_deducting_time
    if is_adding_time:
        is_adding_time = False
        add_button.label("开始增加")
        st.experimental_rerun()
    else:
        is_adding_time = True
        add_button.label("结束增加")
        with st.empty():
            while is_adding_time:
                total_time += 1
                st.write(total_time)
                time.sleep(1)
                st.experimental_rerun()

def deduct_time():
    global total_time, is_adding_time, is_deducting_time
    if is_deducting_time:
        is_deducting_time = False
        deduct_button.label("开始扣减")
        st.experimental_rerun()
    else:
        is_deducting_time = True
        deduct_button.label("结束扣减")
        with st.empty():
            while is_deducting_time:
                if total_time > 0:
                    total_time -= 1
                st.write(total_time)
                time.sleep(1)
                st.experimental_rerun()

def main():
    global add_button, deduct_button
    st.write("# 时间银行")
    st.write("累计时长：", total_time, "秒")
    st.bar_chart(total_time)
    add_button = st.button("开始增加")
    add_button.on_click(add_time)
    deduct_button = st.button("开始扣减")
    deduct_button.on_click(deduct_time)

if __name__ == '__main__':
    main()
