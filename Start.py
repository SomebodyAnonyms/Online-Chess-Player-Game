import win32clipboard
from stockfish import Stockfish
import pyautogui
import time

stockfish = Stockfish("stockfish_20090216_x64_bmi2")

stockfish.set_skill_level(20)
stockfish.set_depth(1000)

Position = {
    "a": 65,
    "b": 100,
    "c": 140,
    "d": 175,
    "e": 215,
    "f": 250,
    "g": 285,
    "h": 325,
    "1": 440,
    "2": 400,
    "3": 360,
    "4": 325,
    "5": 285,
    "6": 250,
    "7": 215,
    "8": 175
}

Move_ST = ""
while Move_ST is not None:
    pyautogui.click(400, 699)
    time.sleep(0.1)
    pyautogui.click(400, 383)
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.press("esc")

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    Move = data

    stockfish.set_fen_position(Move)

    Move_ST = stockfish.get_best_move_time(200)

    Result_x = Position.get(Move_ST[0])
    Result_y = Position.get(Move_ST[1])
    time.sleep(0.2)
    pyautogui.click(Result_x, Result_y)
    Result_x = Position.get(Move_ST[2])
    Result_y = Position.get(Move_ST[3])
    time.sleep(0.2)
    pyautogui.click(Result_x, Result_y)

    time.sleep(3.5)
