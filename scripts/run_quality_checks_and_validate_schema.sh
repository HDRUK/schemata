python scripts/validate_schema.py --schema tools --json examples/tools/test/tools_test.json
python scripts/validate_schema.py --schema project --json examples/project/test/project_test.json
python scripts/validate_schema.py --schema person --json examples/person/test/person_test.json

python scripts/quality_checks.py --schema tools --json examples/tools/test/tools_test.json
python scripts/quality_checks.py --schema project --json examples/project/test/project_test.json
python scripts/quality_checks.py --schema person --json examples/person/test/person_test.json
