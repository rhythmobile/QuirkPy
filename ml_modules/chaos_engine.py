"""
Bangla Chaos Engine 🌀
Your first step from chaos playground to AI/ML tool

This module evolves QuirkPy into a legitimate ML tool while keeping the fun vibe.
"""

import random
import json
from typing import List, Dict

class BanglaChaosGenerator:
    """
    Generates chaotic Bangla text for:
    - Meme creation
    - Data augmentation
    - Creative writing
    - ML training datasets
    """
    
    def __init__(self):
        # Bangla text corpus - will expand with real data
        self.bangla_words = [
            "হ্যালো", "বন্ধু", "কেমন", "আছো", "বাংলা", "চমৎকার", 
            "অসাধারণ", "মজার", "কৌতুক", "ভালোবাসি", "জীবন", "আনন্দ"
        ]
        
        self.bangla_phrases = [
            "কি খবর?", "কেমন চলছে?", "বেশ ভালো!", "মজা পাচ্ছি",
            "কি অবস্থা?", "সব ঠিক আছে", "চমৎকার দিন!", "ভালো থেকো"
        ]
        
        self.emojis = ["😂", "❤️", "🔥", "✨", "🎉", "🤔", "👑", "🌟"]
    
    def chaotic_bangla_sentence(self, chaos_level: float = 0.5) -> str:
        """
        Generate a chaotic Bangla sentence with controlled randomness
        
        Args:
            chaos_level: 0.0 (normal) to 1.0 (maximum chaos)
        """
        base_phrase = random.choice(self.bangla_phrases)
        
        if chaos_level < 0.3:
            return base_phrase
        
        # Add chaos based on level
        words = base_phrase.split()
        
        # Random word replacement
        if random.random() < chaos_level:
            for i in range(len(words)):
                if random.random() < chaos_level / 2:
                    words[i] = random.choice(self.bangla_words)
        
        # Add emojis
        emoji_count = int(chaos_level * 3)
        for _ in range(emoji_count):
            words.append(random.choice(self.emojis))
            
        return ' '.join(words)
    
    def generate_meme_text(self, template: str = "random") -> Dict[str, str]:
        """
        Generate Bangla meme text in different styles
        
        Returns:
            Dict with top_text and bottom_text for memes
        """
        meme_templates = {
            "classic": {
                "top": f"{random.choice(self.bangla_words)} {random.choice(self.emojis)}",
                "bottom": f"{random.choice(self.bangla_phrases)} {random.choice(self.emojis)}"
            },
            "chaotic": {
                "top": self.chaotic_bangla_sentence(0.8),
                "bottom": self.chaotic_bangla_sentence(0.9)
            },
            "minimal": {
                "top": random.choice(self.bangla_words),
                "bottom": random.choice(self.emojis * 3)
            }
        }
        
        if template == "random":
            template = random.choice(list(meme_templates.keys()))
            
        return meme_templates.get(template, meme_templates["classic"])
    
    def create_dataset(self, size: int = 100) -> List[str]:
        """
        Create a synthetic Bangla text dataset for ML training
        
        This is where QuirkPy becomes a legitimate ML tool!
        """
        dataset = []
        for i in range(size):
            chaos_level = random.uniform(0.1, 0.9)
            text = self.chaotic_bangla_sentence(chaos_level)
            dataset.append({
                "text": text,
                "chaos_level": chaos_level,
                "length": len(text),
                "emoji_count": text.count('😂') + text.count('❤️') + text.count('🔥')
            })
        return dataset

# Quick test function
def test_bangla_chaos():
    """Test the chaos engine"""
    generator = BanglaChaosGenerator()
    
    print("🔥 Bangla Chaos Engine Test 🔥")
    print("=" * 50)
    
    # Test meme generation
    meme = generator.generate_meme_text("chaotic")
    print(f"Meme Top: {meme['top']}")
    print(f"Meme Bottom: {meme['bottom']}")
    
    # Test dataset creation
    dataset = generator.create_dataset(5)
    print(f"\nSample Dataset ({len(dataset)} items):")
    for item in dataset[:3]:
        print(f"- {item['text']} (chaos: {item['chaos_level']:.2f})")

if __name__ == "__main__":
    test_bangla_chaos()