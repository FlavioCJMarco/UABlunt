import telebot
from telebot import types
import logging
import time

TOKEN = "802101135:AAEjTDm69YM33QF8fft46QYzOcvE59zSn-o"

userStep = {}
knownUsers = []

commands = {
    'start': 'Arranca el bot',
    'debug': 'Comandos disponibles',
    'setCaladas': 'Ejecuta un comando'
}

age = {}
gender = {}
uab = {}
weed = {}
regDone = {}
inReg = {}
peleaEmojis = {}

gameON = {}
caladas = {}
asigRol = {}
facVet = {}
facTrad = {}
plCivica = {}
facSoc = {}
facCien = {}
escVitae = {}
debugBool = {}

data = {}

#######################################33
# DEFINICIÓN BOOLEANOS SITUACIONES
sitShown = {}
dialogo = {}
sit1bool = {}
sit2bool = {}
sit3bool = {}
sit4bool = {}
sit5bool = {}
sit6bool = {}
sit7bool = {}
sit8bool = {}
sit9bool = {}
sit10bool = {}
sit11bool = {}
sit12bool = {}
sit13bool = {}
sit14bool = {}
sit15bool = {}
sit16bool = {}
sit17bool = {}
sit18bool = {}
sit19bool = {}
sit20bool = {}
sit21bool = {}
sit22bool = {}
sit23bool = {}
sit24bool = {}
sit25bool = {}
sit26bool = {}
sit27bool = {}
sit28bool = {}
sit29bool = {}
sit30bool = {}
sit31bool = {}

boolAgresivo = {}
boolCauto = {}

boolFumeta = {}
boolNeutro = {}
boolSano = {}

boolPrueba = {}
boolNoPrueba = {}

boolMuerte = {}

list_objetos = []
list_objetos_willy = []
list_objetos = [" ", ", Mapa del Eix Central🗺", ", Lazo Amarillo🎗", ", Casco Romano⛑", ", Pokéball Vacía🏀", ", Tarjeta Misteriosa💳"]
list_objetos_willy = [" ", ", Granada del Fortnite 💣", ", Pico del Minecraft ⛏"]
list_objetos_jordi=[" ",",  Llave del Despacho QC/1024 🔑"]
objeto1 = {}
objeto2 = {}
objeto3 = {}
f = {}
pienso = {}


def set_reg_bools(cid):
    ###################################
    # BOOLEANOS DE REGISTRO:
    age[cid] = False
    gender[cid] = False
    uab[cid] = False
    weed[cid] = False
    regDone[cid] = False
    inReg[cid] = False
    peleaEmojis[cid] = False

    debugBool[cid] = False
    caladas[cid] = 0



def set_game_bools(cid):
    caladas[cid] = 0
    # BOOLEANOS DE CONTROL DE JUEGO:
    boolMuerte[cid] = False
    gameON[cid] = False
    asigRol[cid] = False
    facVet[cid] = False
    facTrad[cid] = False
    plCivica[cid] = False
    facSoc[cid] = False
    facCien[cid] = False
    pienso[cid] = False
    objeto1[cid] = 0
    objeto2[cid] = 0
    objeto3[cid] = 0
    # BOOLEANOS DE SITUACION
    dialogo[cid] = False
    sitShown[cid] = False
    sit1bool[cid] = False
    sit2bool[cid] = False
    sit3bool[cid] = False
    sit4bool[cid] = False
    sit5bool[cid] = False
    sit6bool[cid] = False
    sit7bool[cid] = False
    sit8bool[cid] = False
    sit9bool[cid] = False
    sit10bool[cid] = False
    sit11bool[cid] = False
    sit12bool[cid] = False
    sit13bool[cid] = False
    sit14bool[cid] = False
    sit15bool[cid] = False
    sit16bool[cid] = False
    sit17bool[cid] = False
    sit18bool[cid] = False
    sit19bool[cid] = False
    sit20bool[cid] = False
    sit21bool[cid] = False
    sit22bool[cid] = False
    sit23bool[cid] = False
    sit24bool[cid] = False
    sit25bool[cid] = False
    sit26bool[cid] = False
    sit27bool[cid] = False
    sit28bool[cid] = False
    sit29bool[cid] = False
    sit30bool[cid] = False
    sit31bool[cid] = False

    # BOOLEANOS DE ROL
    boolAgresivo[cid] = False
    boolCauto[cid] = False

    boolFumeta[cid] = False
    boolNeutro[cid] = False
    boolSano[cid] = False

    boolPrueba[cid] = False
    boolNoPrueba[cid] = False


###################################

menu = types.ReplyKeyboardMarkup()
menu.add("Acceder al registro 🍃")
menu.add("Seleccionar idioma 🌐")

age_list = []  # Creamos esta lista para añadir todas las posibles respuestas y comprobar si el usuario ha introducido una correcta en el message handler del menú
age_list = ["Soy menor de 18 años. 🧒", "Tengo entre 18 y 25 años.👦", "Tengo entre 26 y 40 años. 🧑",
            "Tengo entre 40 y 60 años. 🧓", "Tengo 61 años o más. 👵", "Prefiero no contestar. 🤷"]
age_menu = types.ReplyKeyboardMarkup()
age_menu.add("Soy menor de 18 años. 🧒")
age_menu.add("Tengo entre 18 y 25 años.👦")
age_menu.add("Tengo entre 26 y 40 años. 🧑")
age_menu.add("Tengo entre 40 y 60 años. 🧓")
age_menu.add("Tengo 61 años o más. 👵")
age_menu.add("Prefiero no contestar. 🤷")

gender_list = ["♂", "♀", "Prefiero no contestar. 🤷️"]
gender_menu = types.ReplyKeyboardMarkup()
gender_menu.add(gender_list[0])
gender_menu.add(gender_list[1])
gender_menu.add(gender_list[2])

uab_list = ["Sí, estoy relacionado directamente con la Universitat Autònoma de Barcelona.",
            "No, no tengo relación alguna."]
uab_menu = types.ReplyKeyboardMarkup()
uab_menu.add(uab_list[0])
uab_menu.add(uab_list[1])

weed_list = ["Sí.", "No.", "Prefiero no contestar. 🤷"]
weed_menu = types.ReplyKeyboardMarkup()
weed_menu.add(weed_list[0])
weed_menu.add(weed_list[1])
weed_menu.add(weed_list[2])

lang_list = ["ESPAÑOL 🇪🇸", "CATALÀ 🏴󠁥󠁳󠁣󠁴󠁿", "ENGLISH 🇬🇧",
             "Atrás"]  # La bandera de Cataluña es así de larga en emoji, sí
lang_menu = types.ReplyKeyboardMarkup()
lang_menu.add(lang_list[0], lang_list[1], lang_list[2])
lang_menu.add(lang_list[3])

debug_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
debug_menu = types.ReplyKeyboardMarkup()
debug_menu.add(debug_list[0], debug_list[1])  # VA/VA
debug_menu.add(debug_list[2], debug_list[3])  # VA/VA
debug_menu.add(debug_list[4], debug_list[5])
debug_menu.add(debug_list[6], debug_list[7])  # /VA
debug_menu.add(debug_list[8], debug_list[9])  # VA/
debug_menu.add(debug_list[10])

setCaladas_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20", "21", "22", "23", "24", "25"]
setCaladas_menu = types.ReplyKeyboardMarkup()
setCaladas_menu.add(setCaladas_list[0], setCaladas_list[1], setCaladas_list[2], setCaladas_list[3], setCaladas_list[4])
setCaladas_menu.add(setCaladas_list[5], setCaladas_list[6], setCaladas_list[7], setCaladas_list[8], setCaladas_list[9])
setCaladas_menu.add(setCaladas_list[10], setCaladas_list[11], setCaladas_list[12], setCaladas_list[13],
                    setCaladas_list[14])
setCaladas_menu.add(setCaladas_list[15], setCaladas_list[16], setCaladas_list[17], setCaladas_list[18],
                    setCaladas_list[19])
setCaladas_menu.add(setCaladas_list[20], setCaladas_list[21], setCaladas_list[22], setCaladas_list[23],
                    setCaladas_list[24])
setCaladas_menu.add(setCaladas_list[25])

boton_rol_list = ["¡ASÍGNAME UN ROL! 🧙"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA ASIGNACIÓN DE ROL
boton_rol = types.ReplyKeyboardMarkup()
boton_rol.add(boton_rol_list[0])

mid_menu_list = ["Iniciar Partida 🍂", "Seleccionar idioma 🌐", "Modificar registro e iniciar partida 🍃"]
mid_menu = types.ReplyKeyboardMarkup()
mid_menu.add(mid_menu_list[0], mid_menu_list[1], mid_menu_list[2])

game_menu_list = ["Dar calada 🚬🍁", "STATS 📖", "Forzar fin de partida ❌"]
game_menu = types.ReplyKeyboardMarkup()
game_menu.add(game_menu_list[0], game_menu_list[1])
game_menu.add(game_menu_list[2])

boton_muerte_list = ["VOLVER A EMPEZAR 🏁"]  # SOLO UN BOTÓN QUE NOS LLEVE AL MENU PRINCIPAL AL MORIR
boton_muerte = types.ReplyKeyboardMarkup()
boton_muerte.add(boton_muerte_list[0])

heart = types.ReplyKeyboardMarkup()  # DE ESTA FORMA MOSTRAMOS UN CORAZONCITO EN UN MENÚ GRANDE QUE NO REDIRIGE A NADA, PUEDE SER ÚTIL
heart.add("❤")

boton_vet_list = ["VETERINARIA 🦓"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA FACULTAD DE VETERINARIA
boton_vet = types.ReplyKeyboardMarkup()
boton_vet.add(boton_vet_list[0])

boton_trad_list = ["TRADUCCIÓN E INTERPRETACIÓN ㊙️"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA FACULTAD DE TRADUCCIÓN
boton_trad = types.ReplyKeyboardMarkup()
boton_trad.add(boton_trad_list[0])

boton_plaza_list = ["PLAZA CÍVICA 🚬️"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA PLAZA CIVICA
boton_plaza = types.ReplyKeyboardMarkup()
boton_plaza.add(boton_plaza_list[0])

boton_social_list = ["️CIENCIAS SOCIALES 💰"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA FACULTAD DE CIENCIAS SOCIALES
boton_social = types.ReplyKeyboardMarkup()
boton_social.add(boton_social_list[0])

boton_ciencia_list = ["️CIENCIAS 🔬"]  # SOLO UN BOTÓN QUE NOS LLEVE A LA FACULTAD DE CIENCIAS
boton_ciencia = types.ReplyKeyboardMarkup()
boton_ciencia.add(boton_ciencia_list[0])

boton_vitae_list = ["️VITAE 🥊"]  # SOLO UN BOTÓN QUE NOS LLEVE A VITAE
boton_vitae = types.ReplyKeyboardMarkup()
boton_vitae.add(boton_vitae_list[0])

boton_eng_list = ["ENGINYERIA 📡 "]  # SOLO UN BOTÓN QUE NOS LLEVE A LA FACULTAD DE ENGINYERIA
boton_eng = types.ReplyKeyboardMarkup()
boton_eng.add(boton_eng_list[0])


# COLOR TEXTO EN LA CONSOLA DEL SERVIDOR
class color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# USER STEP
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print(color.RED + " [¡] ¡¡NUEVO USUARIO!!" + color.ENDC)


# LISTENER
def listener(messages):
    global inReg
    for m in messages:
        if m.content_type == 'text':
            cid = m.chat.id
            print("[" + str(cid) + "] " + str(m.chat.first_name) + ": " + m.text)  # IMPRIMIMOS EL LOG POR PANTALLA
            f[cid] = open('log' + str(cid) + '.txt', 'a')  # Abrimos nuestro fichero log en modo 'Añadir'.
            f[cid].write("[" + str(cid) + "] " + str(
                m.chat.first_name) + ": " + m.text + "\n")  # Escribimos la linea de log en el fichero.
            f[cid].close()  # Cerramos el fichero para que se guarde.

            '''if inReg[cid]==True:
                f[cid] = open( 'log'+str(cid)+'REG.txt', 'a') #Guardamos el registro en modo SOBREESCRIBIR
                f[cid].write("[" + str(cid) + "] " + str(m.chat.first_name) + ": " + m.text + "\n")
                f[cid].close()
            else:
                f[cid] = open( 'log'+str(cid)+'.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
                f[cid].write("[" + str(cid) + "] " + str(m.chat.first_name) + ": " + m.text + "\n") # Escribimos la linea de log en el fichero.
                f[cid].close() # Cerramos el fichero para que se guarde.'''


bot = telebot.AsyncTeleBot(TOKEN)
bot.set_update_listener(listener)

instagram = telebot.types.InlineKeyboardMarkup()
instagram.row(telebot.types.InlineKeyboardButton('Instagram de Pedro B. 📸', url='https://www.instagram.com/pbauza/'))
instagram.row(telebot.types.InlineKeyboardButton('Instagram de Néstor 📸', url='https://www.instagram.com/nestorcamposg/'))
instagram.row(telebot.types.InlineKeyboardButton('Instagram de Flavio 📸', url='https://www.instagram.com/flaviocjm/'))
instagram.row(telebot.types.InlineKeyboardButton('Instagram de Samer 📸', url='https://www.instagram.com/samerbujana/'))
instagram.row(telebot.types.InlineKeyboardButton('Instagram de Pedro G. 📸', url='https://www.instagram.com/pedro_gs_99/'))





# START
@bot.message_handler(commands=['start'])
def command_start(m):
    global regDone, debugBool, knownUsers, objeto1, objeto2, objeto3

    cid = m.chat.id
    # set_game_bools(cid)
    userStep[cid] = 0

    get_user_step(m.chat.id)

    if cid not in knownUsers or regDone[cid] == False:
        set_reg_bools(cid)
        if cid not in knownUsers:
            knownUsers.append(cid)

        bot.send_message(cid, "Hola, " + str(m.chat.first_name) + "...")
        time.sleep(1)
        bot.send_message(cid, "🍁 Bienvenida/o a UABlunt 🍁")
        time.sleep(1)
        bot.send_message(cid, "Desarrollado por:\n-Pedro José Bauzá\n-Néstor Campos\nFlavio Jiménez\n\nEscrito por:\n-Samer Bujana\n-Pedro García",reply_markup=instagram)
        time.sleep(3)
        bot.send_message(cid, "Puedes contactar directamente con el equipo de desarrollo a través del bot @UABluntFeedbackBot :)")
        time.sleep(2)
        bot.send_message(cid, "Antes de nada, necesitamos que contestes unas cuantas preguntas personales para ayudarnos a mejorar.",
                         reply_markup=menu)
    else:
        objeto1[cid] = 0
        objeto2[cid] = 0
        objeto3[cid] = 0
        bot.send_message(cid, "¡Bienvenido de nuevo a UABlunt, " + str(m.chat.first_name) + "!\n\nTIP: ¡Cuéntanos qué opinas de UABlunt a través de @UABluntFeedbackBot!", reply_markup=mid_menu)


# DEBUG
@bot.message_handler(commands=['debug'])
def command_debug(m):
    cid = m.chat.id
    userStep[cid] = 100
    debugBool[cid] = True
    bot.send_message(cid, "UABlunt Debug v1.0", reply_markup=debug_menu)
    bot.send_message(cid,
                     "0. Menú Principal\n1. Registro\n2.Selección de idioma\n3. Asignación de Rol\n4. Veterinaria\n5. Traducción e Interpretación\n6. Plaza Cívica\n7. Ciencias Sociales\n8. Ciencias\n9. VITAE\n10. Escola d'Enginyeria")


@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 100)
def debug(m):
    global regDone, userStep, asigRol, sitShown, gameON, knownUsers, debugBool

    cid = m.chat.id
    text = m.text

    # print(caladas[cid]+"  "+regDone[cid])
    if cid not in knownUsers or regDone[cid] == False:
        set_reg_bools(cid)
        set_game_bools(cid)
        regDone[cid] = True
        if cid not in knownUsers:
            knownUsers.append(cid)
    sitShown[cid] = False
    debugBool[cid] = True
    if text == '0':
        regDone[cid] = True
        userStep[cid] = 0
        bot.send_message(cid, "Menú Principal", reply_markup=mid_menu)

    if text == '1':
        userStep[cid] = 1
        bot.send_message(cid, "Registro")
        bot.send_message(cid, "¿Cuántos años tienes?", reply_markup=age_menu)

    if text == '2':
        userStep[cid] = 2
        bot.send_message(cid, "Selección de idioma", reply_markup=lang_menu)

    if text == '3':
        sitShown[cid] = False
        asigRol[cid] = True
        userStep[cid] = 3
        bot.send_message(cid, "Asignación de rol", reply_markup=boton_rol)

    if text == '4':
        userStep[cid] = 4
        bot.send_message(cid, "Veterinaria", reply_markup=boton_vet)

    if text == '5':
        userStep[cid] = 5
        bot.send_message(cid, "Traducción e Interpretación", reply_markup=boton_trad)

    if text == '6':
        userStep[cid] = 6
        bot.send_message(cid, "Plaza Cívica", reply_markup=boton_plaza)

    if text == '7':
        userStep[cid] = 7
        bot.send_message(cid, "Ciencias Sociales", reply_markup=boton_social)

    if text == '8':
        userStep[cid] = 8
        bot.send_message(cid, "Ciencias", reply_markup=boton_ciencia)

    if text == '9':
        userStep[cid] = 9
        bot.send_message(cid, "VITAE", reply_markup=boton_vitae)

    if text == '10':
        userStep[cid] = 10
        bot.send_message(cid, "Escola d'Enginyeria", reply_markup=boton_eng)


# SET CALADAS (SOLO DEBUG)
@bot.message_handler(commands=['setCaladas'])
def command_setCaladas(m):
    global debugBool, regDone, knownUsers, userStep
    cid = m.chat.id

    if debugBool[cid] == True:
        userStep[cid] = 101
        bot.send_message(cid, "setCaladas [Only Debug Mode]", reply_markup=setCaladas_menu)

    else:
        bot.send_message(cid,
                         "❌ ERROR CRÍTICO ❌\n\nSe ha intentado acceder a una función a la que no se tiene acceso. Se debe haber activado el modo debug con anterioridad.\n\nLa partida se ha reseteado.",
                         reply_markup=menu)


@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 101)
def setCaladas(m):
    cid = m.chat.id
    text = m.text
    caladas[cid] = int(text)
    userStep[cid] = 100
    bot.send_message(cid, "Regresando al menú de debug", reply_markup=debug_menu)
    bot.send_message(cid,
                     "0. Menú Principal\n1. Registro\n2.Selección de idioma\n3. Asignación de Rol\n4. Veterinaria\n5. Traducción e Interpretación\n6. Plaza Cívica\n7. Ciencias Sociales\n8. Ciencias\n9. VITAE\n10. Escola d'Enginyeria")


# MUERTE
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == -1)
def muerte(m):
    cid = m.chat.id
    text = m.text
    command_text(m)
    bot.send_message(cid, "Para resetear el bot, haz clic aquí: /start")


# MENU PRINCIPAL
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 0)
def main_menu(m):
    global asigRol, inReg, userStep
    cid = m.chat.id
    text = m.text
    inReg[cid] = False

    if text == "Acceder al registro 🍃" and regDone[cid] == False:  # REGISTRO INICIAL
        bot.send_message(cid,
                         "Las respuestas a estas preguntas nos ayudan a conocer mejor a los jugadores de UABlunt. Muchas gracias por tu tiempo. :)")
        time.sleep(1)
        inReg[cid] = True
        f[cid] = open('log' + str(m.chat.id) + 'REG.txt', 'w')
        f[cid].write("##########REGISTRO##########\n\n")
        f[cid].close()
        bot.send_message(cid, "¿Cuántos años tienes?", reply_markup=age_menu)
        userStep[cid] = 1
    elif text == "Modificar registro e iniciar partida 🍃" and regDone[cid] == True:  # REGISTRO INICIAL
        bot.send_message(cid, "Muchas gracias por actualizar tu información. :)")
        time.sleep(1)
        set_reg_bools(cid)
        inReg[cid] = True
        bot.send_message(cid, "¿Cuántos años tienes?", reply_markup=age_menu)
        userStep[cid] = 1

    elif text == "Seleccionar idioma 🌐":  # IDIOMA
        bot.send_message(cid, "Selección de idioma:", reply_markup=lang_menu)
        userStep[cid] = 2
    elif text == "Iniciar Partida 🍂":
        set_game_bools(cid)
        bot.send_message(cid, "¡Hora de aventuras!", reply_markup=boton_rol)
        userStep[cid] = 3
        asigRol[cid] = True
    else:
        command_text(m)


# SECUENCIA DE REGISTRO
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def registro(m):
    global age, gender, uab, weed, reg, regDone, inReg, asigRol, userStep
    cid = m.chat.id
    txt = m.text

    if txt in age_list and age[cid] == False:  # TEMP
        bot.send_message(cid, "¿Cuál es tu género?", reply_markup=gender_menu)
        age[cid] = True
    elif txt in gender_list and gender[cid] == False:
        bot.send_message(cid, "¿Eres estudiante, profesor, PAS, PDI o Alumni de la Universitat Autònoma de Barcelona?",
                         reply_markup=uab_menu)
        gender[cid] = True
    elif txt in uab_list and uab[cid] == False:
        bot.send_message(cid, "¿Consumes habitualmente la droga: el porro?", reply_markup=weed_menu)
        uab[cid] = True
    elif txt in weed_list and weed[cid] == False:
        # weed_menu.ReplyKeyboardRemove()

        if txt == 'Sí.' or txt == 'Prefiero no contestar. 🤷':
            bot.send_message(cid,
                             "El equipo de UABlunt no apoya el consumo de drogas. Si crees que puedes tener un problema, hay muchas personas dispuestas a ayudarte.\n\nVisita https://www.fad.es/",
                             reply_markup=heart)
        uab[cid] = True
        regDone[cid] = True

        time.sleep(2)
        bot.send_message(cid, "¡Gracias, " + str(m.chat.first_name) + ", ya puedes empezar tu aventura!",
                         reply_markup=boton_rol)
        set_game_bools(cid)
        inReg[cid] = False
        asigRol[cid] = True
        userStep[cid] = 3
    else:
        command_text(m)


# MENU IDIOMA
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2)
def idioma(m):
    cid = m.chat.id
    text = m.text
    if text != "Atrás" and text in lang_list:
        bot.send_message(cid, "Esta sección está actualmente en desarrollo. ¡Vuelve pronto!", reply_markup=lang_menu)
    elif text == "Atrás":  # ATRAS
        userStep[cid] = 0
        if regDone[cid] == False:
            bot.send_message(cid, "Has vuelto al menú principal", reply_markup=menu)
        else:
            bot.send_message(cid, "Has vuelto al menú principal", reply_markup=mid_menu)
    else:
        command_text(m)


# SECUENCIA DE ASIGNACIÓN DE ROL
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 3)
def asignarRol(m):
    sit1 = telebot.types.InlineKeyboardMarkup()
    sit1.row(telebot.types.InlineKeyboardButton('A', callback_data='1A'),
             telebot.types.InlineKeyboardButton('B', callback_data='1B'))
    sit2 = telebot.types.InlineKeyboardMarkup()
    sit2.row(telebot.types.InlineKeyboardButton('A', callback_data='2A'),
             telebot.types.InlineKeyboardButton('B', callback_data='2B'),
             telebot.types.InlineKeyboardButton('C', callback_data='2C'),
             telebot.types.InlineKeyboardButton('D', callback_data='2D'))
    sit3 = telebot.types.InlineKeyboardMarkup()
    sit3.row(telebot.types.InlineKeyboardButton('A', callback_data='3A'),
             telebot.types.InlineKeyboardButton('B', callback_data='3B'))

    cid = m.chat.id
    text = m.text

    global gameON, asigRol, boolAgresivo, boolCauto, boolFumeta, boolNeutro, boolSano, boolNoPrueba, boolPrueba, sit1bool, sit2bool, sit3bool, debugBool

    gameON[cid] = True
    command_text(m)

    if (sitShown[cid] == False and asigRol[cid] == True) or (debugBool[cid] == True):
        sitShown[cid] = True
        bot.send_message(cid, "zzzzz...zzzz…!!!", reply_markup=game_menu)
        time.sleep(1)
        bot.send_message(cid,
                         "Te despiertan las sirenas, te encuentras mareado pero consigues incorporarte.\n'¿Qué haces en la facultad de veterinaria a estas horas de la mañana?' -Oyes un grito a lo lejos:")
        time.sleep(2)
        bot.send_message(cid, "'¡Eh, tú! ¡Levántate, ahí no se puede estar!'")
        time.sleep(2)
        bot.send_message(cid,
                         '***Te levantas de inmediato, el guardia impone bastante, pero aún así le contestas: \n \n a) ¡A mí no me dé órdenes usted! (agresivo) \n b) De acuerdo, ya me voy, tranquilo... (cauto)',
                         reply_markup=sit1)
        while (sit1bool[cid] == False):
            pass
        time.sleep(2)
        bot.send_message(cid,
                         'Notas algo en el bolsillo, llevas un porro encima, pero mantienes la calma hasta que te alejas del guardia.')
        time.sleep(2)
        bot.send_message(cid,
                         '***¿Cómo ha llegado hasta ahí? ¿Sueles fumar? \n\n a)Sí, casi cada día, para aguantar la uni. (Fumeta)\nb) De vez en cuando, de fiesta con los amigos, que no hace daño. (Fumeta) \n c) He probado alguna vez, pero me da cosa. (Neutro) \n d) No. Eso está mal, los porros matan, por mucho que tenga uno en el bolsillo.\n(...¿Sano?)',
                         reply_markup=sit2)
        while (sit2bool[cid] == False):
            pass
        time.sleep(2)
        bot.send_message(cid,
                         '***¿Quieres probarlo? \n a) Claro, hay que probar la mercancía. \n b) Mejor no, que son las 10, hombre.',
                         reply_markup=sit3)
        while (sit3bool[cid] == False):
            pass
        asigRol[cid] = False  #####FIN ASIGNACIÓN DE ROL
        sitShown[cid] = False

        ##################################################################################################

        if boolAgresivo[cid] == True and boolFumeta[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura, que no teme a un guardia de seguridad ni a una muerte por sobredosis, de hecho te encanta fumar. En un alarde de cordura pensaste que quizás no era el momento de fumar... pero al final la presión social pudo incluso contigo, ¿no?",
                             reply_markup=boton_vet)
        elif boolAgresivo[cid] == True and boolNeutro[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura pero razonable, que no teme a un guardia de seguridad pero hasta cierto punto respeta el concepto de la drogadicción. En un alarde de cordura pensaste que quizás no era el momento de fumar... pero al final la presión social pudo incluso contigo, ¿no?",
                             reply_markup=boton_vet)
        elif boolAgresivo[cid] == True and boolSano[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura pero consecuente con tus actos, que no teme a un guardia de seguridad pero sabe bien que las drogas no son ninguna broma. Demostrando tus valores, eliges no fumarte el porro que había en tu bolsillo, pero al final te das cuenta de que si estaba ahí era por algo, ¿verdad, 'sanote'?",
                             reply_markup=boton_vet)
        elif boolAgresivo[cid] == True and boolFumeta[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura, que no teme a un guardia de seguridad ni a una muerte por sobredosis, de hecho te encanta fumar. Probablemente no haga falta decir que eres la clase de persona que si una mañana se despertase tirada en el césped y se encontrase un porro en el bolsillo se lo fumaría sin pensarlo dos veces (porque es lo que acaba de pasar)",
                             reply_markup=boton_vet)
        elif boolAgresivo[cid] == True and boolNeutro[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura pero razonable, que no teme a un guardia de seguridad pero hasta cierto punto respeta el concepto de la drogadicción. Sin embargo, cuando te despertaste en la hierba esta mañana no te apetecía mucho respetar nada.",
                             reply_markup=boton_vet)
        elif boolAgresivo[cid] == True and boolSano[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             '# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona dura pero consecuente con tus actos, que no teme a un guardia de seguridad pero sabe bien que las drogas no son ninguna broma. Demostrando tus "valors", eliges fumarte el porro que había en tu bolsillo.\n\n*Por supuesto, demuestras tu valor para elegir la opción sana en la segunda pregunta para después fumarte un porro sin pestañear. Mejor olvida eso de que eres consecuente.',
                             reply_markup=boton_vet)

        elif boolAgresivo[cid] == False and boolFumeta[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona capaz de mantener las formas incluso en las soluciones límite, pero cuando fumas te conviertes en todo lo contrario, así que es una pena que te guste tanto fumar. En un alarde de cordura pensaste que quizás no era el momento de fumar... pero al final la presión social pudo incluso contigo, ¿no?",
                             reply_markup=boton_vet)
        elif boolCauto[cid] == True and boolNeutro[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona razonable, que rara vez falta al respeto al tiempo que respeta el concepto de la drogadicción. En un alarde de cordura pensaste que quizás no era el momento de fumar... pero al final la presión social pudo incluso contigo, ¿no?",
                             reply_markup=boton_vet)
        elif boolCauto[cid] == True and boolSano[cid] == True and boolNoPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona cautelosa y casi perspicaz, que sabe comportarse y, sobre todo, sabe bien que las drogas no son ninguna broma. Demostrando tus valores, eliges no fumarte el porro que había en tu bolsillo, pero al final te das cuenta de que si estaba ahí era por algo, ¿verdad, 'sanote'?",
                             reply_markup=boton_vet)
        elif boolCauto[cid] == True and boolFumeta[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona capaz de mantener las formas incluso en las soluciones límite, pero cuando fumas te conviertes en todo lo contrario, así que es una pena que te guste tanto fumar. Es llamativo que pese a saber cuándo mantener la boca cerrada no hayas sido capaz de hacerlo con un porro delante.",
                             reply_markup=boton_vet)
        elif boolCauto[cid] == True and boolNeutro[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             "# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona razonable, que rara vez falta al respeto al tiempo que respeta el concepto de la drogadicción. Sin embargo, cuando te despertaste en la hierba esta mañana no te apetecía mucho respetar nada.",
                             reply_markup=boton_vet)
        elif boolCauto[cid] == True and boolSano[cid] == True and boolPrueba[cid] == True:
            bot.send_message(cid,
                             '# RESULTADOS DE LA ASIGNACIÓN DE ROL\n\nEres una persona cautelosa y casi perspicaz, que sabe comportarse y, sobre todo, sabe bien que las drogas no son ninguna broma. Demostrando tus "valors", eliges fumarte el porro que había en tu bolsillo.\n\n*Por supuesto, demuestras tu valor para elegir la opción sana en la segunda pregunta para después fumarte un porro sin pestañear. Mejor olvida eso de que eres perspicaz.',
                             reply_markup=boton_vet)

        ##################################################################################################

        # bot.send_message(cid, "#FIN DE LA ASIGNACIÓN DE ROL#", reply_markup=boton_vet)
        userStep[cid] = 4


# SECUENCIA DE FACULTAD VETERINARIA
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 4)
def facultadVeterinaria(m):
    sit4 = telebot.types.InlineKeyboardMarkup()
    sit4.row(telebot.types.InlineKeyboardButton('A', callback_data='4A'),
             telebot.types.InlineKeyboardButton('B', callback_data='4B'),
             telebot.types.InlineKeyboardButton('C', callback_data='4C'))

    cid = m.chat.id
    text = m.text

    global gameON, facVet, sit4bool
    facVet[cid] = True

    gameON[cid] = True
    command_text(m)

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid, 'Preguntas a la jirafa sobre las sirenas, qué está pasando.', reply_markup=game_menu)
        time.sleep(2)
        bot.send_message(cid,
                         'Te explica que ayer hubo un ataque informático a la red privada de la UAB, y que se han perdido todos los expedientes y notas.')
        time.sleep(2)
        bot.send_message(cid,
                         'Sorprendido, preguntas:\n a) ¿Se sabe quién ha sido? \n b) ¿Por eso hay tanta seguridad? \n c) ¿Unos munchies?',
                         reply_markup=sit4)
        while (sit4bool[cid] == False):
            pass
        time.sleep(2)
        bot.send_message(cid,
                         'Con esta información, accedes a la intranet de la Universidad y compruebas que efectivamente la página principal de la UAB muestra un mensaje:')
        time.sleep(2)
        bot.send_message(cid, '科学は助ける')
        time.sleep(2)
        bot.send_message(cid,
                         'No lo entiendes, y tampoco tienes conexión a internet, la zona UAB está completamente capada, pero se te ocurre quién podría traducirlo…')
        time.sleep(2)
        if boolMuerte[cid] == False:
            bot.send_message(cid, 'Te diriges a paso firme hacia la facultad de traducción e interpretación...',
                         reply_markup=boton_trad)
            userStep[cid] = 5
            sitShown[cid] = False


# SECUENCIA DE FACULTAD TRADUCCIÓN
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 5)
def facultadTraduccion(m):
    sit7 = telebot.types.InlineKeyboardMarkup()
    sit7.row(telebot.types.InlineKeyboardButton('A', callback_data='7A'),
             telebot.types.InlineKeyboardButton('B', callback_data='7B'),
             telebot.types.InlineKeyboardButton('C', callback_data='7C'),
             telebot.types.InlineKeyboardButton('D', callback_data='7D'))
    sit8 = telebot.types.InlineKeyboardMarkup()
    sit8.row(telebot.types.InlineKeyboardButton('A', callback_data='8A'),
             telebot.types.InlineKeyboardButton('B', callback_data='8B'),
             telebot.types.InlineKeyboardButton('C', callback_data='8C'),
             telebot.types.InlineKeyboardButton('D', callback_data='8D'))

    cid = m.chat.id
    text = m.text

    global gameON, facTrad, caladas, sit7bool, sit8bool
    facTrad[cid] = True

    gameON[cid] = True
    command_text(m)

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid, 'Caminas siguiendo las vías de FGC…y llegas a traducción e interpretación.',
                         reply_markup=game_menu)
        time.sleep(2)
        bot.send_message(cid,
                         'Todo el bioma cambia, y ahora parece como si hubieras viajado al pasado, al Japón feudal.')
        time.sleep(2)
        bot.send_message(cid, 'Escuchas unas hélices girar en la lejanía')
        time.sleep(2)
        bot.send_message(cid, 'zas, zas...')
        time.sleep(2)
        bot.send_message(cid, '¡Es Doraemon con su casquet volador!')
        doraemon = open('Doraemon.jpg', 'rb')
        bot.send_photo(cid, doraemon)
        time.sleep(1)
        bot.send_message(cid, '*Doraemon baja volando del cielo y se acerca a ti')
        time.sleep(1)
        if (caladas[cid] >= 6):
            bot.send_message(cid,
                             '"Hola amigo, ¿como te puedo ayudar?, suelo tener la solución a todos los problemas en mi bolsillo mágico" \na) Le pides un mapa de la universidad \nb)Un lazo amarillo \nc)Un casco romano \nd)Una pokéball vacía',
                             reply_markup=sit7)
            while (sit7bool[cid] == False):
                pass
            bot.send_message(cid,
                             "Se ha añadido un objeto a tu inventario. Puedes acceder a él a través de la opción 'STATS 📖'")
        else:
            bot.send_message(cid,
                             '"No vas lo suficientemente fumando para poder comunicarte conmigo, adiós." - Doraemon vuela hacia el cielo alejándose de ti')
            time.sleep(2)
            bot.send_message(cid, 'Esto te recuerda que quieres darle una calada al porro')
        time.sleep(2)
        bot.send_message(cid,
                         '"Esto ha sido muy raro", piensas. Aunque recuerdas que vas fumado y le das otra calada al porro')
        caladas[cid] = caladas[cid] + 1
        if caladas[cid] == 20:
            bot.send_message(cid,
                             "⚠️ Durante unos segundos todo se vuelve mucho, mucho más oscuro, pero recobras la conciencia. Ten cuidado o puede que no llegues al final de esta historia.")
        if (caladas[cid] >= 25):
            bot.send_message(cid,
                             "Tus ojos empiezan a cerrarse, has fumado demasiado... Empiezas a tener ganas de vomitar, tantas caladas son demasiadas...")
            time.sleep(3)
            bot.send_message(cid, "MUERES por sobredosis. FIN DE LA PARTIDA", reply_markup=boton_muerte)
            userStep[cid] = -1
            boolMuerte[cid] = True
        else:
            time.sleep(2)
            bot.send_message(cid, "Sigues caminando, y alerta por lo que pueda pasar.")
            time.sleep(2)
            bot.send_message(cid, "Un Samurái se cruza en tu camino.")
            samurai = open('SamuraiReeves.jpg', 'rb')
            bot.send_photo(cid, samurai)
            time.sleep(2)
            bot.send_message(cid,
                             '"Buenos días, hace una mañana espléndida. ¿Dónde está tu katana? Un samurái no es nadie sin su arma sagrada" \na) Pides ayuda, de manera respetuosa, haciéndole una reverencia. \nb) Pasas del samurái. \nc) Le pides que te traduzca el texto. \nd)Le intentas robar la katana.',
                             reply_markup=sit8)
            while (sit8bool[cid] == False):
                pass
            if boolMuerte[cid] == False:
                bot.send_message(cid, 'Caminas hacia la Geisha y le preguntas sobre el texto')
                time.sleep(2)
                bot.send_message(cid, '“Science will help”')
                time.sleep(2)
                bot.send_message(cid, 'Lo tienes, ¡debes dirigirte a la facultad de ciencias!')
                time.sleep(2)
                bot.send_message(cid, '...¿Y eso dónde estaba?')
                time.sleep(2)
                if (objeto1[cid] != 1):
                    bot.send_message(cid, 'Piensas que ahora un mapa te vendría de perlas')
                    time.sleep(2)
                    if boolMuerte[cid] == False:
                        userStep[cid] = 6
                        sitShown[cid] = False
                        bot.send_message(cid, 'Recuerdas el camino hacia Plaza Cívica y decides dirigirte ahí',
                                         reply_markup=boton_plaza)

                elif (objeto1 == 1):
                    bot.send_message(cid, 'Por suerte, tienes el mapa del Eix Central que te dio Doraemon')
                    time.sleep(2)
                    if boolMuerte[cid] == False:
                        userStep[cid] = 8
                        sitShown[cid] = False
                        bot.send_message(cid, 'Miras el mapa y te diriges directamente a ciencias.',
                                         reply_markup=boton_ciencia)


# SECUENCIA DE PLAZA CÍVICA
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 6)
def plazaCivica(m):
    sit10 = telebot.types.InlineKeyboardMarkup()
    sit10.row(telebot.types.InlineKeyboardButton('A', callback_data='10A'),
              telebot.types.InlineKeyboardButton('B', callback_data='10B'),
              telebot.types.InlineKeyboardButton('C', callback_data='10C'),
              telebot.types.InlineKeyboardButton('D', callback_data='10D'))

    cid = m.chat.id
    text = m.text

    global gameON, plCivica, sit10bool
    plCivica[cid] = True

    command_text(m)
    gameON[cid] = True

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid,
                         'Después del trauma en Traducción, la cosa no mejora. Llegas al lugar más transitado de la UAB, plaza cívica. Te encuentras con una manifestación, nada fuera de lo normal, pero lo que no te esperas es ver a Willyrex.',
                         reply_markup=game_menu)
        time.sleep(2)
        willy = open('willyrex.jpg', 'rb')
        bot.send_photo(cid, willy)
        time.sleep(3)
        bot.send_message(cid, '“¡Hey buenas a todos! Aquí Willyrex comentando…”')
        time.sleep(2)
        bot.send_message(cid,
                         'Le interrumpes porque ves que va para largo y le haces saber que: \na) Eres su fan desde hace mucho tiempo y te encanta el Fortnite. \nb) Eres su fan desde hace mucho tiempo y te encanta el Minecraft. \nc) No sabes quién es y le pides que se calle. \nd) Le detestas porque pensabas que Wigetta era real.',
                         reply_markup=sit10)
        while (sit10bool[cid] == False):
            pass
        if boolMuerte[cid] == False:
            time.sleep(2)
            bot.send_message(cid,
                             'Sigues caminando como si no hubiera pasado nada...llegas a la facultad de Ciencias Sociales.',
                             reply_markup=boton_social)
            if boolMuerte[cid] == False:
                sitShown[cid] = False
                userStep[cid] = 7


# SECUENCIA DE CIENCIAS SOCIALES
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 7)
def cienciasSociales(m):
    sit12 = telebot.types.InlineKeyboardMarkup()
    sit12.row(telebot.types.InlineKeyboardButton('A', callback_data='12A'),
              telebot.types.InlineKeyboardButton('B', callback_data='12B'),
              telebot.types.InlineKeyboardButton('C', callback_data='12C'),
              telebot.types.InlineKeyboardButton('D', callback_data='12D'))

    cid = m.chat.id
    text = m.text

    global gameON, facSoc, sit12bool
    facSoc[cid] = True

    gameON[cid] = True
    command_text(m)

    sit12bool[cid] = False

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid,
                         'Aquí la gente no parece tan rara, gente fumada como tú, lo que te recuerda que deberías dar una calada.',
                         reply_markup=game_menu)
        time.sleep(2)
        bot.send_message(cid,
                         'Pero entras en la zona de historia y ciencias políticas y empiezas a sufrir...te asaltan líderes políticos históricos.')
        time.sleep(2)
        if (objeto1[cid] == 2):
            bot.send_message(cid, 'Aparece el fantasma jedi de Oriol Junqueras y te ayuda a escapar.')
            junqueras = open('junqueras.jpg', 'rb')
            bot.send_photo(cid, junqueras)
            time.sleep(2)
            bot.send_message(cid, 'En lugar seguro, Oriol te transmite un mensaje:')
            time.sleep(1)
            bot.send_message(cid,
                             "'_Veig que portes la meva insígnia! Per trobar la solució, utilitza l'enginy, o millor dit, ves on hi hagi molt d'això_'",
                             parse_mode="Markdown")
            time.sleep(2)
            if boolMuerte[cid] == False:
                bot.send_message(cid,
                             'Gracias a esto, sabes que debes dirigirte a ingeniería directamente. ¡¡¡Estás en la recta final!!!',
                             reply_markup=boton_eng)

                sitShown[cid] = False
                userStep[cid] = 10
        else:
            time.sleep(2)
            bot.send_message(cid, 'Te acaban pillando los políticos. Te llenan de pins de sus campañas electorales.')
            time.sleep(2)
            bot.send_message(cid, '💜🎗🌹🍏🍊🐂🦅')
            time.sleep(1)
            bot.send_message(cid, 'Como puedes, sales de allí, pero te encuentras a Napoleón Bonaparte.')
            time.sleep(2)
            bot.send_message(cid, 'Aunque mide metro y medio, va a caballo y te apunta con su espada, te pregunta:')
            time.sleep(2)
            bot.send_message(cid,
                             '“¿Donde vas tan rápido?” \na)Me dirijo hacia la facultad de ciencias, ¿me deja pasar?. \nb)Aparta, gabacho! \nc)Le faltas al respeto llamándolo tapón. \nd)¡Por el altísimo! Pero si es el mismísimo Napoleón Bonaparte. El grandísimo Emperador de Francia. Sería usted tan amable de concederme paso hacia las lejanas tierras de la facultad de ciencias? Se me ha hecho saber que cruza por su territorio.',
                             reply_markup=sit12)
            while (sit12bool[cid] == False):
                pass
            if(boolMuerte[cid] == False):
                time.sleep(2)
                bot.send_message(cid,
                                 'Tras la odisea de Ciencias Sociales, crees que puedes con todo, pero te recomendamos que des una calada, queda lo más duro.',
                                 reply_markup=boton_ciencia)
                sitShown[cid] = False
                userStep[cid] = 8


# SECUENCIA DE CIENCIAS
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 8)
def facultadCiencias(m):
    dialog = telebot.types.InlineKeyboardMarkup()
    dialog.row(telebot.types.InlineKeyboardButton('Contestar', callback_data='dialogo'))
    sit13 = telebot.types.InlineKeyboardMarkup()
    sit13.row(telebot.types.InlineKeyboardButton('A', callback_data='13A'),
              telebot.types.InlineKeyboardButton('B', callback_data='13B'),
              telebot.types.InlineKeyboardButton('C', callback_data='13C'),
              telebot.types.InlineKeyboardButton('D', callback_data='13D'))
    sit17 = telebot.types.InlineKeyboardMarkup()
    sit17.row(telebot.types.InlineKeyboardButton('A', callback_data='17A'),
              telebot.types.InlineKeyboardButton('B', callback_data='17B'),
              telebot.types.InlineKeyboardButton('C', callback_data='17C'))

    cid = m.chat.id
    text = m.text

    global gameON, facCien, dialogo, sit13bool, sit17bool
    facCien[cid] = True

    gameON[cid] = True
    command_text(m)

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid,
                         'Has llegado a la facultad de ciencias. La verdad es que tienes un aspecto deplorable y tu tez es grisácea, das bastante pena.',
                         reply_markup=game_menu)
        time.sleep(2)
        bot.send_message(cid, 'No te encuentras para nada bien.')
        time.sleep(2)
        bot.send_message(cid, 'No te queda otra que dar una calada.')
        caladas[cid] = caladas[cid] + 1
        if caladas[cid] == 20:
            bot.send_message(cid,
                             "⚠️ Durante unos segundos todo se vuelve mucho, mucho más oscuro, pero recobras la conciencia. Ten cuidado o puede que no llegues al final de esta historia.")
        if (caladas[cid] >= 25):
            bot.send_message(cid,
                             "Tus ojos empiezan a cerrarse, has fumado demasiado... Empiezas a tener ganas de vomitar, tantas caladas son demasiadas...")
            time.sleep(3)
            bot.send_message(cid, "MUERES por sobredosis. FIN DE LA PARTIDA", reply_markup=boton_muerte)
            userStep[cid] = -1
            boolMuerte[cid] = True
        else:

            bot.send_message(cid,
                             'Sientes como el estómago y los intestinos se te remueven. Decides preguntarle a alguien direcciones para el lavabo.')
            time.sleep(2)
            bot.send_message(cid, 'Te acercas a un hombre con el pelo blanco y un poco alocado. Le tocas el hombro:')
            time.sleep(2)
            bot.send_message(cid,
                             'Le dices: -"Buenas, señor. La verdad es que no me encuentro muy bien, ¿podría decirme dónde está el lavabo? Necesito ir con urgencia."')
            time.sleep(2)
            bot.send_message(cid, 'El hombre se gira, resulta ser Albert Einstein:')
            time.sleep(2)
            einstein = open('einstein.jpg', 'rb')
            bot.send_photo(cid, einstein)

            time.sleep(2)

            bot.send_message(cid,
                             'Buenas, joven. Con que necesita ir al aseo, ¡situación perfecta para que escuche mi acertijo!',
                             reply_markup=dialog)
            while (dialogo[cid] == False):
                pass
            dialogo[cid] = False
            bot.send_message(cid,
                             'Contestas: -"Uff, no tengo tiempo para esto. Me encuentro muy mal, de verdad, le suplico que me diga dónde está."')
            time.sleep(2)
            bot.send_message(cid,
                             'Lo siento, joven, pero si quiere saber la información que poseo deberá seguir mis normas.',
                             reply_markup=dialog)
            while (dialogo[cid] == False):
                pass
            dialogo[cid] = False
            bot.send_message(cid, 'Contestas: -"Agh, adelante."')
            time.sleep(2)
            bot.send_message(cid, 'Tenemos cinco casas de colores diferentes. En cada una de ellas…', reply_markup=dialog)
            while (dialogo[cid] == False):
                pass
            dialogo[cid] = False
            bot.send_message(cid,
                             'Contestas: -"Ya ya, el dueño del pez, ¿no tiene alguno más sencillo y que sea más corto? Creo que lo voy a echar todo."')
            time.sleep(2)
            bot.send_message(cid,
                             'Veo que es alguien impaciente. Le pondré uno facilito. Seguro que el 98% de la población sería capaz de responder correctamente: “Puede devorar todas las cosas: plantas, bestias, flores y aves. Roe el hierro y muerde acero, mata reyes, arruina ciudades y puede derribar las altas montañas.” \na)Ácido fluoroantimónico. \nb) No tengo ni idea. \nc) El tiempo. \nd)¿De verdad que no me deja ir al lavabo?',
                             reply_markup=sit13)
            while (sit13bool[cid] == False):
                pass
            if boolMuerte[cid] == False:
                bot.send_message(cid,
                                 'Te diriges corriendo hacia el lavabo. Entras en un cubículo y te pones de rodillas. Echas toda la pota en la taza')
                time.sleep(2)
                bot.send_message(cid, 'Cuando acabas tiras de la cadena y te sientas un momento. Le das otra calada al spliff.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Vas a lavarte la cara y encuentras un extraño hombre hablando de forma muy acaramelada a una paloma:')
                time.sleep(2)
                bot.send_message(cid,
                                 'T: -"¡Mi amada! Siempre hay alguien que antepone el beneficio propio aunque eso les cueste su integridad. Ya lo sabes. ¿Sospechas que todo lo que está pasando en la universidad está relacionado con algún ingeniero? ¿Estás segura? Sería la tercera vez que nos vemos afectados por algo así."')
                time.sleep(3)
                bot.send_message(cid, 'Le interrumpes y preguntas:', reply_markup=dialog)
                while (dialogo[cid] == False):
                    pass
                dialogo[cid] = False
                bot.send_message(cid, 'Le preguntas: -"¿Qué hace con una paloma?"')
                time.sleep(2)
                bot.send_message(cid, 'T. -¿Paloma? Un poco de respeto, está dirigiéndose a la señora Tesla.')
                time.sleep(2)
                bot.send_message(cid, '*No sabes dónde meterte y das una calada muy profunda a la bengala*',
                                 reply_markup=dialog)
                while (dialogo[cid] == False):
                    pass
                dialogo[cid] = False
                bot.send_message(cid, 'Contestas: -"Ya, claro… Siento la confusión."')
                time.sleep(2)
                bot.send_message(cid, 'T: -"No pasa nada. ¿Necesita algo?, estaba manteniendo una conversación privada.", te dice',
                                 reply_markup=dialog)
                while (dialogo[cid] == False):
                    pass
                dialogo[cid] = False
                bot.send_message(cid, 'Contestas: -"Me gustaría conectarme a una red Wi-Fi ¿Sabe de algún lugar donde funcione?"')
                time.sleep(2)
                bot.send_message(cid,
                                 'T: -No sé de qué me estás hablando. Pero tal vez el hombre calvo ese que siempre viste igual, de negro y un tejano azul pueda ayudarte.',
                                 reply_markup=dialog)
                while (dialogo[cid] == False):
                    pass
                dialogo[cid] = False
                bot.send_message(cid, 'Contestas: -"Gracias. Que le vaya bien a usted y su… esposa."')
                time.sleep(2)
                bot.send_message(cid, 'T: -"Gracias y… vaya al hospital. Eso es una paloma."')
                time.sleep(2)
                bot.send_message(cid,
                                 'Te mira sin mucho afecto y sales en busca del hombre de camisa negra y tejano azul. Sales del lavabo y oyes a dos hombres discutiendo:')
                time.sleep(2)
                bot.send_message(cid, 'S: -"¿¡Marte!? ¿Y qué le pasa a la Tierra, tanto os la habéis cargado?"')
                time.sleep(2)
                bot.send_message(cid, 'E: -"Hay que expandir, colonizar el espacio."')
                time.sleep(2)
                jobsmusk = open('jobsvsmusk.jpg', 'rb')
                bot.send_photo(cid, jobsmusk)
                bot.send_message(cid, '*Discute el hombre que buscas con otro trajeado, lleva un pin que pone SpaceX.',
                                 reply_markup=dialog)
                while (dialogo[cid] == False):
                    pass
                dialogo[cid] = False
                bot.send_message(cid,
                                 'Interrumpes y dices: -"Perdonen, me han dicho que usted podría ayudarme a encontrar una red WIFI."')
                time.sleep(3)
                bot.send_message(cid,
                                 'S: -"Claro que puedo ayudarte. Soy Jobs, encantado. ¿Qué necesitas exactamente? Tengo de todo. ¿Te gustan las manzanas?"')
                time.sleep(3)
                bot.send_message(cid,
                                 'E: -"Jajaja, este hombre se cree que puede venderte cualquier cosa. Soy Elon Musk. Yo sí que te puedo ser de provecho. Si inviertes en mi empresa puedo darte todas las redes WIFI que desees, en un plazo de cinco años."')
                time.sleep(3.5)
                bot.send_message(cid,
                                 'Contestas: \na) Gracias, pero no quiero un iPhone, estoy contento con mi teléfono Android, tampoco quiero pagar mil euros por la base de un televisor. Y no me interesa comprar un lanzallamas, o enviar mi coche al espacio. \nb) ¿Dónde puedo conectarme a esa red? \nc) Os lo tenéis bien creído, eh.',
                                 reply_markup=sit17)
                while (sit17bool[cid] == False):
                    pass

                if boolMuerte[cid] == False:
                    time.sleep(2)
                    bot.send_message(cid,
                                     'Tomas rumbo hacia la Escuela de Ingeniería. Pero tienes que atravesar la peligrosa zona de la Escuela Vitae, en el SAF',
                                     reply_markup=boton_vitae)
                    userStep[cid] = 9
                    sitShown[cid] = False


# SECUENCIA DE VITAE
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 9)
def escuelaVitae(m):
    sit21 = telebot.types.InlineKeyboardMarkup()
    sit21.row(telebot.types.InlineKeyboardButton('A', callback_data='21A'),
              telebot.types.InlineKeyboardButton('B', callback_data='21B'),
              telebot.types.InlineKeyboardButton('C', callback_data='21C'),
              telebot.types.InlineKeyboardButton('D', callback_data='21D'))

    cid = m.chat.id
    text = m.text

    global gameON, facSoc, sit21bool
    escVitae[cid] = True

    gameON[cid] = True
    command_text(m)
    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid,
                         'Estás delante de la Escuela Vitae. Te cruzas con un grupo de cinco personas que van vestidos como soldados romanos y que van borrachos como cubas.',
                         reply_markup=game_menu)
        time.sleep(2)
        romanos = open('romanos.jpg', 'rb')
        bot.send_photo(cid, romanos)
        time.sleep(2)
        bot.send_message(cid, '🍺 🍻 🍹')
        time.sleep(2)
        if (objeto1[cid] == 3):
            if boolMuerte[cid] == False:
                sitShown[cid] = False
                userStep[cid] = 10
                bot.send_message(cid,
                                 'Los soldados romanos te miran, y levantan la barbilla en gesto de que han visto tu casco romano y te saludan levantando sus jarras llenas de vino y cerveza tirando gran parte al suelo.',
                                 reply_markup=boton_eng)

        else:
            bot.send_message(cid,
                             'Los soldados te miran uno tirando la mitad del contenido de su jarra al suelo grita:')
            time.sleep(2)
            bot.send_message(cid,
                             '¡Eh, tú! ¡Sí, tú! Este no es tu territorio. ¿Con qué permiso estás cruzando? ¿Quién te crees que eres?')
            time.sleep(2)
            bot.send_message(cid,
                             'a) ¡Por Osiris! ¡Creo que nos conocemos! ¿Puede ser que alguna vez hayamos disputado una partida a lanzar un balón a un cesto? \nb) Borracho, aparta de mi camino. No quieres problemas así que no me toques las narices. \nc) Buen día y buena ventura, compañeros. Me dirijo a la zona de la facultad de ingeniería. Según la información que poseo el único camino posible para llegar es siguiendo este paso. \nd) Me dirijo por este paso a la facultad de ingeniería. Ahora que tienes suficiente información, métete en tus asuntos.',
                             reply_markup=sit21)
            while (sit21bool[cid] == False):
                pass
            if boolMuerte[cid] == False:
                bot.send_message(cid,
                                 'Los soldados romanos te miran, y levantan la barbilla en gesto de que te han visto y te saludan levantando sus jarras llenas de vino y cerveza tirando gran parte al suelo.',
                                 reply_markup=boton_eng)
                sitShown[cid] = False
                userStep[cid] = 10


# SECUENCIA DE ENGINYERIA
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 10)
def facultadEnginyeria(m):
    dialog = telebot.types.InlineKeyboardMarkup()
    dialog.row(telebot.types.InlineKeyboardButton('Contestar', callback_data='dialogo'))
    sit23 = telebot.types.InlineKeyboardMarkup()
    sit23.row(telebot.types.InlineKeyboardButton('A', callback_data='23A'),
              telebot.types.InlineKeyboardButton('B', callback_data='23B'),
              telebot.types.InlineKeyboardButton('C', callback_data='23C'),
              telebot.types.InlineKeyboardButton('D', callback_data='23D'))
    sit24 = telebot.types.InlineKeyboardMarkup()
    sit24.row(telebot.types.InlineKeyboardButton('A', callback_data='24A'),
              telebot.types.InlineKeyboardButton('B', callback_data='24B'),
              telebot.types.InlineKeyboardButton('C', callback_data='24C'),
              telebot.types.InlineKeyboardButton('D', callback_data='24D'),
              telebot.types.InlineKeyboardButton('E', callback_data='24E'))
    sit28 = telebot.types.InlineKeyboardMarkup()
    sit28.row(telebot.types.InlineKeyboardButton('A', callback_data='28A'),
              telebot.types.InlineKeyboardButton('B', callback_data='28B'),
              telebot.types.InlineKeyboardButton('C', callback_data='28C'),
              telebot.types.InlineKeyboardButton('D', callback_data='28D'))
    sit29 = telebot.types.InlineKeyboardMarkup()
    sit29.row(telebot.types.InlineKeyboardButton('Parar la transferencia de datos, y devolverlos a la universidad.',
                                                 callback_data='29A'))
    sit29.row(telebot.types.InlineKeyboardButton('Borrar los datos y cobrar el dinero de la Pompeu Fabra.',
                                                 callback_data='29B'))

    cid = m.chat.id
    text = m.text

    global gameON, facCien, dialogo, sit22bool, sit23bool, objeto1, objeto2, objeto3
    facCien[cid] = True

    gameON[cid] = True
    command_text(m)

    if (sitShown[cid] == False):
        sitShown[cid] = True
        bot.send_message(cid,
                         'Sientes que has llegado muy lejos, pero aún queda lo más difícil...',
                         reply_markup=game_menu)
        time.sleep(2)
        bot.send_message(cid,
                         'Justo delante de la Escuela hay un grupo de gente. Dos de ellos van vestidos con chalecos y gorras y le están gritando a dos personas disfrazadas. Parece que se están enfrentando.')
        time.sleep(2)
        bot.send_message(cid, 'Necesitas despejarte. Le das un par de caladas muy profundas al petráncano.')
        caladas[cid] = caladas[cid] + 2
        time.sleep(2)
        bot.send_message(cid,
                         '-¡Adelante, Pikachu! ¡Utiliza impactrueno!\n-¡Oh, Dios! Parece que ha sido muy efectivo. ¡Charmander! Usa ascuas.')
        time.sleep(3)
        bot.send_message(cid,
                         'Decides ignorar a esos dos chavales disfrazados de Pokémon y te diriges a la puerta de la facultad para entrar. Se te ponen delante un hombre y una mujer:')
        time.sleep(3)
        bot.send_message(cid,
                         '-¿Dónde crees que vas tan rápido?\n-¿Acaso tienes una entrada?\n-¿O dinero para pagarla?')
        time.sleep(3)
        bot.send_message(cid, 'Sacas el porro y se lo ofreces:', reply_markup=dialog)
        while (dialogo[cid] == False):
            pass
        dialogo[cid] = False
        bot.send_message(cid, 'Contestas: "Aquí tengo mi entrada."')
        time.sleep(2)
        bot.send_message(cid, '-No nos ofrezcas alucinógenos.')
        time.sleep(1)
        bot.send_message(cid, '-No nos gustan las sustancias psicotrópicas.')
        time.sleep(1)
        bot.send_message(cid, '-Consigue una entrada…')
        time.sleep(1)
        bot.send_message(cid, '-...o dinero para ella…')
        time.sleep(1)
        bot.send_message(cid, '-...y te dejaremos entrar.')
        time.sleep(3)
        if (objeto2[cid] != 1):
            bot.send_message(cid,
                             'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos como Naruto.\nc)Los ingenieros vestidos como Dragon Ball.\nd)El ingeniero rapero.',
                             reply_markup=sit23)
            while (sit23bool[cid] == False):
                pass

        elif objeto2[cid] == 1:
            bot.send_message(cid,
                             'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos como Naruto.\nc)Los ingenieros vestidos como Dragon Ball.\nd)El ingeniero rapero.\ne)Lanzar la granada del Fornite',
                             reply_markup=sit24)
            while (sit24bool[cid] == False):
                pass

        if boolMuerte[cid] == False:
            if (objeto1[cid] == 5):  # Tarjeta Misteriosa

                bot.send_message(cid,
                                 'Lees la impresión que hay sobre la tarjeta y te diriges a la espina Q5, la de los laboratorios. La utilizas para entrar en uno de ellos y encuentras uno de los ordenadores encendidos.',
                                 reply_markup=game_menu)
                bot.send_message(cid,
                                 'Abres la consola de comandos del ordenador y puedes deducir que ha habido mucho tráfico de información hacia una IP de uno de los ordenadores que hay en la facultad.\n\nParece que el ladrón de los datos de los alumnos podría ser algún profesor...')
                bot.send_message(cid,
                                 'Encuentras una llave con una línea grabada, se puede leer: QC/1024. Todo esto es muy intenso, sacas la chimichanga y le das una aspirada.')
                caladas[cid] = caladas[cid] + 1
                objeto3[cid] = list_objetos_jordi[1]

            bot.send_message(cid, 'Parece que todo está un poco abandonado.', reply_markup=game_menu)
            time.sleep(2)
            bot.send_message(cid,
                             'Todo está vacío y a oscuras, la única zona medianamente iluminada es la espina QC, así que lo mejor que puedes hacer es visitar sus diferentes plantas.')
            time.sleep(2)
            bot.send_message(cid, '¿Dónde vas? \na) QC/0000 \nb) QC/1000 \nc) QC/2000 \nd) QC/3000', reply_markup=sit28)
            while(sit28bool[cid] == False):
                pass
            time.sleep(2)
            if boolMuerte[cid] == False:
                if objeto3[cid] == 1:
                    bot.send_message(cid,
                                     'Abres la puerta con la tarjeta que encontraste en el laboratorio y embistes al hombre al que escuchabas hablar.',
                                     reply_markup=game_menu)
                    bot.send_message(cid, 'Os disponéis a combatir. Como le has pillado por sorpresa tienes ventaja.')

                elif objeto2[cid] == 2:
                    bot.send_message(cid, 'Sacas el pico del minecraft y empiezas a golpear la puerta.', reply_markup=game_menu)
                    time.sleep(2)
                    bot.send_message(cid,
                                     'Al tercer golpe el pomo se cae y la puerta se abre, pero el hombre que hay en el interior se ha percatado de tu presencia, evidentemente.')
                    time.sleep(2)
                    bot.send_message(cid, 'Pero le has pillado por sorpresa.')
                    time.sleep(2)
                    bot.send_message(cid, 'El hombre: -"¿Qué haces aquí?"')
                    time.sleep(2)
                    bot.send_message(cid,
                                     'Contestas: "¿Qué ha pasado con los datos de los alumnos? He encontrado pruebas que apuntan que hay muchísimo tráfico de información a través de una IP de por aquí. Y eres el único que está dentro de la facultad."')
                    time.sleep(3)
                    bot.send_message(cid, 'El hombre: -"Aparte de ti. No te daré esa información así como así."')
                    time.sleep(2)
                    bot.send_message(cid, '*Os disponéis a combatir.*', parse_mode = "Markdown")
                else:
                    bot.send_message(cid,
                                     'Llamas a la puerta. El hombre que hay en el interior se ha percatado de tu presencia. Evidentemente, se acerca a la puerta y la abre. Te recibe y te invita a pasar.',
                                     reply_markup=game_menu)
                    bot.send_message(cid, 'El hombre: -¿Qué haces aquí?')
                    time.sleep(2)
                    bot.send_message(cid,
                                     'Contestas: "¿Qué ha pasado con los datos de los alumnos? He encontrado pruebas que apuntan que hay muchísimo tráfico de información a través de una IP de por aquí. Y eres el único que está dentro de la facultad."')
                    time.sleep(3)
                    bot.send_message(cid, 'El hombre: Aparte de ti. No te daré esa información así como así.')
                    time.sleep(2)
                    bot.send_message(cid, 'Os disponéis a combatir.')
                if boolMuerte[cid] == False:
                    peleaEmojis[cid] = True
                    time.sleep(2)
                    if objeto3[cid] == 1:
                        bot.send_message(cid,
                                         'Aprovechándote de tu ventaja logras reducirlo, pero se zafa fácilmente cuando te dice todo lo que sabe...')
                    else:
                        bot.send_message(cid, '💥💥💥💥')
                        time.sleep(1)
                        bot.send_message(cid, '🔥🔥🔥🔥')
                        time.sleep(1)
                        bot.send_message(cid, '💥💥💥💥')
                        time.sleep(1)
                        bot.send_message(cid, '🔥🔥🔥🔥')
                        time.sleep(1)
                        bot.send_message(cid, '💥💥💥💥')
                        time.sleep(1)
                        bot.send_message(cid, '🔥🔥🔥🔥')
                        time.sleep(1)
                        bot.send_message(cid, '💥💥💥💥')
                        time.sleep(1)
                        bot.send_message(cid, '🔥🔥🔥🔥')
                        time.sleep(1)
                        bot.send_message(cid, '💥💥💥💥')
                        time.sleep(1)
                        bot.send_message(cid, '🔥🔥🔥🔥')
                        time.sleep(1)
                        bot.send_message(cid, '💀💀💀💀')
                        time.sleep(1)

                        if objeto2[cid] == 2:
                            bot.send_message(cid,
                                             'Tras destrozar todo el despacho logras alcanzar tu pico de Minecraft, que había quedado tirado en el suelo. Te dispones a asestar tu golpe final, pero cambias de opinión cuando el hombre te dice todo lo que sabe...')
                            time.sleep(3)
                        else:
                            bot.send_message(cid,
                                             'Tras destrozar todo el despacho, acabas tirado en el suelo, a solo un puñetazo de que toda esta aventura haya sido en vano.')
                            time.sleep(2)
                            bot.send_message(cid,
                                             'El hombre: Si fueras de Valladolid quizá hubieras tenido alguna oportunidad.')
                            time.sleep(2)
                            bot.send_message(cid,
                                             'El hombre: Ahora que estás más tranquilo, te diré la verdad sobre lo ocurrido...')

                    bot.send_message(cid,
                                     'El hombre: Has de saber que fuiste tú el que me pidió que no te dijera nada sobre esto.')
                    time.sleep(2)
                    bot.send_message(cid, 'Contestas: "¿Que yo te pedí qué? ¿De qué hablas?"')
                    time.sleep(2)
                    bot.send_message(cid, '...')
                    time.sleep(4)
                    bot.send_message(cid,
                                     'El hombre: Los de la Universitat Pompeu Fabra querían sacar a la UAB del juego. Querían subir en el ránking.')
                    time.sleep(4)
                    bot.send_message(cid,
                                     'El hombre: Te pidieron que hicieras algo que realmente hiciera daño a toda la UAB, ellos te compensarían con acabar la carrera allí de manera gratuita y te pagarían con creces. ')
                    time.sleep(4)
                    bot.send_message(cid,
                                     'El hombre: Me pediste que te ayudara a cambio de darme algo de dinero por adelantado... Terminamos de lanzar el ataque justo antes de que me dijeras que ibas a intentar olvidar todo lo que acababa de pasar como fuera para no levantar sospechas, al menos hasta cobrar el dinero.')
                    time.sleep(6)
                    bot.send_message(cid,
                                     'El hombre: Veo que funcionó... Incluso te has olvidado de tu viejo amigo y profesor Jordi Bertrand')
                    time.sleep(3)
                    bot.send_message(cid,
                                     'Jordi: La información de la UAB está almacenada en varios ordenadores de la espina Q5, aún podrías pararlo si quisieras... La elección está en tus manos.')
                    time.sleep(3)
                    bot.send_message(cid, '*De repente, recuerdas todo lo ocurrido hace menos de 24 horas*')
                    time.sleep(2)
                    bot.send_message(cid, 'Solo ahora vuelves en ti y te das cuenta de que solo tienes dos opciones...',
                                     reply_markup=sit29)

# DESARROLLO DE LAS INLINE QUERIES DEL JUEGO (SITUACIONES MULTIRESPUESTA)
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    global gameON, caladas, sit1bool, sit2bool, sit3bool, sit4bool, sit5bool, sit6bool, sit7bool, sit8bool, sit9bool, sit10bool, sit11bool, sit12bool, sit13bool
    print("###Callback Recibido")

    dialog = telebot.types.InlineKeyboardMarkup()
    dialog.row(telebot.types.InlineKeyboardButton('Contestar', callback_data='dialogo'))

    paradise = telebot.types.InlineKeyboardMarkup()
    paradise.row(telebot.types.InlineKeyboardButton('Canta "Paradise" con Willyrex',
                                                    url="https://www.youtube.com/watch?v=hg0KPDrqlBQ"))

    ubisunt_boton = telebot.types.InlineKeyboardMarkup()
    ubisunt_boton.row(telebot.types.InlineKeyboardButton('Sigue escuchando "Dónde Están"',
                                                         url="https://www.youtube.com/watch?v=aJTczAj_JhM"))

    dom_boton = telebot.types.InlineKeyboardMarkup()
    dom_boton.row(telebot.types.InlineKeyboardButton('Seguir a DOM130🎶 en Spotify',
                                                     url='https://open.spotify.com/artist/10t1i6yzv4PnwHy5M7Vsiu'))

    sit5 = telebot.types.InlineKeyboardMarkup()
    sit5.row(telebot.types.InlineKeyboardButton('A', callback_data='5A'))
    sit6 = telebot.types.InlineKeyboardMarkup()
    sit6.row(telebot.types.InlineKeyboardButton('A', callback_data='6A'),
             telebot.types.InlineKeyboardButton('B', callback_data='6B'))
    sit9 = telebot.types.InlineKeyboardMarkup()
    sit9.row(telebot.types.InlineKeyboardButton('A', callback_data='9A'))
    sit11 = telebot.types.InlineKeyboardMarkup()
    sit11.row(telebot.types.InlineKeyboardButton('A', callback_data='11A'),
              telebot.types.InlineKeyboardButton('B', callback_data='11B'))
    sit14 = telebot.types.InlineKeyboardMarkup()
    sit14.row(telebot.types.InlineKeyboardButton('A', callback_data='14A'),
              telebot.types.InlineKeyboardButton('B', callback_data='14B'))
    sit15 = telebot.types.InlineKeyboardMarkup()
    sit15.row(telebot.types.InlineKeyboardButton('A', callback_data='15A'),
              telebot.types.InlineKeyboardButton('B', callback_data='15B'))
    sit16 = telebot.types.InlineKeyboardMarkup()
    sit16.row(telebot.types.InlineKeyboardButton('A', callback_data='16A'),
              telebot.types.InlineKeyboardButton('B', callback_data='16B'))
    sit18 = telebot.types.InlineKeyboardMarkup()
    sit18.row(telebot.types.InlineKeyboardButton('A', callback_data='18A'),
              telebot.types.InlineKeyboardButton('B', callback_data='18B'))
    sit19 = telebot.types.InlineKeyboardMarkup()
    sit19.row(telebot.types.InlineKeyboardButton('B', callback_data='19B'),
              telebot.types.InlineKeyboardButton('C', callback_data='19C'))
    sit20 = telebot.types.InlineKeyboardMarkup()
    sit20.row(telebot.types.InlineKeyboardButton('B', callback_data='20B'))
    sit21REP = telebot.types.InlineKeyboardMarkup()
    sit21REP.row(telebot.types.InlineKeyboardButton('B', callback_data='21B'),
                 telebot.types.InlineKeyboardButton('C', callback_data='21C'),
                 telebot.types.InlineKeyboardButton('C', callback_data='21D'))
    sit22 = telebot.types.InlineKeyboardMarkup()
    sit22.row(telebot.types.InlineKeyboardButton('A', callback_data='22A'),
              telebot.types.InlineKeyboardButton('B', callback_data='22B'))
    sit23 = telebot.types.InlineKeyboardMarkup()
    sit23.row(telebot.types.InlineKeyboardButton('A', callback_data='23A'),
              telebot.types.InlineKeyboardButton('B', callback_data='23B'),
              telebot.types.InlineKeyboardButton('C', callback_data='23C'),
              telebot.types.InlineKeyboardButton('D', callback_data='23D'))
    sit24 = telebot.types.InlineKeyboardMarkup()
    sit24.row(telebot.types.InlineKeyboardButton('A', callback_data='24A'),
              telebot.types.InlineKeyboardButton('B', callback_data='24B'),
              telebot.types.InlineKeyboardButton('C', callback_data='24C'),
              telebot.types.InlineKeyboardButton('D', callback_data='24D'),
              telebot.types.InlineKeyboardButton('E', callback_data='24E'))
    sit25 = telebot.types.InlineKeyboardMarkup()
    sit25.row(telebot.types.InlineKeyboardButton('A', callback_data='25A'),
              telebot.types.InlineKeyboardButton('B', callback_data='25B'),
              telebot.types.InlineKeyboardButton('C', callback_data='25C'),
              telebot.types.InlineKeyboardButton('D', callback_data='25D'))
    sit26 = telebot.types.InlineKeyboardMarkup()
    sit26.row(telebot.types.InlineKeyboardButton('A', callback_data='26A'),
              telebot.types.InlineKeyboardButton('B', callback_data='26B'))
    sit27 = telebot.types.InlineKeyboardMarkup()
    sit27.row(telebot.types.InlineKeyboardButton('A', callback_data='27A'),
              telebot.types.InlineKeyboardButton('B', callback_data='27B'))
    sit28 = telebot.types.InlineKeyboardMarkup()
    sit28.row(telebot.types.InlineKeyboardButton('A', callback_data='28A'),
              telebot.types.InlineKeyboardButton('B', callback_data='28B'),
              telebot.types.InlineKeyboardButton('C', callback_data='28C'),
              telebot.types.InlineKeyboardButton('D', callback_data='28D'))
    sit29 = telebot.types.InlineKeyboardMarkup()
    sit29.row(telebot.types.InlineKeyboardButton('Parar la transferencia de datos, y devolverlos a la universidad.',
                                                 callback_data='29A'))
    sit29.row(telebot.types.InlineKeyboardButton('Borrar los datos y cobrar el dinero de la Pompeu Fabra.',
                                                 callback_data='29B'))

    cid = query.message.chat.id
    data[cid] = query.data
    print(query.data)
    if (gameON[cid] == True):
        if dialogo[cid] == False:
            if data[cid] == 'dialogo':
                dialogo[cid] = True

        if sit1bool[cid] == False:
            if data[cid] == '1A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "'Al final te voy a bajar los humos de un porrazo.' -Se va como si nada hubiera pasado.")
                boolAgresivo[cid] = True
                sit1bool[cid] = True
            elif data[cid] == '1B' and gameON[cid] == True:
                bot.send_message(cid, "'Y que no te vuelva a ver...' -Se va como si nada hubiera pasado.")
                sit1bool[cid] = True
                boolCauto[cid] = True

        if sit2bool[cid] == False:
            if data[cid] == '2A' and gameON[cid] == True:
                sit2bool[cid] = True
                boolFumeta[cid] = True
            elif data[cid] == '2B' and gameON[cid] == True:
                sit2bool[cid] = True
                boolFumeta[cid] = True
            elif data[cid] == '2C' and gameON[cid] == True:
                sit2bool[cid] = True
                boolNeutro[cid] = True
            elif data[cid] == '2D' and gameON[cid] == True:
                sit2bool[cid] = True
                boolSano[cid] = True

        if sit3bool[cid] == False:
            if data[cid] == '3B' and gameON[cid] == True:
                boolNoPrueba[cid] = True
                bot.send_message(cid, "Bien, decides no fumártelo…")
                time.sleep(2)
                bot.send_message(cid,
                                 "Por fin, te encuentras a alguien que conoces, es tu amigo Junior, que estudia el proceso de cómo tragan las jirafas allí en Veterinaria, siempre ha sido cuanto menos curioso, el chaval.")
                time.sleep(2)
                bot.send_message(cid, "Te alegras de verle, y tras unas palabras, le echáis unas caladas al blunt.")
                caladas[cid] = caladas[cid] + 1
                time.sleep(2)
                bot.send_message(cid, '“Este porro no sube…”  decís.')
                time.sleep(4)
                bot.send_message(cid, "...")
                time.sleep(2)
                bot.send_message(cid,
                                 "De repente el cielo cambia de color y tu amigo Junior empieza a hacer cosas raras. Se está transformando... ¡en una jirafa! O en algo parecido... Creo que estás fumao.\n\nSe ha añadido una calada al contador de caladas. Puedes acceder a él a través de la opción 'STATS 📖'")
                time.sleep(2)
                sit3bool[cid] = True
            elif data[cid] == '3A' and gameON[cid] == True:
                boolPrueba[cid] = True
                caladas[cid] = caladas[cid] + 1
                bot.send_message(cid, "Es buena, te sube enseguida.")
                time.sleep(2)
                bot.send_message(cid,
                                 "Empiezas a ver todo de otro color...y te encuentras a alguien, es una especie de jirafa humanoide, da bastante miedo, pero para tu sorpresa es muy amigable.\n\nSe ha añadido una calada al contador de caladas. Puedes acceder a él a través de la opción 'STATS 📖'")
                time.sleep(2)
                sit3bool[cid] = True

        if sit4bool[cid] == False:
            if data[cid] == '4A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "No, no se sabe, pero ahora *uab.cat* muestra un mensaje en japonés, muy enigmático.",
                                 parse_mode="Markdown")
                sit4bool[cid] = True
            elif data[cid] == '4B' and gameON[cid] == True:
                bot.send_message(cid, "Sí, están como locos, ten cuidado")
                time.sleep(1)
                bot.send_message(cid, "***Le preguntas otra opción \na) ¿Se sabe quién ha sido?", reply_markup=sit5)
                sit4bool[cid] = False
            elif data[cid] == '4C' and gameON[cid] == True:
                bot.send_message(cid,
                                 "***La jirafa se ríe y te da algo de pienso. Asqueado, le preguntas otra cosa. \na) ¿Se sabe quién ha sido? \nb) ¿Por eso hay tanta seguridad?",
                                 reply_markup=sit6)
                sit4bool[cid] = False

        if sit5bool[cid] == False:
            if data[cid] == '5A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "No, no se sabe, pero ahora *uab.cat* muestra un mensaje en japonés, muy enigmático.")
                sit5bool[cid] = True
                sit4bool[cid] = True

        if sit6bool[cid] == False:
            if data[cid] == '6A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "No, no se sabe, pero ahora *uab.cat* muestra un mensaje en japonés, muy enigmático.",
                                 parse_mode="Markdown")
                sit6bool[cid] = True
                sit4bool[cid] = True
            elif data[cid] == '6B' and gameON[cid] == True:
                bot.send_message(cid, "Sí, están como locos, ten cuidado")
                time.sleep(1)
                bot.send_message(cid, "***Le haces una última pregunta \na) ¿Se sabe quién ha sido?", reply_markup=sit5)
                sit6bool[cid] = True

        if sit7bool[cid] == False:
            if data[cid] == '7A' and gameON[cid] == True:
                objeto1[cid] = 1
                bot.send_message(cid, "Te ha sido entregado el mapa del Eix Central de manos de Doraemon")
                sit7bool[cid] = True
            elif data[cid] == '7B' and gameON[cid] == True:
                objeto1[cid] = 2
                bot.send_message(cid, "Te ha sido entregado el lazo amarillo de manos de Doraemon")
                sit7bool[cid] = True
            elif data[cid] == '7C' and gameON[cid] == True:
                objeto1[cid] = 3
                bot.send_message(cid, "Te ha sido entregado el casco romano de manos de Doraemon")
                sit7bool[cid] = True
            elif data[cid] == '7D' and gameON[cid] == True:
                objeto1[cid] = 4
                bot.send_message(cid, "Te ha sido entregada la pokéball vacía de manos de Doraemon")
                sit7bool[cid] = True

        if sit8bool[cid] == False:
            if data[cid] == '8A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "El samurái acepta tus respetos, te indica que debes hablar con una Geisha que está paseando por allí con su parasol.")
                sit8bool[cid] = True
            elif data[cid] == '8B' and gameON[cid] == True:
                bot.send_message(cid,
                                 "El samurái te pone la espada al cuello, y no tienes más opción que mostrar respeto.",
                                 reply_markup=sit9)
                # sit8bool[cid]=True
            elif data[cid] == '8C' and gameON[cid] == True:
                bot.send_message(cid,
                                 "El samurái, avergonzado, reconoce que no sabe japonés y es un farsante, y te señala una Geisha que está paseando por allí con su parasol. Se va llorando, le pegas una calada al porro para olvidarlo.")
                time.sleep(2)
                caladas[cid] = caladas[cid] + 1
                if caladas[cid] == 20:
                    bot.send_message(cid,
                                     "⚠️ Durante unos segundos todo se vuelve mucho, mucho más oscuro, pero recobras la conciencia. Ten cuidado o puede que no llegues al final de esta historia.")
                if (caladas[cid] >= 25):
                    bot.send_message(cid,
                                     "Tus ojos empiezan a cerrarse, has fumado demasiado... Empiezas a tener ganas de vomitar, tantas caladas son demasiadas...")
                    time.sleep(3)
                    bot.send_message(cid, "MUERES por sobredosis. FIN DE LA PARTIDA", reply_markup=boton_muerte)
                    userStep[cid] = -1
                    boolMuerte[cid] = True

                sit8bool[cid] = True
            elif data[cid] == '8D' and gameON[cid] == True:
                bot.send_message(cid,
                                 " El samurái te esquiva y te clava la katana en la espalda, muerte en el acto. FIN DE LA PARTIDA",
                                 reply_markup=boton_muerte)
                userStep[cid] = -1
                boolMuerte[cid] = True
                sit8bool[cid] = True

        if sit9bool[cid] == False:
            if data[cid] == '9A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "El samurái acepta tus respetos, te indica que debes hablar con una Geisha que está paseando por allí con su parasol.")
                sit9bool[cid] = True
                sit8bool[cid] = True

        if sit10bool[cid] == False:
            if data[cid] == '10A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Él, agradecido, te proporciona una granada del fornite y cantáis Paradise de coldplay.",
                                 reply_markup=paradise)
                time.sleep(2)
                bot.send_message(cid, "Te ha sido entregado la granada del Fortnite de manos de Willyrex")
                objeto2[cid] = 1
                sit10bool[cid] = True
            elif data[cid] == '10B' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Él, agradecido, te proporciona un pico de minecraft y cantáis Paradise de coldplay.",
                                 reply_markup=paradise)
                time.sleep(2)
                bot.send_message(cid, "Te ha sido entregado el pico del Minecraft de manos de Willyrex")
                objeto2[cid] = 2
                sit10bool[cid] = True
            elif data[cid] == '10C' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Willy te pide que te suscribas y le des a la campanita, a cambio, él te dará un obsequio, a elegir entre: \na) Granada del Fortnite \nb) Pico del Minecraft",
                                 reply_markup=sit11)
                time.sleep(2)
                # sit10bool[cid]=True
            elif data[cid] == '10D' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Aparece Vegetta777, y vuelves a tener Fe, pero entre los dos te matan con el pico de minecraft. Muerte del jugador, FIN DE LA PARTIDA.",
                                 reply_markup=boton_muerte)
                time.sleep(2)
                wigetta = open('wigetta.jpg', 'rb')
                bot.send_photo(cid, wigetta)
                userStep[cid] = -1
                sit10bool[cid] = True
                boolMuerte[cid] = True
                sit8bool[cid] = True

        if sit11bool[cid] == False:
            if data[cid] == '11A' and gameON[cid] == True:
                bot.send_message(cid, "Te ha sido entregado la granada del Fortnite de manos de Willyrex")
                objeto2[cid] = 1
                sit10bool[cid] = True
                sit11bool[cid] = True
            elif data[cid] == '11B' and gameON[cid] == True:
                bot.send_message(cid, "Te ha sido entregado el pico del Minecraft de manos de Willyrex")
                objeto2[cid] = 2
                sit10bool[cid] = True
                sit11bool[cid] = True

        if sit12bool[cid] == False:
            if data[cid] == '12A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Te dejaré pasar si completas la siguiente cita, es de las más famosas que tengo:")
                time.sleep(1)
                bot.send_message(cid,
                                 "“Los ______ son los que buscan la sabiduria; los _____ piensan ya haberla encontrado” \na)Sabios, necios \nb)Necios,sabios",
                                 reply_markup=sit14)
            elif data[cid] == '12B' and gameON[cid] == True:
                bot.send_message(cid,
                                 "“Como osas faltarle el respeto al emperador más grande que ha tenido La France, al grandísimo Napoleón!” (en este momento te pone la espada al cuello) \na)Te disculpas y muestras tus respetos, le ofreces una calada. \nb)Le vuelves a faltar al respeto, llamándolo paticorto.",
                                 reply_markup=sit15)
            elif data[cid] == '12C' and gameON[cid] == True:
                bot.send_message(cid,
                                 "“Como osas faltarle el respeto al emperador más grande que ha tenido La France, al grandísimo Napoleón!” (en este momento te pone la espada al cuello) \na)Te disculpas y muestras tus respetos, le ofreces una calada y gritas “Vive La France!”. \nb)Le vuelves a faltar al respeto, llamándolo paticorto.",
                                 reply_markup=sit16)
            elif data[cid] == '12D' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Napoleón se sonroja y te deja pasar encantado. “Los sabios son los que buscan la sabiduria; los necios piensan ya haberla encontrado”, te dice.")
                sit12bool[cid] = True
        # CONTESTACION A EINSTEIN EN CIENCIAS
        if sit13bool[cid] == False:
            if data[cid] == '13A' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Es una sustancia extremadamente corrosiva, pero no. No me refería a eso. Por ello, no te voy a dar las indicaciones para llegar al lavabo.")
                time.sleep(2)
                bot.send_message(cid, "Necessitas llegar al baño...")
                time.sleep(3)
                bot.send_message(cid, "...")
                time.sleep(2)
                bot.send_message(cid, 'Cada vez te encuentras peor')
                time.sleep(2)
                bot.send_message(cid, 'Te pones blanco, los ojos se te cierran y quedas indispuesto. FIN DE LA PARTIDA',
                                 reply_markup=boton_muerte)
                sit13bool[cid] = True
                userStep[cid] = -1
                boolMuerte[cid] = True
            elif data[cid] == '13B' and gameON[cid] == True:
                bot.send_message(cid,
                                 "No se ha molestado ni en intentarlo. Vergonzoso. Aunque también tiene que haber personas tontas en el mundo a los que pagar poco y explotarlos, como hice yo en Hiroshima. El lavabo está al final del pasillo a la derecha.")
                sit13bool[cid] = True

            elif data[cid] == '13C' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Evidentemente que lo acertaría. Ya dije que era muy fácil. El lavabo está al final del pasillo a la derecha.")
                time.sleep(2)
                sit13bool[cid] = True

            elif data[cid] == '13D' and gameON[cid] == True:
                bot.send_message(cid,
                                 "No se ha molestado ni en intentarlo. Vergonzoso. Aunque también tiene que haber personas tontas en el mundo a los que pagar poco y explotarlos, como hice yo en Hiroshima. El lavabo está al final del pasillo a la derecha.")
                sit13bool[cid] = True

        if sit14bool[cid] == False:
            if data[cid] == '14A' and gameON[cid] == True:
                bot.send_message(cid, "“¡Correcto! Eres digno de pasar y continuar con tu cruzada, joven”.")
                sit12bool[cid] = True
                sit14bool[cid] = True
            elif data[cid] == '14B' and gameON[cid] == True:
                bot.send_message(cid, "“Oh, mon dieu! ¡Dejaré pasar esta osadía, pero que sea la última vez!”")
                sit12bool[cid] = True
                sit14bool[cid] = True

        if sit15bool[cid] == False:
            if data[cid] == '15A' and gameON[cid] == True:
                bot.send_message(cid, "“Está bien, puedes pasar. ¡Recuerdos a los Borbones!”")
                sit12bool[cid] = True
                sit15bool[cid] = True
            elif data[cid] == '15B' and gameON[cid] == True:
                bot.send_message(cid,
                                 "Gran error, Napoleón no perdona esta insensatez, y te clava la espada. Fin de la partida.",
                                 reply_markup=boton_muerte)
                sit12bool[cid] = True
                sit15bool[cid] = True
                userStep[cid] = -1
                boolMuerte[cid] = True

        if sit16bool[cid] == False:
            if data[cid] == '16A' and gameON[cid] == True:
                bot.send_message(cid, "“Está bien, puedes pasar. Recuerdos a los Borbones!”")
                sit16bool[cid] = True
                sit12bool[cid] = True
            elif data[cid] == '16B':
                bot.send_message(cid,
                                 "Gran error, Napoleón no perdona tu insensatez, y te clava la espada. Fin de la partida.",
                                 reply_markup=boton_muerte)
                sit16bool[cid] = True
                sit12bool[cid] = True
                userStep[cid] = -1
                boolMuerte[cid] = True

        if sit17bool[cid] == False:
            if data[cid] == '17A' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Bueno tú te lo pierdes. Tenemos un ecosistema pionero en la industria. La envidia no es buena." \nE: -"Cuando esté muriendo la Tierra, tranquilo. Serás el último en llegar a Marte en uno de mis cohetes. Eso si consigues ir."',
                                 reply_markup=sit19)
            elif data[cid] == '17B' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Según nuestros contactos, en ingeniería parece que hay una conexión estable. One more thing… ten cuidado con los ingenieros. No son muy de fiar, mira a este."')
                sit17bool[cid] = True
            elif data[cid] == '17C' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Si tuvieras cáncer de páncreas no serías tan insolente."\nE: -"Jajaja, tranquilo, este hombre tiene muy poco sentido del humor. ¿Te gustan los delfines? A mí me encantan. Una vez tuve uno, pero dejó de funcionar."',
                                 reply_markup=sit18)

        if sit18bool[cid] == False:
            if data[cid] == '18A' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Bueno tú te lo pierdes. Tenemos un ecosistema pionero en la industria. La envidia no es buena." \nE: -"Cuando esté muriendo la Tierra, tranquilo. Serás el último en llegar a Marte en uno de mis cohetes. Eso si consigues ir."',
                                 reply_markup=sit20)
            elif data[cid] == '18B' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Según nuestros contactos, en ingeniería parece que hay una conexión estable. One more thing… ten cuidado con los ingenieros. No son muy de fiar, mira a este."')
                sit17bool[cid] = True
                sit18bool[cid] = True

        if sit19bool[cid] == False:
            if data[cid] == '19B' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Según nuestros contactos, en ingeniería parece que hay una conexión estable. One more thing… ten cuidado con los ingenieros. No son muy de fiar, mira a este."')
                sit18bool[cid] = True
                sit17bool[cid] = True
                sit19bool[cid] = True
            elif data[cid] == '19C' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Si tuvieras cáncer de páncreas no serías tan insolente."\nE: -"Jajaja, tranquilo, este hombre tiene muy poco sentido del humor. ¿Te gustan los delfines? A mí me encantan. Una vez tuve uno, pero dejó de funcionar."',
                                 reply_markup=sit20)

        if sit20bool[cid] == False:
            if data[cid] == '20B' and gameON[cid] == True:
                bot.send_message(cid,
                                 'S: -"Según nuestros contactos, en ingeniería parece que hay una conexión estable. One more thing… ten cuidado con los ingenieros. No son muy de fiar, mira a este."')
                sit17bool[cid] = True
                sit18bool[cid] = True
                sit19bool[cid] = True
                sit20bool[cid] = True

        if sit21bool[cid] == False:
            if data[cid] == '21A' and gameON[cid] == True:
                bot.send_message(cid, 'Me parece que te equivocas de dioses. Sí, es cierto. Me suenas de algo...')
                time.sleep(2)
                bot.send_message(cid,
                                 'Escoge otra opción: \nb) Borracho, aparta de mi camino. No quieres problemas así que no me toques las narices. \nc) Buen día y buena ventura, compañeros. Me dirijo a la zona de la facultad de ingeniería. Según la información que poseo el único camino posible para llegar es siguiendo este paso. \nd) Me dirijo por este paso a la facultad de ingeniería. Ahora que tienes suficiente información, métete en tus asuntos.',
                                 reply_markup=sit21REP)
            elif data[cid] == '21B' and gameON[cid] == True:
                bot.send_message(cid, 'Deberías tener más modales cuando te superan en número.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Dos hombres te cogen y entre todos te dan 23 puñaladas. MUERES, FIN DE LA PARTIDA',
                                 reply_markup=boton_muerte)
                sit21bool[cid] = True
                userStep[cid] = -1
                boolMuerte[cid] = True
            elif data[cid] == '21C' and gameON[cid] == True:
                bot.send_message(cid,
                                 'Debe saber que el paso por este camino tiene un coste. ¿Está usted dispuesto a pagarlo? \na)Pagarle con unas cuantas caladas de la pipa de la paz. \nb)Pagarle con un puñetazo en la boca.',
                                 reply_markup=sit22)
            elif data[cid] == '21D' and gameON[cid] == True:
                bot.send_message(cid, 'Vaya, vaya. Parece que alguien se cree el gallo del corral.')
                time.sleep(2)
                bot.send_message(cid,
                                 '¡Cogedle! Dos hombres te cogen y entre todos te dan 23 puñaladas. MUERES, FIN DE LA PARTIDA',
                                 reply_markup=boton_muerte)
                userStep[cid] = -1
                boolMuerte[cid] = True
                sit21bool[cid] = True

        if sit22bool[cid] == False:
            if data[cid] == '22A' and gameON[cid] == True:
                userStep[cid] = 10
                sitShown[cid] = False
                sit21bool[cid] = True
                sit22bool[cid] = True
                bot.send_message(cid,
                                 '¡Vaya, vaya! Parece que tenemos trato. Tranquilo, siga este rumbo y en breve llegará a su destino.',
                                 reply_markup=boton_eng)
            elif data[cid] == '22B' and gameON[cid] == True:
                userStep[cid] = -1
                boolMuerte[cid] = True
                bot.send_message(cid,
                                 '¡Date por pagado! Le golpeas en la mandíbula y le salta un diente, dos hombres te cogen y entre todos te dan 23 puñaladas. MUERES, FIN DE LA PARTIDA',
                                 reply_markup=boton_muerte)
                sitShown[cid] = False
                sit21bool[cid] = True
                sit22bool[cid] = True

        if sit23bool[cid] == False and sit24bool[cid] == False:

            if data[cid] == '23A' or data[cid] == '24A' and gameON[cid] == True:
                if objeto1[cid] != 4:
                    bot.send_message(cid, 'Quizá si tuviera una Pokéball...')
                    time.sleep(2)
                    if objeto2[cid] != 1:
                        bot.send_message(cid,
                                         'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero.',
                                         reply_markup=sit23)
                    if objeto2[cid] == 1:
                        bot.send_message(cid,
                                         'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero. \ne)Lanzar la granada del Fortnite',
                                         reply_markup=sit24)
                else:
                    sit23bool[cid] = True
                    sit24bool[cid] = True
                    sit26bool[cid] = True
                    sit27bool[cid] = True
                    bot.send_message(cid, 'Decides utilizar tu pokéball, ¿pero contra quién? \na)Entrenador de Pikachu. \nb)Entrenador de Charmander. \nc)Pikachu. \nd)Charmander', reply_markup=sit25)

            elif data[cid] == '23B' or data[cid] == '24B' and gameON[cid] == True:
                bot.send_message(cid,
                                 '-"Hey, perdonad. Aldeanos de Konoha. Para acceder a la facultad me están pidiendo una entrada. ¿Podríais ayudarme?", dices')
                time.sleep(2)
                bot.send_message(cid, '-Un poco de respeto por favor, que soy Hokage. ¿Qué necesitas exactamente?')
                bot.send_message(cid, 'Contestas: -"Mis disculpas. Me gustaría acceder a la facultad para poder investigar todo esto que está pasando con la red privada."')
                time.sleep(2)
                bot.send_message(cid,'-Agh, los aldeanos de Konoha somos muy dados a la justicia. Puedo enseñarte el camino de las sombras. \na) ¡Joder! Eso sería canelita en rama.\nb) Creo que mejor me voy a hablar con otros frikis.', reply_markup=sit26)

            elif data[cid] == '23C' or data[cid] == '24C':
                bot.send_message(cid, 'Le preguntas: -Oye, ¿eres Goku, verdad?')
                goku = open('goku.jpg', 'rb')
                bot.send_photo(cid, goku)
                time.sleep(2)
                bot.send_message(cid, 'Goku: -Sí, soy yo.')
                time.sleep(1)
                bot.send_message(cid, 'Contestas: -"Eres el defensor de los débiles y de los habitantes de la Tierra ¿verdad?"')
                time.sleep(2)
                bot.send_message(cid, 'Bueno, podría decirse…')
                time.sleep(2)
                bot.send_message(cid,
                                 'Tu le constestas: \na) - Esa panda que hay delante de la puerta amenazan con cargarse la facultad a menos que se les dé lo que piden. ¡Necesitamos que nos ayudes! \nb) -Creo que mejor me voy a hablar con otros frikis.',
                                 reply_markup=sit27)

            elif data[cid] == '23D' or data[cid] == '24D':
                bot.send_message(cid, '"Oye, necesito entrar. ¿Podrías ayudarme?", dices"')
                time.sleep(2)
                bot.send_message(cid, 'DOM130: -"Claro bro, soy la panacea a tus problemas."')
                time.sleep(2)
                bot.send_message(cid, 'DOM130: -"Tranquilo, ahora verás mi esencia."')
                time.sleep(2)
                bot.send_message(cid, 'El rapero se acerca a los de la puerta y les dice:')
                time.sleep(2)
                bot.send_message(cid, 'DOM130: -"A ver, mi bro y yo queremos pasar. Nos vamos a montar un fiestón."')
                time.sleep(2)
                bot.send_message(cid, '-¿Tenéis entradas?')
                time.sleep(2)
                bot.send_message(cid, 'DOM130: -"No. Y no nos hacen falta. Bro, dame una base"')
                time.sleep(2)
                bot.send_message(cid, '*Suena una base de rap*', parse_mode="Markdown")
                time.sleep(2)
                bot.send_message(cid, 'Ha, yo yo yo')
                time.sleep(1)
                bot.send_message(cid, 'Ha, yo yo yo')
                time.sleep(1)
                bot.send_message(cid, 'Eh')
                time.sleep(1)
                bot.send_message(cid, 'Yo')
                time.sleep(1)
                bot.send_message(cid, 'Y donde están')
                time.sleep(1)
                bot.send_message(cid, 'Los niños que en el parque jugaban')
                time.sleep(1)
                bot.send_message(cid, '¿Dónde están?')
                time.sleep(2)
                bot.send_message(cid, '[...]', reply_markup=ubisunt_boton)
                time.sleep(2)
                bot.send_message(cid, '-¿A qué viene esto? ¿De qué niños hablas?')
                time.sleep(2)
                bot.send_message(cid,
                                 'El King del hip-hop no soy yo, pero me falta poco \nSolo sé que no soy Dios cuando con el lienzo choco \nModernízate un poco, bro, no estamos en el barroco \nFlipa más con esto, ey yo, es el flow de Morocco.')
                time.sleep(3)
                bot.send_message(cid, '-¿Este tío qué se ha metido?')
                time.sleep(2)
                bot.send_message(cid,
                                'Pero quemo queroseno, sueno bueno en pleno vuelo \n¿Que no es nuevo? Muestro huevos \nTraes mechero, luego pruebo \nY como llego hasta la cima, me elevo \nPuedo volar por el cielo sin quitar los pies del suelo.')
                time.sleep(2)
                bot.send_message(cid, 'Me está incomodando.')
                time.sleep(2)
                bot.send_message(cid, 'Oye, este tío me da muy mal rollo. Vámonos por favor.')
                time.sleep(2)
                bot.send_message(cid, '*El hombre y la mujer huyen despavoridos, dejando la entrada libre*', parse_mode="Markdown")
                time.sleep(2)
                bot.send_message(cid, 'Alucinando con la boca abierta sacas el cirio y le pegas un calo. Le ofreces al rapero.')
                time.sleep(2)
                caladas[cid] = caladas[cid] + 1
                if caladas[cid] >= 20:
                    bot.send_message(cid,
                                     "⚠️ Durante unos segundos todo se vuelve mucho, mucho más oscuro, pero recobras la conciencia. Ten cuidado o puede que no llegues al final de esta historia.")
                    if (caladas[cid] >= 25):
                        bot.send_message(cid,
                                         "Tus ojos empiezan a cerrarse, has fumado demasiado... Empiezas a tener ganas de vomitar, tantas caladas son demasiadas...")
                        time.sleep(3)
                        bot.send_message(cid, "MUERES por sobredosis. FIN DE LA PARTIDA", reply_markup=boton_muerte)
                        userStep[cid] = -1
                        boolMuerte[cid] = True

                bot.send_message(cid, 'Lo acepta, se lo mete en la boca y lo disfruta. Parece que le sepa a gloria.')
                time.sleep(2)
                bot.send_message(cid, 'Bro, hazme un favor: sígueme en Spotify, Dom130.', reply_markup=dom_boton)
                sit24bool[cid] = True
                sit25bool[cid] = True
                sit26bool[cid] = True
                sit27bool[cid] = True
                sit23bool[cid] = True

            elif data[cid] == '24E':
                bot.send_message(cid, '*Tiras la granada a los pies de los de la entrada y huyen despavoridos*')
                time.sleep(2)
                objeto2[cid] = 0
                bot.send_message(cid, "*Esperas a que se disipe el humo y te adentras en la Escola d'Enginyeria*",
                                 parse_mode="Markdown")
                time.sleep(2)
                sit24bool[cid] = True

        if sit25bool[cid] == False:
            if data[cid] == '25A' or data[cid] == '25B':
                bot.send_message(cid,'¡Oh, mierda! ¡Me has dado en la cabeza, eso duele! La próxima vez saldré vencedor. Toma.\n\n*Te da 12€ y una extraña tarjeta con "Q5" impreso en un lateral*')
                objeto1[cid] = 5
                time.sleep(3)
                bot.send_message(cid,'Te diriges a la puerta y le entregas los 12€ a los chavales de la entrada. Te dan una entrada y te permiten el paso al interior. Hoy tienes una consumición gratis')
                sit25bool[cid] = True
                sit24bool[cid] = True
                sit23bool[cid] = True
            if data[cid] == '25C' or data[cid] == '25D':
                bot.send_message(cid, '-¡Eh! ¡No puedes capturar el pokémon de otro entrenador!')
                time.sleep(2)
                bot.send_message(cid, 'Finalmente le diriges la palabra: ')
                time.sleep(3)
                bot.send_message(cid, 'Dices: -"Haber estudiao"')
                time.sleep(2)
                bot.send_message(cid, '-Venga, si me lo devuelves te doy esta entrada.')
                time.sleep(2)
                bot.send_message(cid, '*Devuelves  el pokémon, te da la entrada y una extraña tarjeta con "Q5" grabado en un lateral.*')
                objeto1[cid] = 5
                time.sleep(2)
                bot.send_message(cid,'*Te diriges a la puerta y le entregas la entrada a los dos frikis. Te permiten el paso al interior. Hoy tienes una consumición gratis*')
                sit25bool[cid] = True
                sit24bool[cid] = True
                sit23bool[cid] = True

        if sit26bool[cid] == False:
            if data[cid] == '26A':
                bot.send_message(cid,
                                 'Te lleva por un camino y te hace colarte por un agujero. Acabas saliendo por el techo del lavabo de la Q1.')
                sit24bool[cid] = True
                sit23bool[cid] = True
                sit25bool[cid] = True
                sit26bool[cid] = True
                sit27bool[cid] = True
            if data[cid] == '26B':
                if objeto2[cid] != 1:
                    bot.send_message(cid,
                                     'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero.',
                                     reply_markup=sit23)
                if objeto2[cid] == 1:
                    bot.send_message(cid,
                                     'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero.\ne) Lanzar la granada del Fortnite',
                                     reply_markup=sit24)

        if sit27bool[cid] == False:
            if data[cid] == '27A':
                bot.send_message(cid,
                                 'Ves como Goku se dirige a los de la puerta y se lía a leches con ellos. Escuchas algún que otro Kame Hame Ha.')
                time.sleep(2)
                bot.send_audio(cid, audio=open('goku-mp3.mp3', 'rb'))
                time.sleep(2)
                bot.send_message(cid, 'Huyen despavoridos con el cuerpo magullado')
                time.sleep(2)
                bot.send_message(cid, 'Goku regresa:')
                time.sleep(2)
                bot.send_message(cid, 'Goku: -Ya podéis estar tranquilos. Trabajo hecho.')
                sit24bool[cid] = True
                sit25bool[cid] = True
                sit26bool[cid] = True
                sit27bool[cid] = True
                sit23bool[cid] = True
            elif data[cid] == '27B':
                if objeto2[cid] != 1:
                    bot.send_message(cid,
                                     'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero.',
                                     reply_markup=sit23)
                if objeto2[cid] == 1:
                    bot.send_message(cid,
                                     'Ves que hay unos cuantos frik... Ingenieros a tu alrededor. Decides hablar con:\na)Los ingenieros vestidos de Pokémon.\nb)Los ingenieros vestidos de Naruto.\nc)Los ingenieros vestidos de Dragon Ball.\nd)El ingeniero rapero. \ne)Lanzar la granada del Fortnite',
                                     reply_markup=sit24)
        if sit28bool[cid] == False:
            if data[cid] == '28A' or data[cid] == '28C' or data[cid] == '28D':
                bot.send_message(cid, 'Vaya, parece que no hay nada ni nadie.')
                time.sleep(2)
                bot.send_message(cid, '¿Dónde vas? \na) QC/0000 \nb) QC/1000 \nc) QC/2000 \nd) QC/3000',
                                 reply_markup=sit28)
            if data[cid] == '28B':
                bot.send_message(cid, 'Ves que uno de los despachos tiene las luces encendidas.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Te diriges al despacho con las luces encendidas. Escuchas que alguien está hablando pero no entiendes muy bien.')
                time.sleep(2)
                bot.send_message(cid, 'Escuchas de fondo: -Sí… No… está… un problema.')
                sit28bool[cid] = True

        if sit29bool[cid] == False:
            if data[cid] == '29A':
                bot.send_message(cid, 'Te diriges hacia el ordenador.')
                time.sleep(2)
                bot.send_message(cid, 'Paras la transferencia.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Le pegas una calada al porro, te lo acabas y llamas al 112, reportas el robo de la información y te declaras culpable.')
                time.sleep(2)
                bot.send_message(cid, 'Más tarde te entregas a la policía.')
                time.sleep(2)
                bot.send_message(cid, 'Se detienen a cinco altos cargos de la Pompeu Fabra.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Se declara un juicio, se les juzga por extorsión, robo de datos y malversación de fondos. Les caen diez años a cada uno.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Gracias a tu colaboración se te baja la condena a arresto domiciliario hasta que acabes la carrera con permiso para ir a clase, estarás bajo vigilancia permanente hasta cumplir tu condena.')
                time.sleep(2)
                sit29bool[cid] = True
                sit29bool[cid] = True
                set_game_bools(cid)
                bot.send_message(cid, '---FIN---', reply_markup=mid_menu)
                bot.send_message(cid, "Desarrollado por:\n-Pedro José Bauzá\n-Néstor Campos\n-Flavio Jiménez\n\nEscrito por:\n-Samer Bujana\n-Pedro García\n\n¡ENHORABUENA POR HABER LLEGADO AL FINAL 1 DE UABlunt!",reply_markup=instagram)

            elif data[cid] == '29B':
                bot.send_message(cid, 'Te diriges al ordenador.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Abres una página de vuelos y te compras un billete a Barbados. Vas a tener un verano de la leche.')
                time.sleep(2)
                bot.send_message(cid, 'Coges el teléfono y llamas a uno de los contactos de la Pompeu Fabra.')
                time.sleep(2)
                bot.send_message(cid, 'Das el aviso de que el trabajo está hecho.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Te proporcionan una cuenta bancaria de las Islas Caimán con el dinero que se te ha prometido.')
                time.sleep(2)
                bot.send_message(cid, 'Cuelgas.')
                time.sleep(2)
                bot.send_message(cid,
                                 'Coges el teléfono, lo rompes y lo estampas contra el suelo, lo pisoteas hasta asegurarte de que está totalmente inservible.')
                time.sleep(2)
                bot.send_message(cid, 'Abres la ventana y tiras el teléfono.')
                time.sleep(2)
                bot.send_message(cid, 'Te pones unas gafas de sol y el búho en los labios, lo enciendes.')
                time.sleep(2)
                bot.send_message(cid, 'Exhalando el humo, sales de allí como el mastodonte que eres.')
                time.sleep(2)
                userStep[cid] = 0
                sit29bool[cid] = True
                set_game_bools(cid)
                bot.send_message(cid, '--FIN--', reply_markup=mid_menu)
                bot.send_message(cid, "Desarrollado por:\n-Pedro José Bauzá\n-Néstor Campos\n-Flavio Jiménez\n\nEscrito por:\n-Samer Bujana\n-Pedro García\n\n¡ENHORABUENA POR HABER LLEGADO AL FINAL 2 DE UABlunt!",reply_markup=instagram)


# OPCIONES DEL MENÚ DE JUEGO
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_text(m):
    global gameON, caladas, asigRol, userStep, objeto, knownUsers
    cid = m.chat.id
    if cid in knownUsers:
        if (m.text == "Dar calada 🚬🍁" and gameON[cid] == True):
            if asigRol[cid] == False and peleaEmojis[cid] == False:
                caladas[cid] = caladas[cid] + 1
                bot.send_message(cid, '🚬🍁LE DAS UNA CALADA AL PORRO')
                if caladas[cid] == 20:
                    bot.send_message(cid,
                                     "⚠️ Durante unos segundos todo se vuelve mucho, mucho más oscuro, pero recobras la conciencia. Ten cuidado o puede que no llegues al final de esta historia.")
                if (caladas[cid] >= 25):
                    bot.send_message(cid,
                                     "Tus ojos empiezan a cerrarse, has fumado demasiado... Empiezas a tener ganas de vomitar, tantas caladas son demasiadas...")
                    time.sleep(3)
                    bot.send_message(cid, "MUERES por sobredosis. FIN DE LA PARTIDA", reply_markup=boton_muerte)
                    userStep[cid] = -1
                    boolMuerte[cid] = True

            else:
                if peleaEmojis[cid] == True:
                    bot.send_message(cid,
                                     '🍁 Eh, eh, no puedes fumar en el despacho. Un poco de respeto. 🍁\n\nNo ha aumentado el contador de caladas.')
                else:
                    bot.send_message(cid,
                                     '🍁 Eh, eh, tómatelo con calma y espera hasta obtener tu rol. 🍁\n\nNo ha aumentado el contador de caladas.')
        elif (m.text == "STATS 📖"):
            list_Facultades = ["0", "1", "2", "Estás en la Facultad de Veterinaria, pero no estás muy seguro.",
                               "Facultad de Veterinaria.", "Facultad de Traducción e Interpretación", "Plaza Cívica",
                               "Facultad de Ciencias Sociales", "Facultad de Ciencias", "VITAE",
                               "Escuela de Ingeniería"]
            bot.send_message(cid,
                             "📖 STATS 📖\n\n-Ubicación: " + list_Facultades[get_user_step(cid)] + "\n-Llevas " + str(
                                 caladas[cid]) + ' caladas.' + "\n-Inventario: Porro" + list_objetos[objeto1[cid]] +
                             list_objetos_willy[objeto2[cid]])
        elif (m.text == "Forzar fin de partida ❌"):
            # gameON[cid] = False
            bot.send_message(cid, "Para resetear el bot, haz clic aquí: /start \n\nEsta acción NO se puede deshacer.")


print ('UABlunt se está ejecutando utilizando esta máquina como servidor.')

while (True):
    if __name__ == '__main__':
        bot.polling(none_stop=True)