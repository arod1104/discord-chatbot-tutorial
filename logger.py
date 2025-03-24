class Logger:
    def __init__(self):
        pass
        
    def log(self, message) -> str:
        print(message)

    def log_error(self, message) -> str:
        print(f'Error: {message}')
