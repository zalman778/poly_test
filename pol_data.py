# coding=utf-8_sig
import random, datetime

#Data file for exact tests
b_login = u"Test Login"  #to test sql inj
b_pass = u"Test Pass"
c_login = u"mpetrov"#.decode('utf-8')
c_pass = u"Qwerty123"
d_rus_name = u"Оптика Nikon 2"#.decode('cp1251').encode('utf-8').decode('utf-8_sig')   #to test rand uts8 symbols
d_eng_name = u"Nikon's optics 2"
d_acro = u"УФМС"#.encode('utf-8').decode('utf-8_sig')
d_web = u"google.fl"
#d_startd = u"01.01.2015"
#d_endd = u"01.01.2015"   #To test: 30, 31feb
d_country = u"Россия"#.decode('utf-8')#.encode('utf-8').decode('utf-8_sig')
d_city = u"Санкт"#.decode('cp1251').encode('utf-8').decode('utf-8_sig')
d_org = u"СПБПУ"#.decode('cp1251').encode('utf-8').decode('utf-8_sig')

#Function of logging IN as user_lvl; [=1 - user;=2  - moder ]
def login_form_enter(self, user_lvl):
    driver = self.driver
    if user_lvl == 1:
        lg_user = "myasnov_av"
        lg_pass = "Qwerty123"
        driver.find_element_by_id("id_login").clear()
        driver.find_element_by_id("id_login").send_keys(lg_user)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(lg_pass)
    elif user_lvl ==2:
        lg_user = "vlad"
        lg_pass = "Qwerty123"
        driver.find_element_by_id("id_login").clear()
        driver.find_element_by_id("id_login").send_keys(lg_user)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(lg_pass)
        driver.find_element_by_xpath(u"//input[@value='Войти']").click()
        driver.find_element_by_xpath("(//button[@name='template'])[2]").click()

    elif user_lvl == 3:
        lg_user = "mpetrov"
        lg_pass = "Qwerty123"
        driver.find_element_by_id("id_login").clear()
        driver.find_element_by_id("id_login").send_keys(lg_user)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(lg_pass)
        driver.find_element_by_xpath(u"//input[@value='Войти']").click()

#Function of logging OUT
def login_form_logout(self):
    driver = self.driver
    driver.find_element_by_xpath("//div[@class='navbar-right']//a[@class='dropdown-toggle']").click()
    driver.find_element_by_link_text(u"Выйти").click()

#Function current date to string
def currDateGen():
    time_mdl = datetime.datetime.now()
    time_cr = str(time_mdl.year)+"_"+str(time_mdl.month)+"_"+str(time_mdl.day)+"-"+str(time_mdl.hour)+"_"+str(time_mdl.minute)+"_"+str(time_mdl.second)
    return time_cr
    

#based of querries from DB
DataBase_real_staff = [
    u"Мяснов Александр",
    u"Писков Валерий",
    u"Гагарский Кирилл",
    u"Козловский Виталий",
    u"Петрович Сергей Юрьевич",
    u"Безухов Андрей",
    u"Филиппов Алексей",
    u"Хан Дмитрий" ]

def db_real_staff_gen():
    return DataBase_real_staff[random.randint(0, len(DataBase_real_staff)-1)]

DataBase_fake_staff = [
    u"Богатырёв Добрыня Никитич",
    u"Никифоров Ядрен Коньякович",
    u"Лисс Лев Эрмитович",
    u"Адольф Ильич Трупогрызов",
    u"Листопад Денис Сидорович",
    u"Борис Борис Борисович",
    u"Рудик Ефрим Робертович",
    u"Замша Игрорь Федорович" ]


def db_fake_staff_gen():
    return DataBase_fake_staff[random.randint(0, len(DataBase_fake_staff)-1)]

DataBase_fake_item_names = [
    u"Фазатронный синхрогенератор ",
    u"Стенд DiLab ",
    u"Приора спорт @kmph ",
    u"Турбофен ",
    u"Бластер водный ",
    u"Турбо веник ",
    u"Компрессор пластмассовый ",
    u"Вертикальный Синхронизатор " ]


def db_fake_item_names():
    return DataBase_fake_item_names[random.randint(0, len(DataBase_fake_item_names)-1)]+str(random.randint(50, 200))

#*  *   *   *   *   *   *   *
#MODULE: Confs
#*  *   *   *   *   *   *   *
DataBase_confs_names = [
    "SECR",
    "Scroll Lock",
    "qqq",
    u"Упячка",
    u"дроп дэйтабэйс",
    u"Фиолетовая морковь",
    u"Петросян-3",
    u"Охота крепкое" ]
global DataBase_confs_current
DataBase_confs_current = 0

def db_conf_name_gen():
    return "conf_"+str(currDateGen())

def db_conf_name_get():
   return DataBase_confs_names[DataBase_confs_current]
#site adress gen:

#*  *   *   *   *   *   *   *
#OIS num generator with memory
global DataBase_added_ois_nums
DataBase_added_ois_nums = []

def db_ois_num_gen():
    num = "2456"+str(random.randint(100, 999))
    DataBase_added_ois_nums.append(num)
    return num

DataBase_added_confs = []
DataBase_added_confs_names = []
DataBase_added_confs_zc = []

#*  *   *   *   *   *   *   *
#MODULE: Члены редколлегий
#*  *   *   *   *   *   *   *
DataBase_added_editorials = []

#*  *   *   *   *   *   *   *
#MODULE: Диссертационные советы
#*  *   *   *   *   *   *   *
DataBase_added_disscouncil = []

#*  *   *   *   *   *   *   *
#MODULE: Конкурсы и гранты
#*  *   *   *   *   *   *   *
DataBase_added_grant = []
DataBase_added_grantbox = ''
DataBase_added_grant_zc = []




