import random

def pitchOptions():
    Pfast = 'It looks like its a Fastball!'
    Pcurve = 'It looks like its a Curveball!'
    Pslider = 'It looks like its a Slider! Swing?'
    Pchange = 'It looks like its a Change-Up! Swing?'
    Pball = 'It looks like its going to be a Ball!'

    x = [Pfast, Pcurve, Pslider, Pchange, Pball*5]   
    print(random.choice(x))
    

pitchOptions()


##pitch = input(random.choice(pitchOptions)).lower()


baseA = ['Single'] * 90 + ['Double'] * 32 + ['Triple'] * 5 + ['Home Run!!!'] * 37
baseB = ['Single'] * 51 + ['Double'] * 16 + ['Triple'] * 0 + ['Home Run!!!'] * 7
baseC = ['Single'] * (153-31-7-8) + ['Double'] * 31 + ['Triple'] * 7 + ['Home Run!!!'] * 8
baseD = ['Single'] * (182-30-3-15) + ['Double'] * 30 + ['Triple'] * 3 + ['Home Run!!!'] * 15
baseE = ['Single'] * (67-9-1-6) + ['Double'] * 9 + ['Triple'] * 1 + ['Home Run!!!'] * 6
baseF = ['Single'] * (111-21-7-10) + ['Double'] * 21 + ['Triple'] * 7 + ['Home Run!!!'] * 10
baseG = ['Single'] * (184-47-5-25) + ['Double'] * 47 + ['Triple'] * 5 + ['Home Run!!!'] * 25
baseH = ['Single'] * (50-8-4-6) + ['Double'] * 8 + ['Triple'] * 4 + ['Home Run!!!'] * 6
baseI = ['Single'] * (128-28-21) + ['Double'] * 28 + ['Triple'] * 0 + ['Home Run!!!'] * 21
baseJ = ['Single'] * (93-18-1-15) + ['Double'] * 18 + ['Triple'] * 1 + ['Home Run!!!'] * 15
