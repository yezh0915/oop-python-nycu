FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

###################################### user #####################################

ENV SHELL=/bin/bash \
    USER=arg \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

###################################### basic tools #####################################

RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    locales \
    make \
    cmake \
    git \
    vim \
    gedit \
    wget \
    sudo \
    lsb-release \
    build-essential \
    net-tools \
    dirmngr \
    gnupg2 \
    mercurial \
    libopencv-dev \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libpcap-dev \
    python3-pip \
    python3-setuptools \
    python3-opencv \
    python3-numpy \
    python3-empy  \
    python3-lxml \
    python3-pymodbus \
    terminator \
    screen \
    nginx \
    openssh-server \
    libglfw3-dev \
    iputils-ping \
    libncurses5-dev \
    libgtk2.0-dev \
    libatk1.0-dev \
    libcairo2-dev \
    libx11-dev \
    libxpm-dev \
    libxt-dev \
    python3-dev \
    pybind11-dev \
    cmake \
    ctags \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

##################################### PIP3 ######################################

RUN pip3 install --upgrade pip setuptools

RUN pip3 install \
    gdown \
    virtualenv \
    pytest \
    flask \
    flask-socketio \
    jupyter \
    virtualenv \
    nbdev \
    cmake \
    numpy \
    cython \
    pandas \
    image \
    pytest-skip-slow \
    Pillow \
    matplotlib \
    tensorflow \
    tensorboard \
    pygwidgets \
    xlsxwriter

# RUN pip install \
#     torch==1.10 \
#     torchvision==0.11.1 \
#     -f https://download.pytorch.org/whl/cu111/torch_stable.html

##################################### gym #####################################
RUN python3 -m pip install --upgrade pip
RUN pip3 install swig
RUN pip3 install gymnasium[all]==0.26.2
RUN pip install gymnasium[box2d]
##################################### codon #####################################
RUN curl -v -fsSL https://exaloop.io/install.sh | bash -x
RUN export PATH=/home/${USER}/.codon/bin:$PATH

##################################### vim-python-ide ######################################
RUN git clone https://github.com/ARG-NCTU/vim-python-ide.git && \
    cd vim-python-ide && ./install.sh
####################################### pyivp ###########################################

RUN cd ${HOME} && git clone https://github.com/ARG-NCTU/pyivp.git \
    && cd pyivp \
    && make -f oop.Makefile
####################################### openai ###########################################
RUN pip install openai
####################################### pypy ###########################################
RUN apt update
RUN apt install --yes software-properties-common
RUN add-apt-repository --yes ppa:pypy/ppa
RUN apt install -y pypy3

####################################### nuitka ###########################################
RUN pip install nuitka
RUN apt install ccache

############################### pydot & grapghviz ###################################
RUN apt update
RUN apt-get update --fix-missing && \
    apt-get install graphviz -y --fix-missing
RUN pip3 install pydot
##################################### meld #####################################
RUN apt-get install meld -y
################################# cloc ripgrep #####################################
RUN apt-get install cloc -y
RUN apt-get install ripgrep -y
################################# movingpandas #####################################
RUN pip3 install movingpandas
RUN apt install libgeos-dev
RUN pip3 install hvplot
RUN pip install geoviews
RUN pip install pykdtree
RUN apt install libsnappy-dev
################################# unzip #####################################
RUN apt-get install unzip
################################# ply #####################################
RUN pip3 install ply

RUN apt-get install less
RUN pip3 install pytest-profiling
RUN apt install python3-ipdb -y
################################# sklearn #####################################
RUN pip3 install scikit-learn
################################# tkinter #####################################
RUN apt-get install -y python3-tk

RUN pip3 install mypy
################################# mkdocs #####################################
RUN pip3 install mkdocs
RUN pip3 install mkdocs-with-pdf
RUN pip3 install mkdocstrings
RUN pip3 install mkdocs-material
RUN pip3 install mkdocstrings[python]

RUN apt install tree

RUN pip3 install xdoctest
RUN pip3 install networkx[all]

RUN pip install mkdocs-mermaid2-plugin

################################# llama #####################################
RUN pip3 install llama-cpp-python

################################# git commit #####################################
RUN pip3 install xlsxwriter

##################################### setting #####################################

RUN chown -R ${USER}:${USER} ${HOME}/
RUN echo "${USER} ALL=(ALL)  NOPASSWD: ALL" > /etc/sudoers
RUN echo "export PATH=/home/${USER}/.codon/bin:$PATH" >> /home/${USER}/.bashrc
    

USER ${USER}

WORKDIR ${HOME}
