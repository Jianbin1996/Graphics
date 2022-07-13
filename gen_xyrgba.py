import random
import matplotlib.pyplot as plt
import numpy as np


size = 64
x_width = 12;
y_width = 12;
num_xy = 2;  #number of x-y pairs per line segment

slope = -32;
y_intercept = 90;

rgb_bitwidth = 14;

num_seg = 2

def int2bi(data,bit_width):
        bi = bin(data)
        bi = bi[2:]
        if(bit_width - len(bi) > 0):
                bi = (bit_width - len(bi))* '0' + bi
        return bi

def norm(data, max_val, width):
        div = (data / max_val) * 100
        return int2bi(data,width)



#generates x,y,r,g,b,a values 
def gen_xy_input(num_xy,slope,y_intercept,num_seg,rgb_bitwidth):
        x_array = []
        y_array = []
        x_bi_array = []
        y_bi_array = []
        fx = open("x_input.txt", "w")
        fy = open("y_input.txt", "w")
        frgbv = open("rgbv_input.txt", "w")
        rgbv_array = []
        for n in range(num_seg): #devide into a few line segments
                x_center = random.randint(0,480) #find a random center for start point 
                y_center = random.randint(0,480)
                r = random.randint(0,255) #8-bit 
                g = random.randint(0,255)
                b = random.randint(0,255)
                v = random.randint(0,255)
                for i in range (num_xy): #for each line segment, introduce some noises due to ADC
                        x = x_center + 10*random.random()
                        y = y_center + 10*random.random()
                        x_bi = int2bi(int(x),14)
                        y_bi = int2bi(int(y),14)
                        r_bi = int2bi(int(r),rgb_bitwidth)
                        g_bi = int2bi(int(g),rgb_bitwidth)
                        b_bi = int2bi(int(b),rgb_bitwidth)
                        v_bi = int2bi(int(v),rgb_bitwidth)
                        fx.write(x_bi+"\n")
                        fy.write(y_bi+"\n")
                        frgbv.write(str(r_bi)+str(g_bi) + str(b_bi) + str(v_bi)+"\n")
                        x_array.append(x)
                        y_array.append(y)
                        rgbv_array.append([r ,g, b,v])
        fx.close()
        fy.close()
        frgbv.close()
        return x_array,y_array,rgbv_array
#generates r,g,b values 
def raster_input(size):
        #set the random seed so we all get the same matrix
        seed = np.random.RandomState(2021)
        #create a 48 X 48 checkerboard of random colours
        rgb_array = seed.randint(0,255,size=(size,size,3))
        return rgb_array

#plot raster buffer output 
def plot_pixel(rgb_array):
        pixel_plot = plt.figure()
        plt.imshow(rgb_array,interpolation = 'nearest', origin = 'lower')
        plt.show()

#plot line segment
def plot_xy(x_arr,y_arr,num_xy):
        fig,xy_plot = plt.subplots()
        for i in range(len(x_arr)/num_xy):
                xy_plot.plot(x_arr[num_xy*i:num_xy*i-1],y_arr[num_xy*i:num_xy*i-1],linewidth = 4)
        #xy_plot.plot(x_arr[0:2],y_arr[0:2],linewidth = 4)
        plt.show()


val = int2bi(32,8)
print(val)
x_arr, y_arr, rgbv_arr = gen_xy_input(num_xy,slope,y_intercept,num_seg,rgb_bitwidth)

#rgb_array = raster_input(size)
#plot_pixel(rgb_array)
#plot_xy(x_arr,y_arr,num_xy)

#plot_pixel 

