import yaml


languages = [
    "es"
]


def main() -> None:
    for language in languages:
        file_name = f"global_mmlu_{language}.yaml"
        try:
            with open(f"{file_name}", "w") as f:
                f.write("# Generated by _generate_configs.py\n")
                yaml.dump(
                    {
                        "include": "_default_yaml",
                        "task": f"global_mmlu_{language}",
                        "dataset_name": language,
                    },
                    f,
                )
        except FileExistsError:
            pass


if __name__ == "__main__":
    main()
