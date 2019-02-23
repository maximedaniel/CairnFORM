import math
import scipy.integrate as integrate
import numpy as np
import time
#import matplotlib.pyplot as plt

LINEAR = 0
EXPONENTIAL = 1
LOGARITHMIC = 2

def getRPM(duration, steps):
	return (steps*1.8 / 360)* (60/duration)

def linear_speed(x, steps):
	return steps * x

def exponential_speed(x, steps):
	exp_min = math.log(0.1)
	exp_max = math.log(4.1)
	exp_range = exp_max - exp_min
	coeff = steps/(math.exp(exp_max)-math.exp(exp_min))
	return coeff *  ((math.exp(x * exp_range + exp_min)) - math.exp(exp_min))

def logarithmic_speed(x, steps):
	log_min = 0.1
	log_max = 4.1
	log_range = log_max - log_min
	coeff = steps/(math.log(log_max)-math.log(log_min))
	return coeff *  ((math.log(x * log_range + log_min)) - math.log(log_min))


def getTrajectory(time_duration=2.0, steps=200, accuracy=0.1, mode=LINEAR):
	steps_by_iteration  = []
	rpm_by_iteration = []

	if mode == LINEAR:
		for time_delta in np.arange(0.0, time_duration, accuracy):
			steps_current = linear_speed(time_delta/time_duration, steps)
			steps_next = linear_speed((time_delta + accuracy)/time_duration, steps)
			steps_diff = steps_next - steps_current
			steps_by_iteration.append(round(steps_diff))
			rpm = getRPM(accuracy, steps_diff)
			rpm_by_iteration.append(round(rpm))

	if mode == EXPONENTIAL:
		for time_delta in np.arange(0.0, time_duration, accuracy):
			steps_current = exponential_speed(time_delta/time_duration, steps)
			steps_next = exponential_speed((time_delta + accuracy)/time_duration, steps)
			steps_diff = steps_next - steps_current
			steps_by_iteration.append(round(steps_diff))
			rpm = getRPM(accuracy, steps_diff)
			rpm_by_iteration.append(round(rpm))


	if mode == LOGARITHMIC:
		for time_delta in np.arange(0.0, time_duration, accuracy):
			steps_current = logarithmic_speed(time_delta/time_duration, steps)
			steps_next = logarithmic_speed((time_delta + accuracy)/time_duration, steps)
			steps_diff = steps_next - steps_current
			steps_by_iteration.append(round(steps_diff))
			rpm = getRPM(accuracy, steps_diff)
			rpm_by_iteration.append(round(rpm))
	return rpm_by_iteration, steps_by_iteration


def move(time_duration=2.0, steps=200, accuracy=0.1, mode=LINEAR):
	rpms, steps = getTrajectory(time_duration, steps, accuracy, mode)
	for rpm, step in zip(rpms, steps):
		print('rpm : ', rpm, ' steps : ', step)

#ln_init = math.log(0.1)
#print("ln(0.1)", ln_init)
#for x in np.arange(0.1,3.0,0.1):
#	print("x+ln_init", x+ln_init)
#	print("exp(x+ln_init) ", math.exp(x+ln_init))
#print("### LINEAR SPEED ###")
#x, y = move(2.0, 200, 0.1, mode=LINEAR)
#plt.plot(x,y, 'ro')
#plt.show()

time_duration = 5.0
steps = 200
accuracy = 1.0

#x = np.arange(0.0, time_duration+accuracy, accuracy)
print("LINEAR")
move(time_duration, steps, accuracy, mode=LINEAR)
print("EXPONENTIAL")
move(time_duration, steps, accuracy, mode=EXPONENTIAL)
print("LOGARITHMIC")
move(time_duration, steps, accuracy, mode=LOGARITHMIC)
#plt.plot(x, y0, 'r--', x, y1, 'g--', x, y2, 'b--')
#plt.show()