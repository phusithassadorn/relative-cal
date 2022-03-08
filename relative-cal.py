#import ไลบรารี scipy เพื่อคำนวณค่าทางสถิติ และ ไลบรารี pandas สำหรับอ่านข้อมูล
from scipy import stats
import pandas as pd

#ใช้ฟังก์ชัน read_csv จากไลบรารี pandas อ่านข้อมูลจากไฟล์ชื่อ predator_dataset.csv แล้วในมาเก็บไว้ใน data frame ชื่อ data
data = pd.read_csv('predator_dataset.csv')