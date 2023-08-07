def test_virtual_environment():
    import sys

    print("Python version:")
    print(sys.version)

    print("\nVirtual environment:")
    print("Is virtual environment? ", hasattr(sys, 'real_prefix'))
    print("Virtual environment path: ", sys.prefix)


if __name__ == "__main__":
    test_virtual_environment()
