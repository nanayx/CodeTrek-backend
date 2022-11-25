# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('utils/serviceAccount1.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

#Users
def getUserIDByEM(user_email):
    doc_ref = db.collection("Users")
    doc = doc_ref.where("email","==",user_email).stream()
    for document in doc:
        return document.id

def getUserDataByID(doc_id):
    doc_ref = db.collection("Users").document(doc_id)
    doc = doc_ref.get()
    return doc.to_dict()

def getUserDataByEM(user_email):
    doc_ref = db.collection("Users")
    doc = doc_ref.where("email","==",user_email).stream()
    for document in doc:
        return document.to_dict()

def getUserExpByEM(user_email):
    udata = getUserDataByEMFB(user_email)
    return udata['exp']

def getUserLevelByEM(user_email):
    udata = getUserDataByEMFB(user_email)
    return udata['level']

def getUserMoneyByEM(user_email):
    udata = getUserDataByEMFB(user_email)
    return udata['money']

def getUserScoreByEM(user_email):
    udata = getUserDataByEMFB(user_email)
    return udata['score']

def getUserScoreRank():
    doc_ref = db.collection("Users")
    doc = doc_ref.order_by("score", direction=firestore.Query.DESCENDING) 
    rank = doc.get()
    ret = {}        
    count = 1
    for document in rank:
        ID = document.id
        udata = getUserDataByID(ID)
        ret[count] = udata
        count += 1
    return ret

def setUserDataByID(doc_id, data):
    doc_ref = db.collection("Users").document(doc_id)
    doc_ref.set(data)

def setUserLevelByEM(user_email, level):
    udata = getUserDataByEMFB(user_email)
    udata['level'] = level
    
    doc_ref = db.collection("Users")
    doc = doc_ref.where("email","==",user_email).stream()
    for document in doc:
        doc_id = document.id

    setUserDataByID(doc_id, udata)

def setUserExpByEM(user_email, exp):
    udata = getUserDataByEMFB(user_email)
    udata['exp'] = exp
    doc_id = getIDByEM(user_email)
    setUserDataByID(doc_id, udata)

def setUserMoneyByEM(user_email, money):
    udata = getUserDataByEMFB(user_email)
    udata['money'] = money
    doc_id = getIDByEM(user_email)
    setUserDataByID(doc_id, udata) 

def setUserScoreByEM(user_email, score):
    udata = getUserDataByEMFB(user_email)
    udata['score'] = score
    doc_id = getIDByEM(user_email)
    setUserDataByID(doc_id, udata)

#Pets
def getPetIDByEM(user_email):
    doc_ref = db.collection("Pets")
    doc = doc_ref.where("usermail", "==", user_email).stream()
    for document in doc:
        return document.id

def getPetDataByEM(user_email):
    doc_ref = db.collection("Pets")
    doc = doc_ref.where("usermail", "==", user_email).stream()
    for document in doc:
        return document.to_dict()

def getPetTypeByEM(user_email):
    pdata = getPetDataByEM(user_email)
    return pdata['type']

def getPetListDataByID(doc_id):
    doc_ref = db.collection("PetList").document(doc_id)
    doc = doc_ref.get()
    return doc.to_dict()

def getPetListImageByID(doc_id):
    pldata = getPetListDataByID(doc_id)
    return pldata['image']
  


def setPetDataByEM(usermail, petname, level, exp, types):
    pdata = {
        "usermail" : usermail,
        "petname" : petname,
        "level" : level,
        "exp" : exp,
        "type" : types
    }
    doc_ref = db.collection("Pets").add(pdata)

def setPetIDByEM(user_email):   
    udata = getUserDataByEMFB(user_email)
    pet_id = getPetIDByEM(user_email)
    doc_id = getIDByEM(user_email)
    udata['petid'] = pet_id
    setUserDataByID(doc_id, udata)

# doc_ref = db.collection("player").document("Jacc")

# doc = doc_ref.get()

# if doc.exists:
#     print(f"Document data: {doc.to_dict()}")
# else:
#     print("No such document!")

if __name__ == '__main__':
    #setPlayerLevel("Jacc2", 999)    
    #getMONEYByIDFB("Jacc")
    #modifyPlayerID("Jacc", "Jacc4")
    #setNewPlayer("nana",487,3,8938)

    #getUserDataByEMFB("123@gmail.com")
    #getSCOREByEMFB("hejnja@gmail.com")
    #setUserScore("123@gmail.com", 8888)
    #setPetData("22@gmail.com", "jacc", "5", "344")
    setUserPETID("123@gmail.com")