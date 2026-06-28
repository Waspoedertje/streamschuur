import json
import os

print("=" * 50)
print("🏚️  Welcome to Streamschuur")
print("Build your own streaming identity")
print("=" * 50)
print()

branding = {}

branding["name"] = input("Streaming service name: ").strip()

print()

branding["welcome"] = input("Welcome message: ").strip()

print()

branding["tagline"] = input("Tagline (optional): ").strip()

print()

print("Accent color")
print("1. Red")
print("2. Blue")
print("3. Green")
print("4. Purple")
print("5. Orange")
print("6. Custom")

choice = input("> ").strip()

colors = {
    "1": "#c62828",
    "2": "#1565c0",
    "3": "#2e7d32",
    "4": "#6a1b9a",
    "5": "#ef6c00"
}

if choice == "6":
    branding["accent"] = input("Hex color (#xxxxxx): ").strip()
else:
    branding["accent"] = colors.get(choice, "#c62828")

print()

branding["logo"] = input("Logo URL or file: ").strip()

branding["banner"] = input("Banner URL or file: ").strip()

branding["background"] = input("Background URL or file: ").strip()

branding["favicon"] = input("Favicon URL or file: ").strip()

branding["mascot"] = input("Mascot URL or file: ").strip()

print()

branding["powered_by_jellyfin"] = True

branding["theme"] = "streamschuur"

branding["version"] = "0.1"

branding["generator"] = "Streamschuur Wizard"

branding["fun_mode"] = input("Enable Fun Mode? (y/n): ").lower() == "y"

os.makedirs("output", exist_ok=True)

with open("output/branding.json", "w", encoding="utf-8") as f:
    json.dump(branding, f, indent=4)

print()
print("✅ branding.json created!")
print()
print("Next step:")
print("Generate custom.css from branding.json")
