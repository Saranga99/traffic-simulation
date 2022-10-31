import pickle
import numpy as np 

car = input("Enter Car Count : ")
# truck = input("Enter truck Count : ")
bus = input("Enter bus Count : ")
bicycle = input("Enter bicycle Count : ")
# lorry = input("Enter lorry Count : ")
speed = input("Enter Average speed(Km/h) : ")


test_data=np.array([car,bus,bicycle,speed]).reshape(1,-1)

DecisionTree_model=pickle.load(open('Decision_Tree.pkl','rb'))

prediction=DecisionTree_model.predict(test_data)

result = prediction[0]
print("output :",result)

if result == 0 :
    print("Low Traffic")
elif  result == 1 :
    print("Medium Traffic")
else :
    print("High Traffic")

     