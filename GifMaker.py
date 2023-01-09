import os
import imageio.v2 as imageio

png_dir = 'C:\\Users\\Victor\\Documents\\DTU\\41812 FEA\\Project 2\\ANSYS'
GifName = 'Anim.gif'
Time = 0.5

images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.PNG'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

imageio.mimsave(png_dir + '\\' + GifName,images,duration=Time)