from conversation_flow import run_conversation

def main():
    final_draft, _ = run_conversation()
    print("# 📘 Final Content Output in Markdown Format\n")
    print(final_draft)

if __name__ == "__main__":
    main()
