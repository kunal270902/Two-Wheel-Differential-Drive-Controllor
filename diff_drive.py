linear_x=0.5
angular_z=0
VrplusVl = 0
VrminusVl = 0
right_wheel_vel = 0
left_wheel_vel = 0
wheel_seperation = x
wheel_circumference = x
motor_rpm = x #max rpm of the motor
max_pwm_val = x
min_pwm_val = x
max_speed = (wheel_circumference*motor_rpm)/60  #m/sec
left_wheel_vel_rpm = 0
right_wheel_vel_rpm = 0
dir1 = 0
dir2 = 0

# Calculate speeds and directions

#sum of right wheel velocity and left wheel velocity --> since linear velocity affects both the wheels equally
VrplusVl = 2 * linear_x

# diffrence between right wheel velocity and left wheel velocity ---> these is how we get anguler velocity of the robot
VrminusVl = -angular_z * wheel_seperation

#right wheel and left wheel velocity in m/sec (along the ground)
right_wheel_vel = (VrplusVl + VrminusVl)/2
left_wheel_vel = VrplusVl -right_wheel_vel

# wheel velocity in rps
right_wheel_vel_rps = right_wheel_vel/wheel_circumference
left_wheel_vel_rps = left_wheel_vel/wheel_circumference

#convert velocity from m/sec to rpm 

right_wheel_vel_rpm = right_wheel_vel_rps*60
left_wheel_vel_rpm = left_wheel_vel_rps*60
speed1 = abs(int(left_wheel_vel_rpm))
speed2 = abs(int(right_wheel_vel_rpm))
print(speed1)   
print(speed2)
