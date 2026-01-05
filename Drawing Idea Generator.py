import random
import time
import sys
import os

class DrawingAdventure:
    def __init__(self):
        self.subjects = [
            "a mythical creature", "an astronaut", "a robot", "a wizard", "a pirate",
            "a dragon", "a futuristic city", "an enchanted forest", "a steampunk machine",
            "a underwater civilization", "a alien landscape", "a time traveler",
            "a magical artifact", "a haunted mansion", "a floating island",
            "a cyberpunk street", "a giant animal", "a person with elemental powers",
            "a celestial being", "a mechanical animal"
        ]
        
        self.actions = [
            "discovering", "battling", "creating", "exploring", "transforming",
            "protecting", "escaping", "searching for", "building", "unleashing",
            "controlling", "befriending", "riding", "hiding from", "communicating with",
            "evolving into", "sacrificing for", "chasing", "solving a mystery about",
            "uncovering the secret of"
        ]
        
        self.settings = [
            "in a neon-lit rainstorm", "at the edge of the universe", "in a library of lost knowledge",
            "on a clockwork planet", "in a dream within a dream", "during a solar eclipse",
            "in a city built on clouds", "inside a living crystal", "on the back of a giant turtle",
            "in a parallel dimension", "during a festival of lights", "in a sunken cathedral",
            "on a bridge between worlds", "in a garden of floating rocks", "at the bottom of the ocean",
            "inside a pocket dimension", "on a spaceship made of wood", "in a desert of glass",
            "on a mountain that reaches space", "in a forest where trees grow upside down"
        ]
        
        self.art_styles = [
            "in pixel art style", "as a watercolor painting", "in comic book style",
            "as an ink sketch with cross-hatching", "in impressionist style",
            "as a charcoal drawing", "in art nouveau style", "as a linocut print",
            "in pointillism", "as a surrealist painting", "in low poly 3D style",
            "as a stained glass window", "in ukiyo-e (Japanese woodblock) style",
            "as a graffiti mural", "in children's book illustration style",
            "as a detailed pen drawing", "in vaporwave aesthetic", "as a Renaissance painting",
            "in minimalistic line art", "as a psychedelic poster"
        ]
        
        self.colors = [
            "with a monochromatic color scheme", "using only warm colors", "in pastel colors",
            "with neon colors on dark background", "using complementary colors",
            "in shades of blue and green", "with a sunset color palette", "in black and white with one accent color",
            "using analogous colors", "with metallic gold and silver accents",
            "in earthy natural tones", "with high contrast colors", "using a triadic color scheme",
            "in cool colors only", "with glow-in-the-dark elements", "using a limited 3-color palette",
            "in sepia tones", "with prismatic/rainbow effects", "using muted desaturated colors",
            "with vibrant tropical colors"
        ]
        
        self.challenges = [
            "Draw it without lifting your pen", "Use only geometric shapes",
            "Draw it with your non-dominant hand", "Complete it in 10 minutes",
            "Draw it from an unusual perspective", "Use only circles and curves",
            "Incorporate a hidden symbol", "Make it symmetrical", "Add a reflective surface",
            "Include a light source with shadows", "Add texture to one element",
            "Show movement or motion lines", "Include a frame within the drawing",
            "Make it look transparent or translucent", "Show the same subject at different times",
            "Incorporate a pattern", "Add a glowing effect", "Show weather effects",
            "Include a reflection", "Add an unexpected small detail"
        ]
        
        self.moods = [
            "mysterious", "epic", "peaceful", "tense", "joyful", "melancholic",
            "whimsical", "dark", "hopeful", "chaotic", "serene", "energetic",
            "nostalgic", "futuristic", "ancient", "magical", "scientific",
            "romantic", "horrifying", "comical"
        ]
        
        self.ideas_history = []
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def slow_print(self, text, delay=0.03):
        """Print text with a typing effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def generate_idea(self, category=None):
        """Generate a random drawing idea"""
        subject = random.choice(self.subjects)
        action = random.choice(self.actions)
        setting = random.choice(self.settings)
        style = random.choice(self.art_styles)
        color = random.choice(self.colors)
        challenge = random.choice(self.challenges)
        mood = random.choice(self.moods)
        
        # Create different types of ideas
        if category == "simple":
            idea = f"Draw {subject} {style}"
        elif category == "scene":
            idea = f"{subject.capitalize()} {action} something {setting} {style}"
        elif category == "challenge":
            idea = f"Draw {subject} {setting}. {challenge}. {color}"
        elif category == "mood":
            idea = f"Create a {mood} scene of {subject} {action} {setting} {style}"
        else:
            # Full random combination
            templates = [
                f"Draw {subject} {action} something {setting} {style} {color}",
                f"Create a {mood} illustration: {subject} {setting}. {challenge}",
                f"{style}: {subject} {action} {setting} with a {mood} feeling. {color}",
                f"Art challenge: {subject} {setting}. {challenge} {color}",
                f"Concept: {subject} {action} {setting}. {style} with a {mood} mood. {challenge}"
            ]
            idea = random.choice(templates)
        
        # Add to history
        self.ideas_history.append(idea)
        
        return idea
    
    def display_banner(self):
        """Display the program banner"""
        self.clear_screen()
        banner = """
        ╔══════════════════════════════════════════════════════════╗
        ║                                                          ║
        ║      🎨 RANDOM DRAWING IDEA GENERATOR 🎨                ║
        ║                 - An Artistic Adventure -                ║
        ║                                                          ║
        ╚══════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def display_idea(self, idea, idea_number):
        """Display the generated idea in a formatted box"""
        print(" " + "═" * 60)
        print(f" 🎨  IDEA #{idea_number} ")
        print(" " + "═" * 60)
        print()
        
        self.slow_print(f"  ✦ {idea}")
        print()
        print(" " + "═" * 60)
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + " " * 10 + "✦ MAIN MENU ✦")
        print(" " * 5 + "─" * 40)
        print("  1. Generate a random drawing idea")
        print("  2. Generate a specific type of idea")
        print("  3. View your idea history")
        print("  4. Get a 5-day drawing challenge")
        print("  5. Clear screen")
        print("  6. Exit the adventure")
        print(" " * 5 + "─" * 40)
    
    def show_category_menu(self):
        """Display the category selection menu"""
        print("\n" + " " * 10 + "✦ IDEA CATEGORIES ✦")
        print(" " * 5 + "─" * 40)
        print("  1. Simple subject + style")
        print("  2. Full scene with action")
        print("  3. Art challenge")
        print("  4. Mood-based idea")
        print("  5. Completely random (default)")
        print(" " * 5 + "─" * 40)
    
    def view_history(self):
        """Display previously generated ideas"""
        if not self.ideas_history:
            print("\n  No ideas generated yet. Start your adventure!")
            return
        
        print("\n" + " " * 10 + f"✦ YOUR IDEA HISTORY ({len(self.ideas_history)} ideas) ✦")
        print(" " * 5 + "─" * 60)
        
        for i, idea in enumerate(self.ideas_history, 1):
            print(f"  {i:2}. {idea}")
        
        print(" " * 5 + "─" * 60)
        input("\n  Press Enter to continue...")
    
    def generate_challenge(self):
        """Generate a 5-day drawing challenge"""
        print("\n" + " " * 10 + "✦ 5-DAY DRAWING CHALLENGE ✦")
        print(" " * 5 + "─" * 60)
        
        challenges = []
        days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
        
        for day in days:
            challenge = self.generate_idea()
            challenges.append(f"  {day}: {challenge}")
        
        # Ensure all challenges are unique
        while len(set(challenges)) < 5:
            challenges = []
            for day in days:
                challenges.append(f"  {day}: {self.generate_idea()}")
        
        for challenge in challenges:
            self.slow_print(challenge, 0.02)
            print()
        
        print(" " * 5 + "─" * 60)
        input("\n  Press Enter to continue your adventure...")
    
    def run(self):
        """Main program loop"""
        self.display_banner()
        
        self.slow_print("  Welcome, artist! Ready for a creative adventure?", 0.04)
        self.slow_print("  I'll help you overcome artist's block with unique drawing ideas.", 0.04)
        self.slow_print("  Let's begin...", 0.05)
        time.sleep(1)
        
        idea_count = 0
        
        while True:
            self.show_menu()
            
            try:
                choice = input("\n  Enter your choice (1-6): ").strip()
                
                if choice == "1":
                    idea_count += 1
                    idea = self.generate_idea()
                    self.display_idea(idea, idea_count)
                    input("\n  Press Enter for more options...")
                
                elif choice == "2":
                    self.show_category_menu()
                    cat_choice = input("\n  Choose a category (1-5): ").strip()
                    
                    category_map = {
                        "1": "simple",
                        "2": "scene",
                        "3": "challenge",
                        "4": "mood",
                        "5": None
                    }
                    
                    category = category_map.get(cat_choice, None)
                    idea_count += 1
                    idea = self.generate_idea(category)
                    self.display_idea(idea, idea_count)
                    input("\n  Press Enter for more options...")
                
                elif choice == "3":
                    self.view_history()
                
                elif choice == "4":
                    self.generate_challenge()
                
                elif choice == "5":
                    self.display_banner()
                
                elif choice == "6":
                    self.slow_print("\n  Thank you for embarking on this artistic adventure!", 0.04)
                    self.slow_print(f"  You generated {idea_count} creative ideas.", 0.04)
                    self.slow_print("  Now go make some amazing art! 🎨✨", 0.04)
                    print()
                    break
                
                else:
                    print("\n  Please enter a number between 1 and 6.")
                    time.sleep(1)
            
            except KeyboardInterrupt:
                print("\n\n  Adventure interrupted! Until next time, artist! 👋")
                break

# Run the adventure
if __name__ == "__main__":
    adventure = DrawingAdventure()
    adventure.run()
