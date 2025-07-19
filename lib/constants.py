from dataclasses import dataclass


@dataclass
class Index:
    YEAR = "年份"
    Y = WATER_RESOURSE = "水资源总量"
    RAIN = "年降雨量"
    TEMP = "年均温"
    HUM = "年平均相对湿度"
    TIME = "年日照时间"
    X = [RAIN, TEMP, HUM, TIME]
    X_ = [RAIN, TIME]


@dataclass
class Label:
    WATER_RESOURSE = "water resourse"
    RAIN = "rain"
    TEMP = "average temperature"
    HUM = "average humidity"
    TIME = "sun shining time"


@dataclass
class CityName:
    HE_YUAN = "河源"
    SHEN_ZHEN = "深圳"
    BEI_JING = "北京"
