import speech_recognition as sr
import pyaudio
import pyttsx3
engine = pyttsx3.init()

response=['WCal','My name is Alfred',
          'Thanks for using this ','Sorry ,this is  beyond my ability']

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
            :mod,'MODULAS':mod, '+': add, '-':sub}

commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end}


print("Welcome to this basic calculator")
beg = "Welcome to this basic calculator"
engine.say(beg)
engine.runAndWait()
print("Ask what you wish to calculate")
engine.say("Ask what you wish to calculate")
engine.runAndWait()
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
    if x.upper() in operations.keys():
        l = extractfloat(tex)
        print(l)
        r = operations[x.upper()] (l[0],l[1])
        print(r)
        engine.say("Your answer is ", str(r))
        engine.runAndWait()
        engine.say(str(r))
        engine.runAndWait()
        break
    elif x.upper() in commands.keys():
        commands[x.upper()] ()
    else:
        sorry()
