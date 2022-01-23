import sqlite3
import random


class AnimalsDB:
    def get_image(self):
        conn = sqlite3.connect('db/AnimalsDB.db')
        cursor = conn.cursor()

        self.cor_type = random.choice(cursor.execute("""SELECT id from Nutr_types""").fetchall())[0]

        images = cursor.execute(f'SELECT Image FROM Animals WHERE Nutr_type_id = {self.cor_type}').fetchall()
        conn.commit()
        ind = random.choice([i for i in range(len(images))])
        img = images[ind][0]
        return img

    def get_type(self):
        return self.cor_type

    def check_type(self, type_name):
        conn = sqlite3.connect('db/AnimalsDB.db')
        cursor = conn.cursor()
        type = cursor.execute(f'SELECT id FROM Nutr_types WHERE Nutr_type = {type_name}').fetchone()
        conn.commit()

        if type == self.cor_type:
            return True
        else:
            return False

