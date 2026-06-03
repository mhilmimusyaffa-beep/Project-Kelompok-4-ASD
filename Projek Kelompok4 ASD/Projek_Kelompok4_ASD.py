import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.json")

print("Database:", DATABASE)
print("Lokasi program:", os.getcwd())
print("File ditemukan?", os.path.exists(DATABASE))

# ============================================================
# DOUBLE LINKED LIST - Struktur Data Utama untuk Playlist
# ============================================================

class Node:
    """Node untuk Double Linked List"""
    def __init__(self, judul):
        self.judul = judul
        self.prev = None  # Pointer ke node sebelumnya
        self.next = None  # Pointer ke node berikutnya