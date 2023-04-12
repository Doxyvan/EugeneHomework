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
        if not isinstance(age, int) or age<0:
            raise ExceptionTypeOfAge
        elif age < 16:
            raise ExceptionValueOfAge
        elif "@" not in email or not (len(email[:email.index("@")]) and len(email[email.index("@")+1:])):
            raise ExceptionEmail
        elif not UniqueName(name, catalog.values()):
            raise ExceptionName
        else:
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
user_data = [("1", "1@1", 15), ("2", "2@2", 19), ("3", "3@3", 23)] # набор сырых данных

for user in user_data:
    try:
        check_user = User(*user) #Если при создании экземпляра класса User возникает ошибка, то обрабатывается except
        catalog[id(check_user)] = check_user #Если предыдущая строчка сработала без проблем, то добавляем пользователя в каталог
    except ExceptionTypeOfAge:
        print("Возраст пользователя должен быть положительным целым числом")
    except ExceptionValueOfAge:
        print("Пользователю меньше 16 лет")
    except ExceptionEmail:
        print("Адрес электронной почты недействителен")
    except ExceptionName:
        print("Имя пользователя не уникально")

print(catalog)