#batch = (name, e-mail, age)

class ExceptionName (Exception): #класс исключения по недопустимости имени
    pass

class ExceptionEmail(Exception): #класс исключения по недопустимости эл. почты
    pass

class ExceptionAge(Exception): #класс исключения по недопустимости возраста
    pass

class ExceptionTypeOfAge(ExceptionAge):
    pass

class ExceptionValueOfAge(ExceptionAge):
    pass

class User():
    def __init__(self, name:str, email:str, age:int, *args, **kwargs) -> None:
        self.name = name
        self.email = email
        #self.age = age - имя пользователя мы не храним, просто проверяем

def UniqueName(name:str, catalog:list[User]): #функция проверки имени на уникальность
    flag = True
    for i in catalog:
        if i.name == name:
            flag = False
    return flag

catalog = dict() #{id: User(name, email), } - каталог готовых пользователей
user_data = [("1", "1@1", 15), ("3", "2@2", 19), ("3", "3@3", 23)] # набор сырых данных

for user in user_data:
    name = user[1]
    age = user[2]
    email = user[1]

    if not isinstance(age, int) or age<0:
        print("Ошибка в веденном возрасте!")
    elif age < 16:
        print("Пользователю меньше 16 лет!")
    elif "@" not in email or not (len(email[:email.index("@")]) and len(email[email.index("@")+1:])):
        print("Неверное введен email!")
    elif not UniqueName(name, catalog.values()):
        print("Имя не уникально!")
    else:
        check_user = User(*user) #Если при создании экземпляра класса User возникает ошибка, то обрабатывается except
        catalog[id(check_user)] = check_user #Если предыдущая строчка сработала без проблем, то добавляем пользователя в каталог

print(catalog)