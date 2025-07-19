

from agent_graph import graph

def main():
    print("LangGraph Math Agent Ready!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ('exit', 'quit'):
            break

        result = graph.run({'query': user_input})
        print("\nAgent:", result)

if __name__ == "__main__":
    main()
