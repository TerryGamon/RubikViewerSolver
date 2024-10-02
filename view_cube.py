import pandas as pd
import numpy as np
import plotnine as p9


def draw(t_cube):

    xmat = pd.DataFrame({
    'value': [0, 1, 2, 3, 4, 5],
    'color': ["yellow", "red", "white", "orange", "green", "blue"]
    })

    df_cube = pd.DataFrame()
    for x in range(6):
        t_df_cube = pd.DataFrame(t_cube[x])
        t_df_cube['zeile'] = t_df_cube.index 
        t_df_cube = t_df_cube.melt(id_vars='zeile', var_name='spalte', value_name='value')
        t_df_cube = pd.merge(t_df_cube, xmat, on='value', how='left')
        t_df_cube['nummer'] = x
        df_cube = pd.concat([df_cube, t_df_cube])
    
    df_cube['xpos'] = df_cube.spalte + (df_cube.nummer-1)*3
    df_cube['ypos'] = df_cube.zeile + 3

    df_cube['xpos'] = np.where(df_cube['nummer'] == 0, df_cube['spalte']+10, df_cube['xpos'])
        
    df_cube['xpos'] = np.where(df_cube['nummer'] == 5, df_cube['spalte']+3, df_cube['xpos'])
    df_cube['ypos'] = np.where(df_cube['nummer'] == 5, df_cube['zeile'], df_cube['ypos'])
    
    df_cube['xpos'] = np.where(df_cube['nummer'] == 4, df_cube['spalte']+3, df_cube['xpos'])
    df_cube['ypos'] = np.where(df_cube['nummer'] == 4, df_cube['zeile'] +6, df_cube['ypos'])
        
    df_cube['xpos'] = df_cube.xpos.astype(int)
    df_cube = df_cube.reset_index(drop=True)

    p=(p9.ggplot(df_cube) +
        p9.scale_x_continuous(breaks=None) +
        p9.scale_y_continuous(breaks=None) +
        p9.geom_tile(p9.aes(x='xpos', y='ypos', fill= 'color'), color= 'darkgray', size=1)  +
        p9.scale_fill_identity() +
        p9.theme_minimal()+
        p9.coord_fixed(ratio = 1)+
        p9.theme(axis_text= p9.element_blank())+
        p9.labs(x='', y='')
    )
    return p

# 0 hinten
# 1 links
# 2 vorne
# 3 rechts
# 4 oben
# 5 unten

