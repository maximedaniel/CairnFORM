import math
import numpy as np
class Transition:

	LINEAR = 0
	EASE_IN_QUAD = 1
	EASE_OUT_QUAD = 2
	EASE_IN_OUT_QUAD = 3

	EASE_IN_CUBIC  = 4
	EASE_OUT_CUBIC  = 5
	EASE_IN_OUT_CUBIC  = 6

	EASE_IN_QUART  = 7
	EASE_OUT_QUART  = 8
	EASE_IN_OUT_QUART = 9

	EASE_IN_QUINT  = 10
	EASE_OUT_QUINT  =  11
	EASE_IN_OUT_QUINT  = 12

	EASE_IN_SINE  = 13
	EASE_OUT_SINE = 14
	EASE_IN_OUT_SINE = 15

	EASE_IN_EXPO  = 16
	EASE_OUT_EXPO  = 17
	EASE_IN_OUT_EXPO  = 18

	EASE_IN_CIRC  = 19
	EASE_OUT_CIRC  = 20
	EASE_IN_OUT_CIRC  = 21


	# simple linear tweening - no easing, no acceleration
	@classmethod
	def linearTween(cls, t, b, c, d):
		return c*t/d + b

			

	# quadratic easing in - accelerating from zero velocity

	@classmethod
	def easeInQuad(cls, t, b, c, d):
		t /= d
		return c*t*t + b

			

	# quadratic easing out - decelerating to zero velocity

	@classmethod
	def easeOutQuad(cls, t, b, c, d):
		t /= d
		return -c * t*(t-2) + b


			

	# quadratic easing in/out - acceleration until halfway, then deceleration

	@classmethod
	def easeInOutQuad(cls, t, b, c, d):
		t /= d/2
		if  t < 1 :
			return c/2*t*t + b
		t -= 1
		return -c/2 * (t*(t-2) - 1) + b



	# cubic easing in - accelerating from zero velocity

	@classmethod
	def easeInCubic(cls, t, b, c, d):
		t /= d
		return c*t*t*t + b


			

	# cubic easing out - decelerating to zero velocity

	@classmethod
	def easeOutCubic(cls, t, b, c, d):
		t /= d
		t -= 1
		return c*(t*t*t + 1) + b


			

	# cubic easing in/out - acceleration until halfway, then deceleration

	@classmethod
	def easeInOutCubic(cls, t, b, c, d):
		t /= d/2
		if t < 1:
		 return c/2*t*t*t + b
		t -= 2
		return c/2*(t*t*t + 2) + b

		

	# quartic easing in - accelerating from zero velocity

	@classmethod
	def easeInQuart(cls, t, b, c, d):
		t /= d
		return c*t*t*t*t + b


			

	# quartic easing out - decelerating to zero velocity

	@classmethod
	def easeOutQuart(cls, t, b, c, d):
		t /= d
		t -= 1
		return -c * (t*t*t*t - 1) + b


			

	# quartic easing in/out - acceleration until halfway, then deceleration

	@classmethod
	def easeInOutQuart(cls, t, b, c, d):
		t /= d/2
		if t < 1:
		 return c/2*t*t*t*t + b
		t -= 2
		return -c/2 * (t*t*t*t - 2) + b



	# quintic easing in - accelerating from zero velocity

	@classmethod
	def easeInQuint(cls, t, b, c, d):
		t /= d
		return c*t*t*t*t*t + b


			

	# quintic easing out - decelerating to zero velocity

	@classmethod
	def easeOutQuint(cls, t, b, c, d):
		t /= d
		t -= 1
		return c*(t*t*t*t*t + 1) + b


			

	# quintic easing in/out - acceleration until halfway, then deceleration

	@classmethod
	def easeInOutQuint(cls, t, b, c, d):
		t /= d/2
		if t < 1:
		 return c/2*t*t*t*t*t + b
		t -= 2
		return c/2*(t*t*t*t*t + 2) + b

			

	# sinusoidal easing in - accelerating from zero velocity

	@classmethod
	def easeInSine(cls, t, b, c, d):
		return -c * math.cos(t/d * (math.pi/2)) + c + b


			

	# sinusoidal easing out - decelerating to zero velocity

	@classmethod
	def easeOutSine(cls, t, b, c, d):
		return c * math.sin(t/d * (math.pi/2)) + b


			

	# sinusoidal easing in/out - accelerating until halfway, then decelerating

	@classmethod
	def easeInOutSine(cls, t, b, c, d):
		return -c/2 * (math.cos(math.pi*t/d) - 1) + b


			

	# exponential easing in - accelerating from zero velocity

	@classmethod
	def easeInExpo(cls, t, b, c, d):
		return c *  math.pow( 2, 10 * (t/d - 1) ) + b


			

	# exponential easing out - decelerating to zero velocity

	@classmethod
	def easeOutExpo(cls, t, b, c, d):
		return c * ( -math.pow( 2, -10 * t/d ) + 1 ) + b


			

	# exponential easing in/out - accelerating until halfway, then decelerating

	@classmethod
	def easeInOutExpo(cls, t, b, c, d):
		t /= d/2
		if t < 1: 
			return c/2 * math.pow( 2, 10 * (t - 1) ) + b
		t -= 1
		return c/2 * ( -math.pow( 2, -10 * t) + 2 ) + b

			

	# circular easing in - accelerating from zero velocity

	@classmethod
	def easeInCirc(cls, t, b, c, d):
		t /= d
		return -c * (math.sqrt(1 - t*t) - 1) + b


			

	# circular easing out - decelerating to zero velocity

	@classmethod
	def easeOutCirc(cls, t, b, c, d):
		t /= d
		t -= 1
		return c * math.sqrt(1 - t*t) + b


			

	# circular easing in/out - acceleration until halfway, then deceleration

	@classmethod
	def easeInOutCirc(cls, t, b, c, d):
		t /= d/2
		if t < 1:
		 return -c/2 * (math.sqrt(1 - t*t) - 1) + b
		t -= 2
		return c/2 * (math.sqrt(1 - t*t) + 1) + b

	@classmethod
	def transition(cls, mode, t, b, c, d):
		#sign = np.sign(c)
		#print(sign)
		if mode == cls.LINEAR:
			return cls.linearTween(t,b,c,d)

		if mode == cls.EASE_IN_QUAD:
			return cls.easeInQuad(t,b,c,d)

		if mode == cls.EASE_OUT_QUAD:
			return cls.easeOutQuad(t,b,c,d)

		if mode == cls.EASE_IN_OUT_QUAD:
			return cls.easeInOutQuad(t,b,c,d)

		if mode == cls.EASE_IN_CUBIC:
			return cls.easeInCubic(t,b,c,d)

		if mode == cls.EASE_OUT_CUBIC:
			return cls.easeOutCubic(t,b,c,d)

		if mode == cls.EASE_IN_OUT_CUBIC:
			return cls.easeInOutCubic(t,b,c,d)

		if mode == cls.EASE_IN_QUART:
			return cls.easeInQuart(t,b,c,d)

		if mode == cls.EASE_OUT_QUART:
			return cls.easeOutQuart(t,b,c,d)

		if mode == cls.EASE_IN_OUT_QUART:
			return cls.easeInOutQuart(t,b,c,d)

		if mode == cls.EASE_IN_QUINT:
			return cls.easeInQuint(t,b,c,d)

		if mode == cls.EASE_OUT_QUINT:
			return cls.easeOutQuint(t,b,c,d)

		if mode == cls.EASE_IN_OUT_QUINT:
			return cls.easeInOutQuint(t,b,c,d)

		if mode == cls.EASE_IN_SINE:
			return cls.easeInSine(t,b,c,d)

		if mode == cls.EASE_OUT_SINE:
			return cls.easeOutSine(t,b,c,d)

		if mode == cls.EASE_IN_OUT_SINE:
			return cls.easeInOutSine(t,b,c,d)

		if mode == cls.EASE_IN_EXPO:
			return cls.easeInExpo(t,b,c,d)

		if mode == cls.EASE_OUT_EXPO:
			return cls.easeOutExpo(t,b,c,d)

		if mode == cls.EASE_IN_OUT_EXPO:
			return cls.easeInOutExpo(t,b,c,d)

		if mode == cls.EASE_IN_CIRC:
			return cls.easeInCirc(t,b,c,d)

		if mode == cls.EASE_OUT_CIRC:
			return cls.easeOutCirc(t,b,c,d)

		if mode == cls.EASE_IN_OUT_CIRC:
			return cls.easeInOutCirc(t,b,c,d)
