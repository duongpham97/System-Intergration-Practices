from  DEMOJSON import RestFirebase as rect
from  firebase_admin import db
from firebase_admin import credentials
import firebase_admin
from DEMOJSON.lophoc import lophoc
if __name__ == '__main__':
    cred = credentials.Certificate('flycam-184516-firebase-adminsdk-fps0w-307954056b.json')
    # default_app = firebase_admin.initialize_app(cred)
    #
    # print(default_app.name)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://flycam-184516.firebaseio.com/'
    })
    info = lophoc("Tich hop","Duong PH","Nguyen Thi Anh Dao")
    refInfo = db.reference()
    request = refInfo.child("Person").set({
        'Class Name':info.name,
        'Student':info.student,
        'Teacher':info.teacher,
    })
    #rect.__requests__("Nhan","Nguoi")
    data = rect.__results__("Person")
    print(data)
