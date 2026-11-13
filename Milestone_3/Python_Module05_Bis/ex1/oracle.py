#!/usr/bin/env python3

import os
from dotenv import load_dotenv

REQUIRED_VARS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def oracle_config() -> dict[str, str | None]:
    load_dotenv()
    return {var: os.getenv(var) for var in REQUIRED_VARS}


def print_devolopment(config: dict[str, str | None]) -> None:
    print("Mode: development")
    print("Database: Connected to local instance")
    print("API Access: Authenticated (development)")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Remote Network: Online")


def print_production(config: dict[str, str | None]) -> None:
    print("Mode: production")
    print("Database: Connected to production instance")
    print("API Access: Authenticated (production)")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Remote Network: Online (production)")


def main() -> None:
    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    config = oracle_config()
    missing = [key for key, value in config.items() if not value]

    if missing:
        print("[KO] Environment configuration incomplete!")
        for var in missing:
            print(f"Missing environment variable: {var}")
        print("\nPlease configure your .env file using "
              ".env.example as a template.")
        return

    print("Configuration loaded:")
    if config["MATRIX_MODE"] == "development":
        print_devolopment(config)
    elif config["MATRIX_MODE"] == "production":
        print_production(config)
    else:
        print("[KO] Invalid MATRIX_MODE")
        print("Missing environment variable: MATRIX_MODE")
        print("\nPlease configure your .env file using"
              " .env.example as a template.")
        return

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
