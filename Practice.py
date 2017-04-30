colors = ["blue", "red", "green"]
textures = ["smooth", "bumpy"]
shapes = ["circle", "square", "triangle"]

p = []

for color in colors:
    for texture in textures:
        for shape in shapes:
            p.append("%s %s %s" % (color, texture, shape))

print len(p)
print p