finish_matrix = (
    (2,3,2),
    (3,0,3),
    (2,3,2)
)

def optimal_route(figure: dict, finish: dict, count = 0) -> int:

    direction_x = finish['x'] - figure['x']
    direction_y = finish['y'] - figure['y']

    if (direction_x > 1 or direction_y > 1):
        dx = -1 if direction_x < 0 else 1
        dy = -1 if direction_y < 0 else 1
        figure['x'] += dx
        figure['y'] += dy

        if abs(direction_x) > abs(direction_y):
            figure['x'] += dx
        else:
            figure['y'] += dy

        count += 1
        return optimal_route(figure, finish, count)
    
    return count + finish_matrix[direction_x + 1][direction_y + 1]

if __name__ == "__main__":
    print('minimal steps count: ', optimal_route(
        {'x':8, 'y':1},
        {'x':5, 'y':6}
    ))