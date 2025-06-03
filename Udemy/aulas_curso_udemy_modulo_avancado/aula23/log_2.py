from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log_2.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')

class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(msg_formatada)
        with open(LOG_FILE, 'a') as arquivo_2:
            arquivo_2.write(msg_formatada)
            arquivo_2.write('\n')

l1 = LogFileMixin()
l1.log_error('Erro grave!!')
l1.log_success('Sucesso Mulecote!!')
    

