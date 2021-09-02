import pandas as pd
import math


def percentile(values: list, percent=0.5, sort=False):
    if not values or 0.0 > percent > 1.0:
        return None
    values = sorted(values) if not sort else values
    position = (len(values) - 1) * percent
    floor = math.floor(position)
    ceil = math.ceil(position)
    if floor == ceil:  # Если индекс целый
        return values[int(position)]
    floor_part = values[int(floor)] * (ceil - position)
    ceil_part = values[int(ceil)] * (position - floor)
    return floor_part + ceil_part


if __name__ == '__main__':
    men = [140, 145, 160, 190, 155, 165, 150, 190, 195, 138, 160, 155, 153, 145, 170, 175, 175, 170, 180,
           135, 170, 157, 130, 185, 190, 155, 170, 155, 215, 150, 145, 155, 155, 150, 155, 150, 180, 160,
           135, 160, 130, 155, 150, 148, 155, 150, 140, 180, 190, 145, 150, 164, 140, 142, 136, 123, 155]
    women = [140, 120, 130, 138, 121, 125, 116, 145, 150, 112, 125, 130, 120, 130, 131, 120, 118, 125, 135,
             125, 118, 122, 115, 102, 115, 150, 110, 116, 108, 95, 125, 133, 110, 150, 108]
    people = men + women
    ndarray_p = pd.DataFrame(people)
    print(f'pandas 75 percentile: {ndarray_p.describe().values[6][0]},'
          f'\nmy 75 percentile: {percentile(people, 0.75)}')
