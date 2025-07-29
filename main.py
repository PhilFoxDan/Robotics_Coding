import numpy as np
from numpy import sin, cos, pi, dot

# DH Parameters
# [theta (in degree), alpha (in degree), a, d]

def dhTransformation():
    
    tetha1 = input("Enter Tetha 1: ")
    tetha2 = input("Enter Tetha 2: ")
    tetha3 = input("Enter Tetha 3: ")
    tetha4 = input("Enter Tetha 4: ")
    tetha5 = input("Enter Tetha 5: ")
    
    tetha1 = np.deg2rad(int(tetha1))
    tetha2 = np.deg2rad(int(tetha2))
    tetha3 = np.deg2rad(int(tetha3))
    tetha4 = np.deg2rad(int(tetha4))
    tetha5 = np.deg2rad(int(tetha5))
    
    dh_params = [
        [tetha1, np.deg2rad(-90), 0, 1],  # 0
        [tetha2, 0, 2,  0],  # 1
        [tetha3, 0, 3, 3],  # 2
        [tetha4, np.deg2rad(-90), 0, 0],  # 3
        [tetha5, 0, 0, 5]  # 4
    ]
    
    T_total = np.identity(4)
    
    for i in reversed(dh_params):
        T = [
            [cos(i[0]), -sin(i[0])*cos(i[1]), sin(i[0])*sin(i[1]), i[2]*cos(i[0])],
            [sin(i[0]), cos(i[0])*cos(i[1]), -cos(i[0])*sin(i[1]), i[2]*sin(i[0])],
            [0,         sin(i[1]),            cos(i[1]),           i[3]],
            [0,         0,                    0,                   1]
        ]
        
        T_total = dot(T, T_total)
    
    T_total_Rounded = np.round(T_total, decimals=5)    
    print(T_total_Rounded)

if __name__ == "__main__":
    dhTransformation()