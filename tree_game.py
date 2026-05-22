#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌳 மண்ணின் மடி முதல் மரத்தின் முடி வரை!
Tree Life Cycle Game in Tamil
"""

import os
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class TreeLifeCycleGame:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.lives = 3
        self.player_name = ""
        self.game_over = False
        
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display game header"""
        print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🌳 மண்ணின் மடி முதல் மரத்தின் முடி வரை! 🌳{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}விளையாட்டு: 'இயற்கையின் சுழற்சி'{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}நிலை: {self.level} | புள்ளிகள்: {self.score} | உயிர்: {self.lives}{Style.RESET_ALL}\n")
    
    def display_level_info(self, level_num, title, description):
        """Display level information"""
        self.clear_screen()
        self.display_header()
        print(f"{Fore.CYAN}{'━'*60}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}நிலை {level_num}: {title}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*60}{Style.RESET_ALL}\n")
        print(f"{Fore.WHITE}{description}{Style.RESET_ALL}\n")
    
    def get_choice(self, options):
        """Get user choice"""
        for i, option in enumerate(options, 1):
            print(f"{Fore.LIGHTYELLOW_EX}{i}. {option}{Style.RESET_ALL}")
        
        while True:
            try:
                choice = int(input(f"\n{Fore.LIGHTBLUE_EX}உங்கள் தேர்வு (1 அல்லது 2): {Style.RESET_ALL}"))
                if choice in [1, 2]:
                    return choice
                else:
                    print(f"{Fore.RED}❌ 1 அல்லது 2 என்று மட்டும் தேர்ந்தெடுக்கவும்!{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ சரியான எண்ணை உள்ளிடவும்!{Style.RESET_ALL}")
    
    def show_result(self, is_correct, correct_choice, explanation):
        """Show result of choice"""
        if is_correct:
            print(f"\n{Fore.GREEN}✅ சரியான பதில்!{Style.RESET_ALL}")
            self.score += 10
            print(f"{Fore.LIGHTGREEN_EX}+10 புள்ளிகள்! மொத்தம்: {self.score}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}❌ தவறான பதில்!{Style.RESET_ALL}")
            self.lives -= 1
            print(f"{Fore.LIGHTRED_EX}ஒரு உயிர் இழந்தீர்கள். மீதமுள்ள உயிர்: {self.lives}{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'─'*60}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}📚 விளக்கம়:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{explanation}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'─'*60}{Style.RESET_ALL}\n")
    
    def level_1(self):
        """Level 1: The Seed (உறங்கும் விதை)"""
        self.display_level_info(
            1,
            "உறங்கும் விதை (The Seed)",
            """நீ இப்போது மண்ணிற்குள் இருக்கும் ஒரு சிறிய விதை. 
உனக்கு உயிர் வர வேண்டும் என்றால் நீ எதைத் தேர்ந்தெடுப்பாய்?"""
        )
        
        options = [
            "சூரிய ஒளி மற்றும் அளவான தண்ணீர்",
            "அதிகப்படியான வெள்ளம்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 1)
        
        explanation = """🌱 சூரிய ஒளி மற்றும் நீர் என்ற சரியான சூழ்நிலையில், 
உன்னுடைய விதையின் மேல் ஓட்டை உடைத்து நீ மெதுவாக வெளியே வருகிறாய்!
வேர்கள் மண்ணிற்குள் செல்லவும், இதழ் மேலே வருவும் தொடங்குகிறது!"""
        
        self.show_result(is_correct, 1, explanation)
        self.level += 1
    
    def level_2(self):
        """Level 2: The Sprout (துளிர்விடும் சிறு செடி)"""
        self.display_level_info(
            2,
            "துளிர்விடும் சிறு செடி (The Sprout/Sapling)",
            """மண்ணைப் பிளந்து கொண்டு இரண்டு சிறிய இலைகளுடன் நீ வெளியே வந்துவிட்டாய்.
இப்போது பலமான காற்று வீசுகிறது, ஆடு மாடுகள் உன்னை உண்ண வருகின்றன.
நீ என்ன செய்வாய்?"""
        )
        
        options = [
            "வேர்களை மண்ணிற்குள் ஆழமாகப் பதித்து, நேராக நிற்கப் பழகுவாய்",
            "பயந்து போய் இலைகளைச் சுருக்கிக் கொள்வாய்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 1)
        
        explanation = """💪 உன்னுடைய வேர்கள் மண்ணின் அடிப்பகுதியில் நன்கு விரிந்து பரவுகின்றன.
நீ பலம் பெற்று, பலமான காற்றை எதிர்கொள்ள முடிந்தது!
கிளைகள் வளர்ந்து, நீ ஒரு பெரிய செடியாக மாறுகிறாய்!"""
        
        self.show_result(is_correct, 1, explanation)
        self.level += 1
    
    def level_3(self):
        """Level 3: The Growing Tree (விருட்சமாகும் மரம்)"""
        self.display_level_info(
            3,
            "விருட்சமாகும் மரம் (The Growing Tree)",
            """நாட்கள் கடக்கின்றன. உனது தண்டுப்பகுதி தடிமனாகி, 
கிளைகள் பரப்பி நீ ஒரு பெரிய மரமாக மாறிவிட்டாய்!
இப்போது உனக்கு ஒரு புதிய ஆசை வருகிறது. 
உன்னைப் பார்க்க அழகாக மாற்ற நீ என்ன செய்ய வேண்டும்?"""
        )
        
        options = [
            "இலைகளை உதிர்க்க வேண்டும்",
            "அழகிய பூக்களைப் பூக்க வேண்டும்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 2)
        
        explanation = """🌸 மரத்தின் கிளைகளில் அழகிய வண்ணக் பூக்கள் பூத்துக் குலுங்குகின்றன!
தேனீக்களும் வண்ணத்துப்பூச்சிகளும் உன்னைத் தேடி வருகின்றன.
மகரந்தச்சேர்க்கை மூலம் பூக்கள் கனிகளாக மாற வாய்ப்பு கிடைக்கிறது!"""
        
        self.show_result(is_correct, 2, explanation)
        self.level += 1
    
    def level_4(self):
        """Level 4: Flower to Raw Fruit (பூவிலிருந்து காய்)"""
        self.display_level_info(
            4,
            "பூவிலிருந்து காய் (Flower to Raw Fruit)",
            """பூக்கள் பூத்துவிட்டன. அடுத்ததாக, இயற்கை உனக்குள் ஒரு மாற்றத்தை ஏற்படுத்துகிறது.
அந்தப் பூக்கள் எல்லாம் என்னவாக மாற வேண்டும்?"""
        )
        
        options = [
            "காய்ந்து கீழே விழ வேண்டும்",
            "சிறிய பிஞ்சுகளாக மாறி, பசுமையான காய்களாக மாற வேண்டும்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 2)
        
        explanation = """🌿 பூக்கள் மெதுவாக உருமாறி, மரமெங்கும் பச்சை பசேலெனக் காய்கள் தொங்குகின்றன!
இந்தக் காய்கள் மிகவும் சிறியதாகவும் வளர வேண்டியதாகவும் இருக்கிறது.
பசுமையான இந்தக் காய்கள் மெதுவாக வளர்ந்து பழமாக மாற தொடங்குகின்றன!"""
        
        self.show_result(is_correct, 2, explanation)
        self.level += 1
    
    def level_5(self):
        """Level 5: The Ripe Fruit (காயிலிருந்து கனி)"""
        self.display_level_info(
            5,
            "காயிலிருந்து கனி (The Ripe Fruit)",
            """பச்சை காய்கள் அப்படியே இருந்தால் பறவைகளும் மனிதர்களும் சாப்பிட முடியாது.
அவைகளுக்குச் சுவை ஊட்ட நீ என்ன செய்ய வேண்டும்?"""
        )
        
        options = [
            "சூரிய ஒளியை உள்வாங்கி, காய்களைக் கனிய வைக்க (பழுக்க வைக்க) வேண்டும்",
            "காய்களை அப்படியே வைத்திருக்க வேண்டும்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 1)
        
        explanation = """🍎 சூரிய ஒளியின் மாধுர்யமாக, காய்கள் யாவும் 
சுவையான, இனிப்பான, சிவந்த பழங்களாக (கனி) பழுத்துத் தொங்குகின்றன!
பறவைகள் மகிழ்ச்சியோடு வந்து பழங்களைச் சுவைக்கின்றன.
மனிதர்களும் உன் பழங்களைப் பறித்துச் செல்கிறார்கள்!"""
        
        self.show_result(is_correct, 1, explanation)
        self.level += 1
    
    def level_6(self):
        """Level 6: The Magic Cycle (சுழற்சியின் நிறைவு)"""
        self.display_level_info(
            6,
            "சுழற்சியின் நிறைவு (The Magic Cycle)",
            """பழங்கள் நன்றாகப் பழுத்துவிட்டன. 
இப்போது பலத்த காற்று வீசுகிறது. பழம் மரத்திலிருந்து கீழே விழுகிறது.
அடுத்து என்ன நடக்கும்?"""
        )
        
        options = [
            "பழம் மண்ணில் மட்கி, அதனுள் இருக்கும் விதை மீண்டும் மண்ணிற்குள் செல்லும்",
            "பழம் காணாமல் போய்விடும்"
        ]
        
        choice = self.get_choice(options)
        is_correct = (choice == 1)
        
        explanation = """♻️ பழுத்த பழம் கீழே விழுந்து, அதன் சதைப்பகுதி மண்ணோடு மட்க,
உள்ளிருந்த விதைக்கு மீண்டும் மழைநீர் கிடைக்கிறது.
அது முளைத்து மீண்டும் ஒரு புதிய மரமாக வளரத் தொடங்குகிறது!

🌍 இயற்கையின் இந்தச் சுழற்சி என்றும் முடிவற்றது!
ஒரு மரம் ஆயிரம் விதைகளை உருவாக்குகிறது.
ஆயிரம் விதைகள் ஆயிரம் மரங்களை உருவாக்குகிறது!"""
        
        self.show_result(is_correct, 1, explanation)
    
    def show_final_score(self):
        """Display final score and results"""
        self.clear_screen()
        print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🏆 விளையாட்டு முடிந்தது! 🏆{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
        
        if self.lives > 0:
            print(f"{Fore.LIGHTGREEN_EX}✅ வாழ்த்துகள்! நீ வெற்றி பெற்றாய்!{Style.RESET_ALL}\n")
            print(f"{Fore.YELLOW}🎮 விளையாட்டு முடிவு:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  👤 வீரர் பெயர்: {self.player_name}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  ⭐ மொத்த புள்ளிகள்: {self.score}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  ❤️ மீதமுள்ள உயிர்: {self.lives}{Style.RESET_ALL}\n")
            
            if self.score >= 50:
                print(f"{Fore.LIGHTGREEN_EX}🌟 அद்புத வீரர்! நீ இயற்கையின் ஞானி!{Style.RESET_ALL}")
            elif self.score >= 40:
                print(f"{Fore.LIGHTGREEN_EX}🌳 நல்ல வீரர்! இயற்கையை நன்றாக புரிந்தாய்!{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}📚 மேலும் கற்றல் தேவை. மீண்டும் விளையாடு!{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTRED_EX}❌ விளையாட்டு முடிந়துவிட்டது!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}உயிர்கள் எல்லாம் இழந்துவிட்டாய்!{Style.RESET_ALL}\n")
            print(f"{Fore.CYAN}  👤 வீரர் பெயர்: {self.player_name}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  ⭐ பெற்ற புள்ளிகள்: {self.score}{Style.RESET_ALL}\n")
            print(f"{Fore.LIGHTYELLOW_EX}மீண்டும் விளையாட முயற்சி செய்!{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
    
    def play_game(self):
        """Main game loop"""
        self.clear_screen()
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}🌳 மண்ணின் மடி முதல் மரத்தின் முடி வரை! 🌳{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        self.player_name = input(f"{Fore.LIGHTYELLOW_EX}உங்கள் பெயர் என்ன?: {Style.RESET_ALL}").strip()
        if not self.player_name:
            self.player_name = "விளையாட்டு வீரர்"
        
        print(f"\n{Fore.LIGHTGREEN_EX}நல்வரவு {self.player_name}! 🎮{Style.RESET_ALL}\n")
        input(f"{Fore.LIGHTYELLOW_EX}விளையாட்டைத் தொடங்க Enter அழுத்தவும்...{Style.RESET_ALL}")
        
        # Play all 6 levels
        levels = [self.level_1, self.level_2, self.level_3, self.level_4, self.level_5, self.level_6]
        
        for level_func in levels:
            if self.lives <= 0:
                print(f"\n{Fore.LIGHTRED_EX}😢 உயிர்கள் முடிந்துவிட்டன! விளையாட்டு முடிந்துவிட்டது!{Style.RESET_ALL}")
                break
            
            level_func()
            if self.lives > 0 and level_func != levels[-1]:
                input(f"\n{Fore.LIGHTYELLOW_EX}அடுத்த நிலைக்குச் செல்ல Enter அழுத்தவும்...{Style.RESET_ALL}")
        
        self.show_final_score()

def main():
    """Main entry point"""
    try:
        game = TreeLifeCycleGame()
        game.play_game()
        
        # Ask to play again
        while True:
            play_again = input(f"{Fore.LIGHTYELLOW_EX}மீண்டும் விளையாட விரும்புகிறீர்களா? (ஆ/இல்லை): {Style.RESET_ALL}").strip().lower()
            if play_again in ['ஆ', 'yes', 'y']:
                game = TreeLifeCycleGame()
                game.play_game()
            else:
                print(f"\n{Fore.LIGHTGREEN_EX}விளையாட்டு மற்றும் கற்றலுக்காக நன்றி! 🌳{Style.RESET_ALL}")
                print(f"{Fore.CYAN}மீண்டும் சந்திப்போம்! 👋{Style.RESET_ALL}\n")
                break
    
    except KeyboardInterrupt:
        print(f"\n\n{Fore.LIGHTYELLOW_EX}விளையாட்டு நிறுத்தப்பட்டது.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}மீண்டும் சந்திப்போம்! 👋{Style.RESET_ALL}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
