class Index:
    YEAR = "年份"
    WATER_RESOURSE = "水资源总量"
    RAIN = "年降雨量"
    TEMP = "年均温"
    HUM = "年平均相对湿度"
    TIME = "年日照时间"
    X = [RAIN, TEMP, HUM, TIME]
    X_ = [RAIN, TIME]


class Label:
    WATER_RESOURSE = "water resourse"
    RAIN = "rain"
    TEMP = "average temperature"
    HUM = "average humidity"
    TIME = "sun shining time"


class CityName:
    HEYUAN = "河源"
    SHENZHEN = "深圳"
    BEIJING = "北京"
