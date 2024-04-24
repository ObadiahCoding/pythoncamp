import random

def roll_dice():
    return random.randint(1, 6)

def ludo_dice():
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }

    roll_result = roll_dice()
    print(f"Dice Roll: {dice_faces[roll_result]} ({roll_result})")

if __name__ == "__main__":
    ludo_dice()
