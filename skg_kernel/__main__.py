from ipykernel.kernelapp import IPKernelApp
from . import SKGKernel

IPKernelApp.launch_instance(kernel_class=SKGKernel)
