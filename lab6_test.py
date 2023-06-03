from lab6.komiwojazer import * 

# Dane punktów
points = [
    (29, -82),
    (-11, -86),
    (35, 36),
    (96, -15),
    (-3, -71),
    (-49, 97),
    (44, 13),
    (6, -22),
    (38, -82),
    (34, 18),
    (-7, 57),
    (-5, -54),
    (-49, 13),
    (60, 94),
    (-44, -16),
    (-66, -29),
    (93, 35),
    (-32, 41),
    (67, -15),
    (37, -9),
    (49, -3),
    (79, 49),
    (-37, 26),
    (60, -75),
    (-28, 41),
    (0, -22),
    (-51, -9),
    (-68, -97),
    (-40, 3),
    (-15, 28),
    (61, 15),
    (70, -47),
    (-70, -40),
    (-70, 72),
    (51, 1),
    (-25, 56),
    (-52, 23),
    (15, -69),
    (33, 51),
    (40, -30),
    (84, 80),
    (-4, 26),
    (-22, -82),
    (-47, -54),
    (3, -25),
    (-21, 29),
    (-3, -70),
    (-87, -73),
    (-85, 69),
    (-9, 65),
    (-36, -79),
    (44, -29),
    (-63, -74),
    (-46, -4),
    (-51, 22),
    (100, -38),
    (87, -50),
    (-97, -43),
    (-56, 32),
    (-72, 95),
    (89, 37),
    (38, -52),
    (73, -16),
    (51, -51),
    (-47, -17),
    (74, 47),
    (-85, 81),
    (-9, 4),
    (-25, -59),
    (-72, 53),
    (88, 85),
    (-60, 24),
    (86, 71),
    (35, 85),
    (58, -83),
    (75, -70),
    (-84, -41),
    (58, 36),
    (42, -66),
    (35, -55),
    (-72, 51),
    (-28, 76),
    (14, -37),
    (-42, -60),
    (-97, 50),
    (-99, 93),
    (42, 83),
    (-11, 74),
    (12, 43),
    (84, 71),
    (98, -36),
    (-30, 22),
    (51, -2),
    (75, -16),
    (40, -99),
    (86, -78),
    (82, -23),
    (55, 27),
    (97, 25),
    (-72, 24),
    (82, 17),
    (64, 74),
    (9, 81),
    (-62, -68),
    (38, -80),
    (-7, -97),
    (-89, 62),
    (-61, -89),
    (-78, -29),
    (69, -64),
    (57, 38),
    (89, -53),
    (-33, 44),
    (-15, 88),
    (19, -21),
    (68, 19),
    (68, 93),
    (96, -11),
    (13, 98),
    (-63, 22),
    (-6, -83),
    (-20, 89),
    (-62, 74),
    (-97, 81),
    (57, 14),
    (92, 94),
    (-70, -94),
    (41, -49),
    (-59, 4),
    (30, 28),
    (-46, -49),
    (-65, -89),
    (-16, -40),
    (-73, -53),
    (-86, -26),
    (-37, -2),
    (25, 63),
    (-17, -19),
    (2, -9),
    (56, 73),
    (74, 7),
    (14, 2),
    (-25, -28),
    (38, -85),
    (34, 61),
    (29, -73),
    (47, -92),
    (29, -14),
    (26, -87),
    (18, -10)
]

# Uruchomienie algorytmu symulowanego wyżarzania
best_path, best_distance = simulated_annealing(points)

# Wyświetlenie wyników
print("Najkrótsza ścieżka:", best_path)
print("Długość ścieżki:", best_distance)

# Wyrysowanie najkrótszej ścieżki na wykresie
plot_path(points, best_path)