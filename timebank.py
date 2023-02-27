import streamlit as st
import time

# 设置页面标题
st.set_page_config(page_title='时长增加和扣减应用')

# 初始化累计时长
total_time = 0

# 开始计时
def start_timing():
    start_time = time.time()
    return start_time

# 结束计时
def end_timing(start_time):
    end_time = time.time()
    time_elapsed = end_time - start_time
    return time_elapsed

# 显示累计时长
def display_total_time():
    st.write('累计时长为：', total_time, '秒')

# 主函数
def main():
    global total_time
    st.title('时长增加和扣减应用')
    add_time_started = False
    sub_time_started = False
    add_time_elapsed = 0
    sub_time_elapsed = 0
    while True:
        # 显示累计时长
        display_total_time()
        # 开始增加时长
        if st.button('开始增加'):
            if not add_time_started:
                add_time_started = True
                st.write('开始增加时长')
                add_time_start_time = start_timing()
            else:
                st.write('计时已经开始')
        # 结束增加时长
        if st.button('结束增加'):
            if add_time_started:
                add_time_started = False
                st.write('结束增加时长')
                add_time_elapsed = end_timing(add_time_start_time)
                total_time += add_time_elapsed
            else:
                st.write('请先开始增加时长')
        # 开始扣减时长
        if st.button('开始扣减'):
            if not sub_time_started:
                sub_time_started = True
                st.write('开始扣减时长')
                sub_time_start_time = start_timing()
            else:
                st.write('计时已经开始')
        # 结束扣减时长
        if st.button('结束扣减'):
            if sub_time_started:
                sub_time_started = False
                st.write('结束扣减时长')
                sub_time_elapsed = end_timing(sub_time_start_time)
                total_time -= sub_time_elapsed
                if total_time < 0:
                    total_time = 0
            else:
                st.write('请先开始扣减时长')
        # 增加和扣减时长的计时
        if add_time_started:
            add_time_elapsed = end_timing(add_time_start_time)
            st.write('已经增加时长：', add_time_elapsed, '秒')
        if sub_time_started:
            sub_time_elapsed = end_timing(sub_time_start_time)
            st.write('已经扣减时长：', sub_time_elapsed, '秒')
        # 设置刷新间隔为0.1秒
        time.sleep(0.1)

if __name__ == '__main__':
    main()
