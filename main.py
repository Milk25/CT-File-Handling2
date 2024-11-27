import os

def list_directory_contents(path):
    """
    Lists and prints all files and subdirectories in the given path.
    
    Args:
        path (str): The directory path to list contents for.
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"Error: The path '{path}' is not a directory.")
            return

        # List directory contents
        print(f"\nContents of '{path}':")
        contents = os.listdir(path)
        if contents:
            for item in contents:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print(f"[DIR]  {item}")
                else:
                    print(f"[FILE] {item}")
        else:
            print("The directory is empty.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to prompt the user for a directory path and list its contents."""
    while True:
        path = input("\nEnter the directory path (or type 'exit' to quit): ").strip()
        if path.lower() == 'exit':
            print("Goodbye!")
            break
        list_directory_contents(path)

if __name__ == "__main__":
    main()