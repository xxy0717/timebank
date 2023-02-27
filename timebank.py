import streamlit as st
import time

# 设置页面标题
st.set_page_config(page_title="TimeBank App", page_icon=":hourglass_flowing_sand:")

# 定义全局变量
total_time = 0
adding_time = 0
subtracting_time = 0

# 定义计时器函数
def timer():
    global adding_time, subtracting_time
    while True:
        if adding_time > 0:
            adding_time += 1
        if subtracting_time > 0:
            subtracting_time += 1
        time.sleep(1)

# 开始计时器
timer_thread = st.experimental_background_thread(timer)

# 定义主函数
def main():
    global total_time, adding_time, subtracting_time

    # 显示标题和页面描述
    st.title("TimeBank App")
    st.write("Add or subtract time with the click of a button!")

    # 显示累计时长柱状图和时长数值
    st.write("")
    st.write(f"**Total time:** {total_time} seconds")
    st.progress(total_time/100)

    # 显示添加时长按钮
    st.write("")
    if adding_time == 0:
        add_button = st.button("Start Adding Time")
    else:
        add_button = st.button("Stop Adding Time")
    if add_button:
        if adding_time == 0:
            adding_time = 1
        else:
            total_time += adding_time
            adding_time = 0

    # 显示扣减时长按钮
    st.write("")
    if subtracting_time == 0:
        subtract_button = st.button("Start Subtracting Time")
    else:
        subtract_button = st.button("Stop Subtracting Time")
    if subtract_button:
        if subtracting_time == 0:
            subtracting_time = 1
        else:
            total_time -= subtracting_time
            subtracting_time = 0

# 运行应用
if __name__ == "__main__":
    main()
