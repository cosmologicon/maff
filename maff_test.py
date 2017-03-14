from __future__ import division
import unittest, maff, math

# Available as math.isclose in Python 3.2+
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
	return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class MaffTest(unittest.TestCase):
	def assertClose(self, a, b, rel_tol=1e-09, abs_tol=0.0):
		self.assertTrue(isclose(a, b, rel_tol, abs_tol))

	def test_phi(self):
		self.assertGreater(math.Phi, 0)
		self.assertClose(math.phi, math.Phi + 1)
		self.assertClose(math.phi, 1 / math.Phi)

	def test_sign(self):
		self.assertEqual(math.sign(-0.3), -1)
		self.assertEqual(math.sign(0.0), 0)
		self.assertEqual(math.sign(-0.0), 0)
		self.assertEqual(math.sign(0.3), 1)

	def test_clamp(self):
		self.assertEqual(math.clamp(3, 4, 5), 4)
		self.assertEqual(math.clamp(4.5, 4, 5), 4.5)
		self.assertEqual(math.clamp(6, 4, 5), 5)

	def test_mix(self):
		self.assertClose(math.mix(20, 30, 0.3), 23)
		self.assertClose(math.mix(20, 30, -0.3), 17)

	def test_step(self):
		self.assertEqual(math.step(0, 1), 1)
		self.assertEqual(math.step(0, -1), 0)

	def test_smoothstep(self):
		self.assertClose(math.smoothstep(3, 4, 2), 0)
		self.assertClose(math.smoothstep(3, 4, 3.25), 0.15625)
		self.assertClose(math.smoothstep(3, 4, 5.5), 1)

	def test_length(self):
		self.assertClose(math.length([2.5]), 2.5)
		self.assertClose(math.length([0, 0, 0]), 0)
		self.assertClose(math.length([1, 1, 1, 1]), 2)

	def test_distance(self):
		self.assertClose(math.distance([1, 2, 3], [1, 2, 3]), 0)
		self.assertClose(math.distance([2], [-3]), 5)
		self.assertClose(math.distance([2, -2], [5, 2]), 5)

	def test_dot(self):
		self.assertClose(math.dot([2], [3]), 6)
		self.assertClose(math.dot([1, 2, 3], [2, 1, 0]), 4)

	def test_norm(self):
		vs = (1,), (0, 1, 2), (-3, 3, -3, 3)
		for v in vs:
			for a in [0, 1, 10]:
				vnorm = math.norm(v, a)
				self.assertClose(math.length(vnorm), a)
				self.assertClose(math.dot(v, vnorm), a * math.length(v))

	def test_ease(self):
		self.assertClose(math.ease(-0.5), 0)
		self.assertClose(math.ease(0), 0)
		self.assertClose(math.ease(0.25), 0.15625)
		self.assertClose(math.ease(1), 1)
		self.assertClose(math.ease(100), 1)

	def test_fade(self):
		self.assertClose(math.fade(5, 10, 0), 0)
		self.assertClose(math.fade(5, 10, 4), 0)
		self.assertClose(math.fade(11, 10, 4), 0.25)
		self.assertClose(math.fade(14, 10, 4), 1)

	def test_smoothfade(self):
		self.assertClose(math.smoothfade(5, 10, 4), 0)
		self.assertClose(math.smoothfade(11, 10, 4), 0.15625)
		self.assertClose(math.smoothfade(14, 10, 4), 1)

	def test_dfade(self):
		self.assertClose(math.dfade(5, 10, 20, 0), 0)
		self.assertClose(math.dfade(5, 10, 20, 4), 0)
		self.assertClose(math.dfade(12, 10, 20, 4), 0.5)
		self.assertClose(math.dfade(14, 10, 20, 4), 1)
		self.assertClose(math.dfade(18, 10, 20, 4), 0.5)
		self.assertClose(math.dfade(20, 10, 20, 4), 0)
		self.assertClose(math.dfade(200, 10, 20, 4), 0)
		self.assertClose(math.dfade(14, 10, 20, 10), 0.4)
		self.assertClose(math.dfade(16, 10, 20, 10), 0.4)

	def test_dsmoothfade(self):
		self.assertClose(math.dsmoothfade(5, 10, 20, 0), 0)
		self.assertClose(math.dsmoothfade(11, 10, 20, 4), 0.15625)
		self.assertClose(math.dsmoothfade(19, 10, 20, 4), 0.15625)

	def test_approach(self):
		self.assertClose(math.approach(10, 20, 1), 11)
		self.assertClose(math.approach(10, -20, 1), 9)
		self.assertClose(math.approach(10, 20, 100), 20)
		self.assertClose(math.approach(10, -20, 100), -20)

	def test_approach_vector(self):
		vs = (0, 0, 0), (1, 2, 3), (1, -1, 1)
		for v0 in vs:
			for v1 in vs:
				for d in (0, 0.01, 1, 100):
					v = math.approach(v0, v1, d)
					# v0, v, v1 collinear by the triangle inequality
					# with v in between v0 and v1
					self.assertClose(
						math.distance(v0, v) + math.distance(v, v1),
						math.distance(v0, v1))
					self.assertClose(
						math.distance(v0, v),
						min(math.distance(v0, v1), d))

	def test_CS(self):
		cases = (0, 1, 1, 0), (1.5, 0, 0, 0), (math.tau / 8, math.sqrt(2), 1, 1)
		for theta, r, x, y in cases:
			a, b = math.CS(theta, r)
			self.assertClose(a, x)
			self.assertClose(b, y)

	def test_CSround(self):
		for ntheta in (2, 4, 7, 13):
			for r in (0, 1, 10):
				for jtheta0 in (0, 0.1, 0.8):
					xys = math.CSround(ntheta, r, jtheta0)
					for xy in xys:
						self.assertClose(math.length(xy), r)
					d = 2 * r * math.sin(math.tau / ntheta / 2)
					for j in range(ntheta):
						k = (j + 1) % ntheta
						self.assertClose(math.distance(xys[j], xys[k]), d)

if __name__ == '__main__':
    unittest.main()

