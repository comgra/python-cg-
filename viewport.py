xw_min, yw_min = 0, 0
xw_max, yw_max = 100, 100
xv_min, yv_min = 200, 200
xv_max, yv_max = 400, 400
xw, yw = 50, 75
xv = xv_min + (xw - xw_min) * (xv_max - xv_min) / (xw_max - xw_min)
yv = yv_min + (yw - yw_min) * (yv_max - yv_min) / (yw_max - yw_min)
print("Mapped point in viewport:", xv, yv)
