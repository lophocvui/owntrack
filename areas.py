from collections import namedtuple
from pprint import pprint as pp
import sys
 
Pt = namedtuple('Pt', 'x, y')               # Point
Edge = namedtuple('Edge', 'a, b')           # Polygon edge from a to b
Poly = namedtuple('Poly', 'name, edges')    # Polygon
 
_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min

def rayintersectseg(p, edge):
    ''' takes a point p=Pt() and an edge of two endpoints a,b=Pt() of a line segment returns boolean
    '''
    a,b = edge
    if a.y > b.y:
        a,b = b,a
    if p.y == a.y or p.y == b.y:
        p = Pt(p.x, p.y + _eps)
 
    intersect = False
 
    if (p.y > b.y or p.y < a.y) or (
        p.x > max(a.x, b.x)):
        return False
 
    if p.x < min(a.x, b.x):
        intersect = True
    else:
        if abs(a.x - b.x) > _tiny:
            m_red = (b.y - a.y) / float(b.x - a.x)
        else:
            m_red = _huge
        if abs(a.x - p.x) > _tiny:
            m_blue = (p.y - a.y) / float(p.x - a.x)
        else:
            m_blue = _huge
        intersect = m_blue >= m_red
    return intersect
 
def _odd(x): return x%2 == 1
 
def ispointinside(p, poly):
    ln = len(poly)
    return _odd(sum(rayintersectseg(p, edge)
                    for edge in poly.edges ))


ptit = Poly(name='ptit', edges=(
		Edge(a=Pt(x=105.788045, y=20.980871), b=Pt(x=105.787134, y=20.980113)),
		Edge(a=Pt(x=105.787134, y=20.980113), b=Pt(x=105.786904, y=20.980399)),
		Edge(a=Pt(x=105.786904, y=20.980399), b=Pt(x=105.786735, y=20.980684)),
		Edge(a=Pt(x=105.786735, y=20.980684), b=Pt(x=105.786816, y=20.980864)),
		Edge(a=Pt(x=105.786816, y=20.980864), b=Pt(x=105.786714, y=20.981135)),
		Edge(a=Pt(x=105.786714, y=20.981135), b=Pt(x=105.786478, y=20.981420)),
		Edge(a=Pt(x=105.786478, y=20.981420), b=Pt(x=105.786682, y=20.981661)),
		Edge(a=Pt(x=105.786682, y=20.981661), b=Pt(x=105.787068, y=20.981666)),
		Edge(a=Pt(x=105.787068, y=20.981666), b=Pt(x=105.787492, y=20.981651)),
		Edge(a=Pt(x=105.787492, y=20.981651), b=Pt(x=105.788045, y=20.980871))
		
	))

aosen = Poly(name='aosen', edges=(
		Edge(a=Pt(x=20.980738, y=105.788234), b=Pt(x=20.981735, y=105.787499)),
		Edge(a=Pt(x=20.981735, y=105.787499), b=Pt(x=20.982702, y=105.786657)),
		Edge(a=Pt(x=20.982702, y=105.786657), b=Pt(x=20.983233, y=105.786856)),
		Edge(a=Pt(x=20.983233, y=105.786856), b=Pt(x=20.983466, y=105.787533)),
		Edge(a=Pt(x=20.983466, y=105.787533), b=Pt(x=20.983067, y=105.788222)),
		Edge(a=Pt(x=20.983067, y=105.788222), b=Pt(x=20.982584, y=105.787795)),
		Edge(a=Pt(x=20.982584, y=105.787795), b=Pt(x=20.981411, y=105.789007)),
		Edge(a=Pt(x=20.981411, y=105.789007), b=Pt(x=20.980738, y=105.788234))
	))

home = Poly(name='home', edges=(
		Edge(a=Pt(x=20.972787, y=105.784327), b=Pt(x=20.972917, y=105.784101)),
		Edge(a=Pt(x=20.972917, y=105.784101), b=Pt(x=20.973019, y=105.784171)),
		Edge(a=Pt(x=20.973019, y=105.784171), b=Pt(x=20.973102, y=105.784174)),
		Edge(a=Pt(x=20.973102, y=105.784174), b=Pt(x=20.973095, y=105.784381)),
		Edge(a=Pt(x=20.973095, y=105.784381), b=Pt(x=20.972949, y=105.784510)),
		Edge(a=Pt(x=20.972949, y=105.784510), b=Pt(x=20.972787, y=105.784327))
	))
