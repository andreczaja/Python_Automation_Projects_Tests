class Log:
    def _log(self, msg):
        return NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')
    

class LogFileMixin(Log):
    def _log(self,msg):
        print(f'{msg}, {self.__class__.__name__}')

if __name__ == '__main__':
    l1 = LogFileMixin()
    l1.log_error("404")