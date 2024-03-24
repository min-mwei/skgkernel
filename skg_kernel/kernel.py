import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from ipykernel.ipkernel import IPythonKernel

class SKGKernel(IPythonKernel):
    implementation = 'SKG'
    implementation_version = '1.0'
    language = 'python'
    banner = "SKG kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        logger.info("audit logged:", code)
        return super().do_execute(code, silent, store_history, user_expressions, allow_stdin)
