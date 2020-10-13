import datetime
import os

data_pair = []
coordinate = []

def get_gps_data(log):
    readObj = os.popen('cat %s | grep GNRMC' % (log))
    gprmc = readObj.readlines()
    readObj.close()
    f = open(log+".data","w")
    writecnt = 0
    for line in gprmc:
        # print(line)
        array = line.split(',')
        if len(array) < 2:
            break
        if array[2] != 'V':
            time = datetime.datetime.strptime(array[1], "%H%M%S.00")
            str_time = time.strftime('%I:%M:%S')
            lon = array[5]
            index = lon.index('.')
            tmp = float(lon[index-2:])/60
            lon = float(lon[:index-2]) + tmp
            lat = array[3]
            index = lat.index('.')
            tmp = float(lat[index-2:])/60
            lat = float(lat[:index-2]) + tmp
            speed = array[7]
            gpsdatas=[lon, lat, speed]
            # print("time=", str_time, "long=",lon, "lat=", lat, "speed=", speed)
            data_pair.append([str_time, gpsdatas])
            # coordinate.append({"time":str_time, "lon":lon, "lat":lat, "speed":speed})
            coordinate.append(str_time)
            coordinate.append(str(lon))
            coordinate.append(str(lat))
            coordinate.append(speed)
            if writecnt == 0:
                string = str_time + "," + str(lon) + "," + str(lat) + "," + speed
            else:
                string = "," + str_time + "," + str(lon) + "," + str(lat) + "," + speed
            # print(string)
            f.write(string)
            writecnt = writecnt + 1
    # print(coordinate)
    f.close()
    print(log+" process finished!")
    return data_pair

def file_iter(path):
    if not os.path.isdir(path):
        print("Path '"+ path +"' doesnot exit, please select a folder and try again.")
        return
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            names = file.split('.')
            if (names[-1] == "gps") or (names[-1] == "nmea"):
                print(os.path.join(path, file))
                get_gps_data(os.path.join(path, file))

if __name__ == "__main__":
    # LOG = '20200923_155942_nmea.csv'
    # LOG = '20200107_114318.nmea'
    # get_gps_data(LOG)
    # print(data_pair)
    file_iter("./log_gps")
    # file_iter('.')
    # f = open("test.txt", "w")
    # f.write("hello")
    # print(f.tell())
    # f.close()
    # f = open("test.txt", "r")
    # str = f.readline()
    # print(f.tell())
    # print(str)
    # f.close()