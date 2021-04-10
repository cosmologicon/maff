# maff
Python convenience functions that I wish were in the math module, as well as some that I agree
probably shouldn't be.

## Quick usage

	import maff
	print(maff.ease(0.1))

The first time you import `maff`, it will also pollute the `math` module with its own functions, so
you can call them via `math` on any module that imports `math`.

	import maff, math
	print(math.ease(0.1))

## To install

Download `maff.py` and put it in your source directory. To install from command line:

	curl https://raw.githubusercontent.com/cosmologicon/maff/master/maff.py > my-source-directory/maff.py

## Usage notes

As the name hopefully implies, this is a bit of a frivolous module and not recommended for serious
use. I plan to use it for game jams.

Any function that accepts a "vector" expects some iterable, typically a list, tuple, `pygame.math.Vector2`,
etc. Try your vector type and see if it works. If not, file an issue, and I should be able to support it.

## Constants

`maff.tau`: the circle constant equal to 2pi.

`maff.phi` and `maff.Phi`: golden ratio and reciprocal golden ratio.

## Functions taken from GLSL

`maff.sign(x)`: sign of x.

`maff.clamp(x, a, b)`: clamps x to range [a, b].

`maff.mix(x, y, a)`: mix the values x and y with mixing factor a. The value of a is clamped to the
range [0, 1]. Also works for vector-valued x and y.

`maff.imix(x, y, a)`: like `mix`, but converts the value to the nearest integer.

`maff.step(edge, x)`: Heaviside step function of x with given edge.

`maff.smoothstep(edge0, edge1, x)`: step function with Hermite interpolation between edge0 and
edge1.

`maff.length(v)`: length of vector v. Can be any iterable.

`maff.distance(v0, v1)`: distance between vectors v0 and v1

`maff.dot(v0, v1)`: dot product

`maff.norm(v)` or `maff.normalize(v)`: normalize vector to length 1. Does not fail on zero vector.

`maff.norm(v, a)` or `maff.normalize(v, a)`: normalize vector to length a.

## Fade functions

`maff.ease(x)`: Hermite interpolation of x in range (0, 1). Equal to `maff.smoothstep(0, 1, x)`.

`maff.fade(x, x0, dx)`: fade from 0 to 1 starting at x = x0 for a fade interval of dx.

`maff.smoothfade(x, x0, dx)`: like `fade` with Hermite interpolation.

`maff.dfade(x, x0, x1, dx)`: double-fade from 0 to 1 starting at x0, then back from 1 to 0 ending at
x1, with a fade interval of dx on both ends.

`maff.dsmoothfade(x, x0, x1, dx)`: double-fade with Hermite interpolation.

`maff.fadebetween(x, x0, y0, x1, y1)`: returns the y-value such that (x, y) is linearly interpolated
between the points (x0, y0) and (x1, y1). Works for vector-valued y's.

`maff.smoothfadebetween(x, x0, y0, x1, y1)`: returns the y-value such that (x, y) is smoothly
interpolated between (x0, y0) and (x1, y1). Works for vector-valued y's.

`maff.cycle(a)`: sinusoidal cycle between 0 and 1 and back to 0 with period 1. Can be used with
`maff.mix` to cycle between two values: `maff.mix(x, y, maff.cycle(a))`.

## Approach functions

`maff.approach(x, y, dx)`: increase or decrease x by amount dx in the direction of y. If the
distance between x and y is less than dx, then return y instead. x and y can be vectors.

`maff.softapproach(x, y, dlogx)`: increase or decrease x by an amount determined by dlogx. dlogx is
a unitless parameter between 0 and infinity. If dlogx is 0, then x will be returned. For
sufficiently large dlogx, then y will be returned. Calling this repeatedly and updating the value of
x will give exponential decay toward y, with a timescale factor of 1 / dlogx.

`maff.softapproach(x, y, dlogx, dxmax=inf, dymin=0.1)`: After calculating the approach distance dx,
it's compared with dxmax. If it exceeds dxmax then it's capped at dxmax. If the resulting is a
distance less than dymin away from y, then y is returned. This is because with exponential decay
it's impossible to ever exactly reach y.

## Trigonometry and Rotation

`maff.CS(theta)`: 2-tuple of cos(theta), sin(theta).

`maff.CS(theta, r)`: 2-tuple of r cos(theta), r sin(theta).

`maff.CSround(ntheta)`: Produces ntheta 2-tuples of cos(theta), sin(theta) distributed around the
unit circle.

`maff.CSround(ntheta, r=1, jtheta0=0)`: specify radius and offset.

`maff.R(theta, (x, y))`: 2-tuple of the vector <x, y> rotated counterclockwise by the angle `theta`.

`maff.R(theta)`: returns a function that takes a single vector argument, and return that vector
rotated counterclockwise by the angle `theta`.

## Pseudorandom values

`maff.fuzz(*args)`: produce a number in the range [0, 1) that is deterministically calculated from
any number of numerical arguments. The result can be treated as a low-quality pseudorandom number,
using the arguments as a seed. Differences in the arguments smaller than 1e-6 may result in
correlations. That is, `maff.fuzz(x)` may be close or equal to `maff.fuzz(x + 1e-7)`.

`maff.fuzzrange(a, b, *args)`: produce a number in the range [a, b). Equivalent to:
`maff.mix(a, b, maff.fuzz(*args))`.

## Thanks

Special thanks to [Daniel Pope (lordmauve)](https://github.com/lordmauve) for handling the packaging
and licensing!
