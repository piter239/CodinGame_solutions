import sys
import math

[[int(j) for j in input().split()] for i in range(int(input()))]

# Error vars
prev_error = 0
sum_error = 0

# PID controller constants
KP = 49
KI = 0  # 1
KD = 0  # 49
TARGET_SPEED = -39.0

while True:
    X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]

    # PID controller
    error = TARGET_SPEED - VS
    sum_error += error
    prev_error = error
    cmd = KP * error + KI * sum_error + KD * (error - prev_error)

    print(0, int(min(max(cmd, 0), 4)))
