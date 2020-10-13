1.transform_gps_data.py select a folder to extract time, lng, lat and speed from GNRMC, and save the array in a file whit suffix ".data"
2.A button lies in the first line of gps_trace.html, kick the button to load a file which contains the GPS points information(including  time, lng, lat and speed)
3.gps_trace.html will translate the GPS points coordinate to Baidu coordinate by callback(it will cost a lot of time).
4.After step 3 or timeout(for 10 seconds), gps_trace.html tries to show points in Baidu map, and the center of the points will be set to the view center.
5. The points with high speed will show in red marker, low speed with orange,  static with blue.When mouse move to the point, the speed according to the point will appear.
