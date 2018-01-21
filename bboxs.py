# soubor generuje selecty pro spatialite databazi s nahodnymi bounding boxy odpovidajicimi celemu rozsahu dat
import csv, random

XMIN = -24
XMAX = 60

YMIN = 34
YMAX = 71

f = open('bboxs.csv', 'w')
for i in range(1, 51):
    xmin_gen = random.randint(XMIN, XMAX)
    xmax_gen = random.randint(XMIN, XMAX)

    ymin_gen = random.randint(YMIN, YMAX)
    ymax_gen = random.randint(YMIN, YMAX)

    # zkontroluju jestli xmax neni mensi nez xmin
    while xmax_gen < xmin_gen:
        xmax_gen = random.randint(XMIN, XMAX)

    while ymax_gen < ymin_gen:
        ymax_gen = random.randint(YMIN, YMAX)

    f.write(str(i) + '\t' + 'SELECT * FROM roads WHERE Intersects(BuildMbr(' + str(xmin_gen) + ', ' + str(ymin_gen) + ', ' + str(
        xmax_gen) + ', ' + str(ymax_gen) + '), geom);\n')

f.close()
