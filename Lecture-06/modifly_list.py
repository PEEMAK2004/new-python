# Modifying lists
shapes = ["circle", "square", "triangle", "rectangle", "hexagon"]
shapes [1] = "ellipse"
shapes [3] = "pentagon"
shapes [len(shapes) - 1] = "octagon"
print (f"Modified shapes: {shapes}")