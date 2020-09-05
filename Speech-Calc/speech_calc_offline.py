import speech_recognition as sr
import pyaudio
import pyttsx3
engine = pyttsx3.init()

response=['Welcome to smart calculator','My name is MONTY',
          'Thanks for enjoy with me ','Sorry ,this is  beyond my ability']

r = sr.Recognizer()

def voicetospeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + speech)
        return speech
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    words = r.recognize_sphinx(audio)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        return words
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        return -1
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        return -1
'''

def extract(text):
    l=[]

    for t in text.split(' '):
        try:
            l.append(t)
        except ValueError:
            pass
    for x in l:
        print(x)
    return l

def extractfloat(text):
    l=[]

    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    for x in l:
        print(x)
    return l



def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

# Addition
def add(a,b):
    return a+b

# Subtraction
def sub(a,b):
    return a-b

# Multiplication
def mul(a,b):
    return a*b

# Division
def div(a,b):
    return a/b

# Remainder
def mod(a,b):
    return a%b

# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()

def myname():
    print(response[1])
def sorry():
    print(response[3])

def listToString(s):

    str1 = ""
    s = str(s)
    for ele in s:
        str1 += ele

    # return string
    return str1



operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,
            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,
            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,
            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,
            'DIVISION':div,'MOD':mod,'REMANDER'
            :mod,'MODULAS':mod}

commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}



print("Welcome to this basic calculator, we can do simple calculations as of \
this version")

print("Say something (related to a calculation obviously)")
speech = voicetospeech()
while(speech == -1):
    speech = voicetospeech()
'''
print(speech)
temp = extract(speech)
for x in temp:
    print(x)
'''
tex = listToString(speech)
text = extract(speech)

for x in text:
    if(x == '+'):
        x = 'plus'

    if x.upper() in operations.keys():
        l = extractfloat(tex)
        print(l)
        r = operations[x.upper()] (l[0],l[1])
        print(r)
        engine.say(str(r))
        engine.runAndWait()
        break
    else:
        sorry()
