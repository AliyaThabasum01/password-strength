from getpass import getpass
from checker import check_strength

password = getpass("Enter password: ")

score, feedback = check_strength(password)

print("\n🔐 Password Strength")
print("=" * 35)
print(f"Score: {score}/5")

print("\nFeedback:")
for item in feedback:
    print(f"• {item}")
