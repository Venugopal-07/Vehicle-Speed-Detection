import math
from config import PIXEL_TO_METER, FPS

def calculate_speed(prev_point, curr_point):
    distance_pixels = math.dist(prev_point, curr_point)
    distance_meters = distance_pixels * PIXEL_TO_METER
    speed_mps = distance_meters * FPS
    speed_kmph = speed_mps * 3.6
    return int(speed_kmph)
