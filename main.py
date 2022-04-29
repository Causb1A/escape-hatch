from my_app import module_1
import sys

if __name__ == "__main__":
    """
    Main function that runs the application
    """
    try:
        module_1.run()

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception:
        raise Exception
