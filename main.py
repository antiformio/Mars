from mars.mars_robot import Robot


if __name__ == "__main__":
    top_right = input("Enter plateau top-right: ")
    current_pos = input("Enter current position and orientation: ")
    orders = input("Enter robot orders: ")
    robot = Robot()
    print(robot.compute_orders(
        {
            "map_top_right": top_right,
            "current_pos": current_pos,
            "orders": orders
        }
    ))
