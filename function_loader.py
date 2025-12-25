import importlib
import inspect

def execute_function(func_name: str, params: dict, methodname: str):  # Parameters from the server are entered here
    try:
        module = importlib.import_module(f"functions.{func_name}")
    except ModuleNotFoundError:
        return {"error": "Function not found"}
    # check framework in method
    if not hasattr(module, methodname):
        return {"error": f"Method '{methodname}' not found"}

    method = getattr(module, methodname)

    if not callable(method):
        return {"error": "Selected attribute is not callable"}

    sig = inspect.signature(method)
    if len(sig.parameters) == 0:  # If the function does not take parameters
        return method()

    
    if not params:  # A function that requires arguments, or parameters, will return an error if no arguments are provided
        return {"error": "This method requires parameters"}

    try:
        bound = sig.bind(**params)
        bound.apply_defaults()
    except TypeError as e:
        return {"error": str(e)}

    return method(**bound.arguments)
