def calculate_xp_threshold(self):
    """
    Algorithm: As level increases, it becomes harder to level up.
    Formula: Next Level XP = Current Level * 100
    """
    self.xp_to_next_level = self.level * 100

def gain_xp(self, amount, activity_name):
    print(f"--- ⚔️ {self.name} performed {activity_name}! ---")
    self.current_xp += amount
    print(f"Received {amount} XP.")
    
    # Check if we leveled up (Loop handles multiple level ups at once)
    while self.current_xp >= self.xp_to_next_level:
        self.level_up()
    
    self.show_stats()

def level_up(self):
    self.current_xp -= self.xp_to_next_level                                                                 # Carry over extra XP
    self.level += 1
    self.calculate_xp_threshold()                                                                            # Recalculate difficulty
    
    # Rank Up Logic (If statements)
    if self.level == 5:
        self.rank = "Intermediate Mage"
    elif self.level == 10:
        self.rank = "Main Sorcerer"
        
    print(f"\n✨  HURRY LEVEL UP! You are now Level {self.level} ({self.rank})! ✨\n")

def show_stats(self):
    # Create a visual progress bar
    progress_percent = int((self.current_xp / self.xp_to_next_level) * 10)
    bar = "█" * progress_percent + "-" * (10 - progress_percent)
    print(f"[{bar}] {self.current_xp}/{self.xp_to_next_level} XP to next level")
