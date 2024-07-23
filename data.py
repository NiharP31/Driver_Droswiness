from imports import os

data_path = r'C:\Users\nihar\Documents\github\Deep_learning\Driver_drowsiness\Driver Drowsiness Dataset (DDD)'

drowsy_data_path = [os.path.join(data_path, 'Drowsy', i) for i in os.listdir(os.path.join(data_path, 'Drowsy'))]
non_drowsy_data_path = [os.path.join(data_path, 'Non Drowsy', i) for i in os.listdir(os.path.join(data_path, 'Non Drowsy'))]

