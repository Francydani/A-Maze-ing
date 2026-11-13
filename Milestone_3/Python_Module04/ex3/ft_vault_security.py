#!/usr/bin/env python3

def secure_archive(
        name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(name, 'r') as archive:
                data = archive.read()
                return (True, data)
        elif action == "write":
            with open(name, 'w') as archive:
                archive.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    archive1 = secure_archive("/not/existing/file")
    print(
        f"Using 'secure_archive' to read from a nonexistent file:\n"
        f"({archive1[0]}, \"{archive1[1]}\")")
    print()
    archive2 = secure_archive("eso.txt", "read")
    print(
        f"Using 'secure_archive' to read from an inaccessible file:\n"
        f"({archive2[0]}, \"{archive2[1]}\")")
    print()
    archive3 = secure_archive("ancient_fragment.txt")
    print(
        f"Using 'secure_archive' to read from a regular file:\n"
        f"({archive3[0]}, \"{archive3[1]}\")")
    print()
    archive4 = secure_archive("hola", "write", "I am good")
    print(
        f"Using 'secure_archive' to write previous content to a new file:\n"
        f"({archive4[0]}, \"{archive4[1]}\")")


if __name__ == "__main__":
    main()
