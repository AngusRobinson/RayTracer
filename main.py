import PIL.Image
from io import BytesIO
import IPython.display
import numpy as np
def draw(a, fmt='png'):
    a = np.uint8(a)
    f = BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)
    IPython.display.display(IPython.display.Image(data=f.getvalue()))


class Sphere:
    def __init__(self, pos, r, colour = [255,255,255]):
        self.pos = np.array(pos)
        self.r = r
        self.colour = np.array(colour)

    def intersect(self, v):
        a = 1
        b = -2*np.dot(v, self.pos)
        c = np.dot(self.pos, self.pos) - self.r*self.r
        disc = b**2 - 4*a*c
        if disc < 0:
            return -1
        else:
            return (-b - np.sqrt(disc)) / (2 * a)
            


def raytrace(v, shapes):
    distlist = [(x.intersect(v), x) for x in shapes]
    distlist = [(d, x) for d, x in distlist if d > 0]
    distlist.sort(key = lambda el: el[0])
    colour = distlist[0][1].colour if distlist else [0,0,0]
    return colour