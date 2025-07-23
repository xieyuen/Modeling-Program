class Index:
    YEAR = "年份"
    WATER_RESOURCE = "水资源总量"
    RAIN = "年降雨量"
    TEMP = "年均温"
    HUM = "年平均相对湿度"
    TIME = "年日照时间"
    X = [RAIN, TEMP, HUM, TIME]  # 四元自变量
    X_ = [RAIN, TIME]  # 二元自变量


class Label:
    WATER_RESOURSE = "water resource (m³)"
    RAIN = "rain (mm)"
    TEMP = "average temperature (℃)"
    HUM = "average humidity (%)"
    TIME = "sun shining time (h)"


class CityName:
    HEYUAN = "河源"
    SHENZHEN = "深圳"
    BEIJING = "北京"
