from time import ctime ,sleep
import webbrowser
import random
import requests

def get_input():
    global user_input

    user_input = input("ASK FROM ME  -------> : ")

def find_google():
    global fg
    fg = input("what do you want to search ?. : ")

def find_maps():
    global fm
    fm = input("where do you want to search ?. :")

def find_weather():
    global fw
    fw = input("where do you want to know ?.")

def print_answers(put_here):
    print(f'ALEXA -----> {put_here}')


def greeting():
    g_messages = ["hi there.","hey sadaruwan.","yeah im here.","How can I help you sadaruwan","im here."]
    r_message = random.choice(g_messages)
    print(r_message)

def thanking():
    th_messages = ["you are welcome.","its pleasure to being with you.","Never mind its my job"]
    r_th_message = random.choice(th_messages)
    print(r_th_message)




def get_ip_info():

    global internet_status
    internet_status = False

    try:
        r = requests.get('https://get.geojs.io/')
        ip_req = requests.get('https://get.geojs.io/v1/ip.json')
        ip_add = ip_req.json()['ip']
        # print(ip_add)

        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_req = requests.get(url)
        geo_data = geo_req.json()

        global get_city , get_region , get_country , get_latitude , get_longitude

        get_city = str((geo_data['city']))
        get_region = str((geo_data['region']))
        get_country = str((geo_data['country']))
        get_latitude = str((geo_data['latitude']))
        get_longitude = str((geo_data['longitude']))

        internet_status = True

    except:
        internet_status = False


def analyse_voice():

    get_ip_info()

    joke_count = 0
    answer_count = 0

    while True:

        if internet_status == False:
            print_answers("Check Your Internet Connection !")
            break

        else:
            pass

        if answer_count >= 5:
            joke_count = 0
            answer_count = 0

        else:
            pass

        get_input()

        words = ["time","location","city","country","hi","bye","thank","search","town",
                 "do","old","joke","ok","okay","thanks","great","wow","name","yoo","yo",
                 "tired","sleep","sleepy","hey","region","weather"]

        x = str(user_input)
        z = x.split()
        avl_words = 0

        for y in z:
            if y.lower() in words:
                avl_words += 1

        if avl_words == 0:

            print_answers("Did Not Get you.")
            continue

        elif avl_words >= 2:
            print_answers("Cant Identify What You Actualy Need.")

        else:
            if "bye" in z:

                print_answers("Ok. Good Bye Sadaruwan.")
                break

            else:
                for i in z:
                    if i.lower() in words :

                        if  joke_count >= 1:
                            answer_count += 1

                        else:
                            pass

                        if i.lower() =="time":
                            now_time = "Now Time Is " + ctime() +"."
                            converted_now_time = str(now_time)
                            print_answers(converted_now_time)
                            break

                        elif i.lower()=="town":

                            print_answers("only able to fine country, region & city for you")
                            break

                        elif i.lower()=="city":
                            your_city = 'Your city Is,'+ get_city + '.'
                            print_answers(your_city)
                            break

                        elif i.lower()=="hi" or i.lower()=="yoo" or i.lower()=="yo" or i.lower()=="hey" :

                            greeting()
                            break

                        elif i.lower()=="thank" or i.lower()=="thanks":

                            thanking()
                            break

                        elif i.lower()=="search":
                            find_google()

                            if fg =="":
                                print_answers("Did Not Able To Find.")
                                break

                            google_url = 'https://google.com/search?q=' + fg
                            webbrowser.get().open(google_url)
                            print_answers("here what i got.")

                            sleep(1.5)
                            break

                        elif i.lower()=="location":
                            find_maps()

                            if fm == "":
                                print_answers("Did Not Able To Find.")
                                break

                            else:

                                location_url = 'https://google.nl/maps/place/' + fm + '/&amp'
                                webbrowser.get().open(location_url)
                                print_answers("here what i got.")
                                sleep(1.5)
                                break
                            break

                        elif i.lower()=="country":

                            your_country = 'Your country Is ,' + get_country + '.'
                            print_answers(your_country)
                            break

                        elif i.lower()=="region":
                            your_region = 'Your Region Is ,' + get_region + '.'
                            print_answers(your_region)
                            break

                        elif i.lower()=="old":

                            print_answers("I have no idea about that. ask from the inventer.")
                            break

                        elif i.lower()=="do":

                            print_answers("I can do several thing for you as for now. in near future i will be upgraded with more. for now i can search what ever you want from google , find loactions , time , city , country & make you mood good Thats all.")
                            break

                        elif i.lower()=="joke":

                            if joke_count == 0:
                                print_answers("imagine, that how there is no internet connection in the world")
                                joke_count += 1

                            else:
                                print("Im fed up with telling stories to you. so plz.")
                            break


                        elif i.lower()=="ok" or i.lower()=="okay":

                            print_answers("Sounds Good.")
                            break

                        elif i.lower()=="wow" or i.lower()=="great":

                            print_answers("Its awesome being able to help.")
                            break

                        elif i.lower()=="name":

                            print_answers("my name is alexa.")
                            break

                        elif i.lower()=="tired":

                            print_answers("okay sadaruwan take a rest.")
                            break

                        elif i.lower()=="sleep" or i.lower()=="sleepy":

                            print_answers("okay sadaruwan go to the bed.")
                            break

                        elif i.lower()=="weather":

                            find_weather()
                            if fw =="":
                                print_answers("Did Not Able To Find.")
                                break

                            else:
                                google_url = 'https://google.com/search?q=' + " current weather of " + fw
                                webbrowser.get().open(google_url)
                                print_answers("here what i got.")

                                sleep(1.5)
                                break

                    else:
                        continue

analyse_voice()
