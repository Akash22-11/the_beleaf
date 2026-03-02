class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.rank = "Novice Mage"
        self.calculate_xp_threshold()

    # ---------------- XP SYSTEM ----------------
    def calculate_xp_threshold(self):
        """
        Difficulty increases non-linearly.
        Formula: XP = 100 * level^1.5
        """
        self.xp_to_next_level = int(100 * (self.level ** 1.5))

    # ---------------- GAIN XP ----------------
    def gain_xp(self, amount, activity_name):
        print(f"\n--- ⚔️ {self.name} performed {activity_name}! ---")
        self.current_xp += amount
        print(f"Received {amount} XP.")

        # Handle multiple level-ups
        while self.current_xp >= self.xp_to_next_level:
            self.level_up()

        self.show_stats()

    # ---------------- LEVEL UP ----------------
    def level_up(self):
        # Carry extra XP
        self.current_xp -= self.xp_to_next_level
        self.level += 1

        self.update_rank()
        self.calculate_xp_threshold()

        print(f"\n✨ LEVEL UP! You are now Level {self.level} ({self.rank})! ✨")

    # ---------------- RANK SYSTEM ----------------
    def update_rank(self):
        if self.level >= 15:
            self.rank = "Archmage"
        elif self.level >= 10:
            self.rank = "Main Sorcerer"
        elif self.level >= 5:
            self.rank = "Intermediate Mage"
        else:
            self.rank = "Novice Mage"

    # ---------------- STATS DISPLAY ----------------
    def show_stats(self):
        # Prevent overflow
        progress_ratio = self.current_xp / self.xp_to_next_level
        progress_percent = min(10, int(progress_ratio * 10))

        bar = "█" * progress_percent + "-" * (10 - progress_percent)

        print(f"[{bar}] {self.current_xp}/{self.xp_to_next_level} XP")
        print(f"Level: {self.level} | Rank: {self.rank}")
