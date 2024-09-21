employe_list=[]
def employee_id():
    check=True
    print('EMPLOYE DETAILS')
    id=int(input('enter employee id:'))
    name = input('enter employee name: ')
    age = input('enter employee age: ')
    gender= input('enter employee gender: ')
    salary= input('enter employee salary: ')
    position= input('enter employee position : ')
    if len(employe_list)==0:
        check=True
    else:
        for i in  employe_list:
            if id == i['id']:
                check=False
                break
    if check==True:
        empdict={
            'id':id,
            'name':name,
            'age':age,
            'gender':gender,
            'salary':salary,
            'position':position
        }
        employe_list.append(empdict)
        print("employe id added successfully"
              )
    else:
        print('id already exist')
    print(employe_list)
def update_emp():
    id = int(input('enter employe id:'))
    for emp in employe_list:
        if id==emp['id']:
            print('choose your choice which deteails you want cahnge')
            print('''1.name
            2.age,
            3.salary,
            4.position''')
            updt=input('enter your choice:')
            if updt=="1":
                print('name:',emp['name'])
                emp['name']=input('enter name:')
            elif updt == "2":
                    print('age:', emp['age'])
                    emp['age'] = input('enter age:')
            elif updt=="3":
                print('salary:',emp['salary'])
                emp['salary']=input('enter salary:')
            elif updt=="4":
                print('position:',emp['position'])
                emp['position']=input('enter position:')
            print('update succesfully')
            break
            return
        else:
            print('employe not found')
print()
def delete_emp():
    id = int(input('enetr employe id:'))
    for i in employe_list:
        if id==i['id']:
            employe_list.remove(i)
            print('employe delete successfuly')
            return
    print('employe not fonded')