FROM nvidia/cuda:11.6.0-devel-ubuntu20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get update && apt-get install -y wget git curl build-essential
RUN apt-get install -y python3-pip

WORKDIR /home/biolib

RUN pip -q install git+https://github.com/sokrypton/ColabDesign.git@v1.1.0
RUN pip3 install -qU setuptools cuda-python
RUN pip3 install -qU biopython dm-haiku==0.0.5 py3Dmol ml-collections==0.1.0 tqdm matplotlib 
RUN pip3 install -qU tensorflow tbp-nightly dm-tree

RUN pip3 install --upgrade jax==0.2.14
RUN pip3 install --upgrade "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.4.0.27-1+cuda11.6_amd64.deb
RUN apt install ./libcudnn8_8.4.0.27-1+cuda11.6_amd64.deb


COPY run.py run.py
COPY example.fasta example.fasta
COPY example.pdb example.pdb
