"""
    作者：
    功能：
    版本：2.0
    日期：
"""


def main():
    """
    主函数
    """
    print('请输入以下信息，用空格分隔')
    input_str = input('(1)PM2.5 (2)co:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    # 调用AQI计算函数
    aqi_val = cal_aqi(param_list)

    print('空气质量指数为：{}'.format(aqi_val))



if __name__ == '__main__':
    main()