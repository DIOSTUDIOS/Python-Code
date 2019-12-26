from pyautocad import Autocad
from pyautocad import APoint


acad = Autocad(create_if_not_exists = True)
acad.prompt('Hello, CAD from python')

print(acad.doc.name)

p1 = APoint(0, 0)
p2 = APoint(1000, 1000)

for i in range(5):
	acad.model.AddLine(p1, p2)
	acad.model.AddCircle(p1, 100)

	p1.y += 100