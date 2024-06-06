import sqlite3

def ensure_table_exists():
        conn = sqlite3.connect('warriors.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS warriors (name text, health integer, strength integer, agility integer, magic integer, defense integer, discord_user_id text)")
        conn.close()

class Warrior:
    def __init__(self, name: str, health: int, strength: int, agility: int, magic: int, defense: int, discord_user_id: str):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.magic = magic
        self.defense = defense
        self.discord_user_id = discord_user_id

    def copy(self):
        return self.__class__.raw_copy(self.name, self.health, self.strength, self.agility, self.magic, self.defense, self.discord_user_id)

    @classmethod
    def raw_copy(cls, name: str, health: int, strength: int, agility: int, magic: int, defense: int, discord_user_id: str):
        obj = cls.__new__(cls)
        obj.name = name
        obj.health = health
        obj.strength = strength
        obj.agility = agility
        obj.magic = magic
        obj.defense = defense
        obj.discord_user_id = discord_user_id
        return obj

    def save_to_db(self):
        ensure_table_exists()
        conn = sqlite3.connect('warriors.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS warriors (name text, health integer, strength integer, agility integer, magic integer, defense integer, discord_user_id text)")
        c.execute("INSERT INTO warriors VALUES (?, ?, ?, ?, ?, ?, ?)", (self.name, self.health, self.strength, self.agility, self.magic, self.defense, self.discord_user_id))
        conn.commit()
        conn.close()

    @classmethod
    def character_exists(cls, name: str):
        ensure_table_exists()
        conn = sqlite3.connect('warriors.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS warriors (name text, health isnteger, strength integer, agility integer, magic integer, defense integer, discord_user_id text)")
        c.execute("SELECT * FROM warriors WHERE name=?", (name,))
        result = c.fetchone()
        conn.close()
        return result is not None
    
    def get_characters_by_user_id(discord_user_id: str):
        ensure_table_exists()
        conn = sqlite3.connect('warriors.db')
        c = conn.cursor()
        c.execute("SELECT * FROM warriors WHERE discord_user_id=?", (discord_user_id,))
        results = c.fetchall()
        conn.close()
        return results
    @classmethod
    def delete_character(cls, name: str):
        ensure_table_exists()
        conn = sqlite3.connect('warriors.db')
        c = conn.cursor()
        c.execute("DELETE FROM warriors WHERE name=?", (name,))
        conn.commit()
        conn.close()
    
