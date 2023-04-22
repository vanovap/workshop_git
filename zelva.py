from turtle import forward, left, right, shape, exitonclick

for cislo_ctverce in range(3):
	for cislo_strany in range(4):
		forward(50)
		left(90)
	left(20)
exitonclick()


"""
Složitý postup:

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

left(20)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

left(20)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)

exitonclick() # jinak by se okýnko se želvou zavřelo hned po vykreslení
"""
