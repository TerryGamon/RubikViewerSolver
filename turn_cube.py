import pandas as pd
import numpy as np

# 0 hinten
# 1 links
# 2 vorne
# 3 rechts
# 4 oben
# 5 unten

def cube_ganz_rechts(xcube):
    #dreht den ganzen würfel nach rechts, front wird rechts, links wird front, etc.
    t_cube = xcube.copy()
    t_side = t_cube[0].copy()
    t_cube[0] = t_cube[3].copy()
    t_cube[3] = t_cube[2].copy()
    t_cube[2] = t_cube[1].copy()
    t_cube[1] = t_side

    t_cube[4] = np.rot90(t_cube[4],-1)
    t_cube[5] = np.rot90(t_cube[5])
    return t_cube

def cube_ganz_links(xcube):
    #dreht den ganzen würfel nach links, front wird links, rechts wird front, etc.
    #das ist das gleiche wie 3x nach rechts drehen
    t_cube = xcube.copy()
    for x in range(3):
        t_cube = cube_ganz_rechts(t_cube)
    return(t_cube)

def cube_ganz_runter(xcube):
    t_cube = xcube.copy()
    t_side = t_cube[0].copy()
    t_cube[0] = t_cube[5].copy()
    t_cube[0] = np.rot90(t_cube[0])
    t_cube[0] = np.rot90(t_cube[0])
    t_cube[5] = t_cube[2].copy()
    t_cube[2] = t_cube[4].copy()
    
    t_cube[4] = np.rot90(t_side)
    t_cube[4] = np.rot90(t_cube[4])

    t_cube[1] = np.rot90(t_cube[1]) # im uzs
    t_cube[3] = np.rot90(t_cube[3],-1) # gg uzs
    return t_cube

def cube_ganz_rauf(xcube):
    t_cube = xcube.copy()
    for x in range(3):
        t_cube = cube_ganz_runter(t_cube)
    return(t_cube)

def cube_ganz_rechts_kippen(xcube):
    t_cube = xcube.copy()
    t_cube = cube_ganz_runter(t_cube)
    t_cube = cube_ganz_rechts(t_cube)
    t_cube = cube_ganz_rauf(t_cube)
    return t_cube

def cube_ganz_links_kippen(xcube):
    t_cube = xcube.copy()
    t_cube = cube_ganz_runter(t_cube)
    t_cube = cube_ganz_links(t_cube)
    t_cube = cube_ganz_rauf(t_cube)
    return t_cube


### Bewegung einzelner Ebenen nach gängiger Nomenklatur


# R ... R - Right side clockwise [Right side upwards]
# r ... R’ - Right side anticlockwise [Right side downwards]
# L ... L -  Left side clockwise [Left side downwards]
# e ... L’ - Left side anticlockwise [Left side upwards] (Note: L and R may be confusing at first since the moves are opposite to each other)
# F ... F - Front side clockwise 
# f ... F’ - Front side anticlockwise
# U ... U - Upper face clockwise
# u ... U’ - Upper face anticlockwise
# M ... M - Middle horizontal clockwise
# m ... M' - Middle horizontal anticlockwise

def U(xcube):
    t_cube = xcube.copy()
    t_slice = t_cube[2][2].copy()
    t_cube[2][2] = t_cube[3][2].copy()
    t_cube[3][2] = t_cube[0][2].copy()
    t_cube[0][2] = t_cube[1][2].copy()
    t_cube[1][2] = t_slice
    t_cube[4] = np.rot90(t_cube[4]) # im uzs
    return t_cube

def u(xcube):
    t_cube = xcube.copy()
    for x in range(3):
        t_cube = U(t_cube)
    return(t_cube)

def Ll(xcube,n):
    t_cube = xcube.copy()
    t_cube = cube_ganz_rechts_kippen(t_cube)
    for x in range(n):
        t_cube = U(t_cube)
    t_cube = cube_ganz_links_kippen(t_cube)    
    return(t_cube)

def L(xcube):
    t_cube = Ll(xcube,1)
    return t_cube

def l(xcube):
    t_cube = Ll(xcube,3)
    return t_cube

def Ff(xcube,n):
    t_cube = xcube.copy()
    t_cube = cube_ganz_rauf(t_cube)
    for x in range(n):
        t_cube = U(t_cube)
    t_cube = cube_ganz_runter(t_cube)
    return t_cube

def F(xcube):
    t_cube = Ff(xcube,1)
    return t_cube

def f(xcube):
    t_cube = Ff(xcube,3)
    return t_cube

def Rr(xcube,n):
    t_cube = xcube.copy()
    t_cube = cube_ganz_links_kippen(t_cube)
    for x in range(n):
        t_cube = U(t_cube)
    t_cube = cube_ganz_rechts_kippen(t_cube)
    return t_cube

def R(xcube):
    t_cube = Rr(xcube,1)
    return t_cube

def r(xcube):
    t_cube = Rr(xcube,3)
    return t_cube

def Bb(xcube,n):
    t_cube = xcube.copy()
    t_cube = cube_ganz_runter(t_cube)
    for x in range(n):
        t_cube = U(t_cube)
    t_cube = cube_ganz_rauf(t_cube)
    return t_cube

def B(xcube):
    t_cube = Bb(xcube,1)
    return t_cube

def b(xcube):
    t_cube = Bb(xcube,3)
    return t_cube

def Dd(xcube,n):
    t_cube = xcube.copy()
    t_cube = cube_ganz_rauf(t_cube)
    t_cube = cube_ganz_rauf(t_cube)
    for x in range(n):
        t_cube = U(t_cube)
    t_cube = cube_ganz_runter(t_cube)
    t_cube = cube_ganz_runter(t_cube)
    return t_cube

def D(xcube):
    t_cube = Dd(xcube,1)
    return t_cube

def d(xcube):
    t_cube = Dd(xcube,3)
    return t_cube

def M(xcube):
    t_cube = xcube.copy()
    t_cube = U(t_cube)
    t_cube = d(t_cube)
    t_cube = cube_ganz_rechts(t_cube)
    return t_cube

def m(xcube):
    t_cube = xcube.copy()
    t_cube = u(t_cube)
    t_cube = D(t_cube)
    t_cube = cube_ganz_links(t_cube)
    return t_cube


def move(xcube, value):
    xcube = xcube.copy()

    function_map = {
        'subfunc': {0: U, 1: u, 2: L, 3: l, 4: F, 5: f, 6: R, 7: r, 8: B, 9: b, 10: D, 11: d, 12: M, 13: m},
        'name': {0: 'U', 1: 'u', 2: 'L', 3: 'l', 4: 'F', 5: 'f', 6: 'R', 7: 'r', 8: 'B', 9: 'b', 10: 'D', 11: 'd', 12: 'M', 13:'m'}
    }

    name_to_func_map = {v: function_map['subfunc'][k] for k, v in function_map['name'].items()}
    name_to_number_map = {v: k for k, v in function_map['name'].items()}

    if isinstance(value, str) and value in name_to_func_map:
        xcube = name_to_func_map[value](xcube)
        name = value
        number = name_to_number_map[value]
    elif value in function_map['subfunc']:
        xcube = function_map['subfunc'][value](xcube)
        name = function_map['name'][value]
        number = value
    else:
        raise ValueError(f"nicht im Moveset: {value}")

    return xcube, name, number