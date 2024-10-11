
class App:
    @staticmethod
    def start() -> None:
        print("Welcome to my App. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                print("Unknown command. Type 'exit' to exit.")

        
