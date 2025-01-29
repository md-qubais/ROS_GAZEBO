import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Global variable to store the minimum distance to an obstacle
min_distance = float('inf')

# Callback function for the LaserScan topic
def scan_callback(scan_data):
    global min_distance
    # Get the minimum distance from the laser scan data
    min_distance = min(scan_data.ranges)

def reactive_control():
    global min_distance

    # Initialize the ROS node
    rospy.init_node('reactive_control', anonymous=True)

    # Create a publisher for the /cmd_vel topic
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Subscribe to the /scan topic to get obstacle distances
    rospy.Subscriber('/scan', LaserScan, scan_callback)

    # Define the rate for the loop
    rate = rospy.Rate(10)  # 10 Hz

    # Define movement commands
    move_cmd = Twist()
    move_cmd.linear.x = 0.2  # Default forward velocity
    move_cmd.angular.z = 0.0

    # Set the obstacle avoidance threshold distance
    obstacle_threshold = 0.5  # Meters

    rospy.loginfo("Reactive control: Robot will stop if an obstacle is closer than 0.5 meters")

    try:
        while not rospy.is_shutdown():
            if min_distance < obstacle_threshold:
                # Stop the robot if an obstacle is too close
                rospy.logwarn(f"Obstacle detected! Stopping. Distance: {min_distance:.2f} m")
                move_cmd.linear.x = 0.0
                move_cmd.angular.z = 0.0
            else:
                # Move forward if the path is clear
                rospy.loginfo(f"Path clear. Distance: {min_distance:.2f} m")
                move_cmd.linear.x = 0.2
                move_cmd.angular.z = 0.0

            # Publish the movement command
            cmd_vel_pub.publish(move_cmd)

            # Sleep to maintain the loop rate
            rate.sleep()

    except rospy.ROSInterruptException:
        rospy.loginfo("Shutting down reactive control.")

if __name__ == "__main__":
    reactive_control()
