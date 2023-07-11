import curses 
import time
def showspeed(screen, wpm):
    screen.addstr(20, 10, wpm)

def speedtest(screen, target_text):
    current_text = []
    wpm = 0
    start_time = time.time()
    screen.nodelay(True)
    while True:

        time_end = max(time.time() - start_time, 1)
        wpm = round((len(current_text)/ (time_end/60))/5)

        screen.clear()
        screen.addstr(20, 10, str(wpm))

        try:
            key = screen.getkey()
        except: 
            continue
        
        current_text.append(key)
        screen.addstr(5, 10, str(current_text))
        screen.refresh()


def main(screen):
    target_text = "hello my name is tom i'm from sheffield"
    
    while True:
        speedtest(screen, target_text)



curses.wrapper(main)