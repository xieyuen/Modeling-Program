from dataclasses import dataclass


@dataclass
class Title:
    CITY_INDEX = "城市编号"
    TRAFFIC_FLOW = "汽车流量"
    PM_CONCENTRATION = "PM2.5浓度"
    AVERAGE_TEMPERTURE = "平均气温"
    HUMIDITY = "空气湿度"
    WIND_SPEED = "风速"
    X = [TRAFFIC_FLOW, AVERAGE_TEMPERTURE, HUMIDITY, WIND_SPEED]

@dataclass
class Labels:
    TRAFFIC_FLOW = "traffic flow"
    PM_CONCENTRATION = "PM2.5 concentration"
    AVERAGE_TEMPERTURE = "average temperture"
    HUMIDITY = "humidity"
    WIND_SPEED = "wind speed"