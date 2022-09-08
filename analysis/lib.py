import importlib
import os


def pick_backend_tables():
    backend = os.environ.get("OPENSAFELY_BACKEND", "tpp")
    if backend == "expectations":
        backend = "tpp"
    tables = importlib.import_module(f"databuilder.tables.beta.{backend}")
    return tables.patients,
