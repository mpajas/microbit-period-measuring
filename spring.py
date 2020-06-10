from microbit import *
from array import array

N = 300
time_step = 30

def mean(arr):
    return sum(arr)/len(arr)

def autocorrelate(data):
    autocorrel = array("f",[0]*len(data))
    for i in range(len(data)):
        for j in range(len(data)):
            autocorrel[i] += data[j] * data[ ( j + i ) % len(data)]
    return autocorrel

def find_peaks(data):
    peaks = []
    for i in range(1, len(data)-1):
        if(data[i-1]<data[i] and data[i+1]<data[i]):
            peaks.append(i)
    return peaks

def calculate_period(peaks):
    diff = 0
    for i in range(len(peaks)-1):
        diff+=peaks[i+1]-peaks[i]
    return diff/(len(peaks)-1)*time_step*1e-3

for i in range(3):
    display.show(str(3-i))
    sleep(1000)

data = array("f",[0]*N)
display.show("M",delay=50)

for i in range(N):
    sleep(time_step)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    norm = (x**2 + y**2 + z**2)**(1/2)
    data[i]= norm

display.scroll("Calculating...")

autocor = autocorrelate(data)
peaks = find_peaks(autocor)
T = calculate_period(peaks)
#potrebno je dodati odsječak za računanje konstante elastičnosti:
#početak odsječka
#pi = 3.14159265359
#m = 0.200 #kg
#k = m*((2*pi)/T)**2
#kraj odsječka

while True:
    display.show("A")
    if button_a.is_pressed():
        display.scroll(str(T))
        display.scroll("sec")
    #potrebno je dodati odsječak za računanje konstante elastičnosti:
    #početak odsječka
    #if button_b.is_pressed():
    #    display.scroll(str(k))
    #kraj odsječka
