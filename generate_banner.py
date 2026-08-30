#!/usr/bin/env python3
"""
Generate animated GIF banner for GitHub profile
Run: python generate_banner.py
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
except ImportError:
    print("Install required packages: pip install Pillow")
    exit(1)

def create_animated_banner():
    """Create an animated banner GIF"""
    
    # Banner config
    width, height = 1200, 200
    frames = []
    colors = [
        (6, 182, 212),      # Cyan
        (99, 102, 241),     # Indigo
        (236, 72, 153),     # Pink
        (249, 115, 22),     # Orange
        (168, 85, 247),     # Purple
    ]
    
    text = "Krishnanunni H Pillai"
    subtitle = "AI/ML Engineer • Full-Stack Developer • Data Scientist"
    
    # Create frames for animated banner
    for frame_idx in range(len(colors) * 2):
        # Create new image
        img = Image.new('RGB', (width, height), color=(15, 23, 42))  # Dark background
        draw = ImageDraw.Draw(img)
        
        # Determine color for this frame
        color_idx = frame_idx % len(colors)
        current_color = colors[color_idx]
        
        # Draw gradient-like effect by drawing rectangles
        rect_width = width // 5
        for i in range(5):
            alpha_idx = (i + frame_idx) % len(colors)
            color = colors[alpha_idx]
            draw.rectangle(
                [(i * rect_width, 0), ((i + 1) * rect_width, 20)],
                fill=color
            )
        
        # Add text
        try:
            # Try to use a nice font
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        except:
            # Fallback to default font
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Draw main text with current color
        text_bbox = draw.textbbox((0, 0), text, font=font_large)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (width - text_width) // 2
        text_y = 40
        
        draw.text((text_x, text_y), text, fill=current_color, font=font_large)
        
        # Draw subtitle in white
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = 120
        
        draw.text((subtitle_x, subtitle_y), subtitle, fill=(226, 232, 240), font=font_small)
        
        frames.append(img)
    
    # Save as GIF
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    frames[0].save(
        'assets/banner.gif',
        save_all=True,
        append_images=frames[1:],
        duration=500,  # 500ms per frame
        loop=0
    )
    
    print("✅ Animated banner created: assets/banner.gif")
    print("💡 Add to README with: ![Banner](assets/banner.gif)")

def create_skill_badges():
    """Create skill visualization"""
    
    skills = [
        ("Python", 95),
        ("JavaScript", 90),
        ("Machine Learning", 88),
        ("Full-Stack Dev", 90),
        ("System Design", 82),
    ]
    
    width, height = 400, 300
    img = Image.new('RGB', (width, height), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Title
    draw.text((20, 10), "Skills & Proficiency", fill=(6, 182, 212), font=font)
    
    y = 50
    for skill, percentage in skills:
        # Skill name
        draw.text((20, y), skill, fill=(226, 232, 240), font=font_small)
        
        # Progress bar background
        bar_width = 350
        bar_height = 12
        draw.rectangle(
            [(20, y + 25), (20 + bar_width, y + 25 + bar_height)],
            outline=(99, 102, 241),
            fill=(31, 41, 55)
        )
        
        # Progress bar fill
        fill_width = int((percentage / 100) * bar_width)
        draw.rectangle(
            [(20, y + 25), (20 + fill_width, y + 25 + bar_height)],
            fill=(6, 182, 212)
        )
        
        # Percentage text
        draw.text((375, y + 20), f"{percentage}%", fill=(236, 72, 153), font=font_small)
        
        y += 50
    
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    img.save('assets/skills.png')
    print("✅ Skills visualization created: assets/skills.png")
    print("💡 Add to README with: ![Skills](assets/skills.png)")

if __name__ == "__main__":
    print("🎨 Generating GitHub profile assets...\n")
    
    try:
        create_animated_banner()
        print()
        create_skill_badges()
        print("\n✨ All assets generated successfully!")
        print("\n📋 Next steps:")
        print("1. Commit assets/ folder to your GitHub profile repo")
        print("2. Add to README.md:")
        print("   ![Banner](assets/banner.gif)")
        print("   ![Skills](assets/skills.png)")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you have PIL/Pillow installed: pip install Pillow")
