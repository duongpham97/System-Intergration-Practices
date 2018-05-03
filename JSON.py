import  json
from DEMOJSON.lophoc import lophoc
def read():
 with open("Demo.JSON","r") as file:
  data = json.load(file)
  print(data["Student"][3]["Name"])
def read1():
 f = open("Demo.JSON","r")
 data = f.read()
 print(data)
 return data
def write(filename):
 data = lophoc("Tich hop","Duong PH","Nguyen Thi Anh Dao")
 f = open(filename+".json","w+")
 f.write(data.toString())
 print(data.toString())

if __name__ == '__main__':
 write("Result")