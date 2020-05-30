from microbit import *
from array import array
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
    return diff/(len(peaks)-1)*40*1e-3
data = []
display.show("3")
sleep(1000)
display.show("2")
sleep(1000)
display.show("1")
sleep(1000)
print("A")
data = array("f",[0]*350)
for i in range(350):
    if i%25==0:
        display.scroll(str((350-i)//25),delay=50)
    sleep(40)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    norm = (x**2 + y**2 + z**2)**(1/2)
    data[i]= norm
display.scroll("Calculating...")
T = calculate_period(find_peaks(autocorrelate(data)))
while True:
    display.show("A")
    if button_a.is_pressed():
        display.scroll(str(T))
        display.scroll("sec")
