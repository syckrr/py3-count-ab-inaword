import sys
say=0
print("Welcome,'ab' Search Algorithm v1.0\nCoded by acap1t!")
def fonksiyon():
    global say,kelime
    kelime= str(input("Search in :(should include 'ab')\n ># "))
    for harf in kelime:
        if harf=='a':
            asay=1
        if harf=='b':
            if asay==1:
                say=say+1
                asay=0

while True:
    fonksiyon()
    print(kelime," -Has ",say,"  'ab'!\n------")
    say=0
