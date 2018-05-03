from  firebase import  firebase
firebase = firebase.FirebaseApplication('https://flycam-184516.firebaseio.com/', None)
def __results__(filename):
    result = firebase.get('/'+filename, None)
    return result
def __requests__(value,folderName):
    request = firebase.post('/'+folderName      ,{'Name':value})
    return value;

def __deleteData(pri_name,value):
    remove = firebase.delete(pri_name,value)
    return  remove;