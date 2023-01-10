import os
import imageio.v2 as imageio

png_dir = 'C:\\Users\\Victor\\Documents\\DTU\\41812 FEA\\Project 2\\ANSYS'
GifName = 'Anim.gif'
Time = 0.1

l = os.listdir(png_dir)
l = [val for val in l if val.endswith(".PNG")]

images = []
for file_name in sorted(l, key=lambda x: int(x.split(".")[0])) :
    if file_name.endswith('.PNG'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
        print(file_name)

imageio.mimsave(png_dir + '\\' + GifName,images,duration=Time)