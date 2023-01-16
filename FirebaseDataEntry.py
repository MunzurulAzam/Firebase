import pyrebase

# firebase key
config = {
    'apiKey': "AIzaSyDEWvdDa-52NsKvlqVbhee4nuz0uG-UeAc",
    'authDomain': "islamicapp-6b802.firebaseapp.com",
    'databaseURL': "https://islamicapp-6b802-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "islamicapp-6b802",
    'storageBucket': "islamicapp-6b802.appspot.com",
    'messagingSenderId': "831928341721",
    'appId': "1:831928341721:web:79966e89449ee8e7241ac8",
    'measurementId': "G-VJS7Z643ET"

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

while 1:
    shura_no = input("Enter shura number:")
    shura_name = input("Enter shura name:")

    data = {
        "shura_no": shura_no,
        "shura_name": shura_name,
    }
    db.child("কোরানের দোয়া").child("কোরানের সুরা").child("কোরানের সুরা নাম সমূহ").push(data)