FROM --platform=linux/amd64 nvidia/cuda:11.8.0-runtime-ubuntu18.04

# Set default shell to /bin/bash
SHELL ["/bin/bash", "-cu"]

ENV USER_NAME=ismayilz
ENV HOME=/home/${USER_NAME}
ENV CONDA_PREFIX=${HOME}/.conda
ENV CONDA=${CONDA_PREFIX}/condabin/conda
ENV REPO_DIR=${HOME}/project-morphgen
ENV CONDA_ENV=morphgen

WORKDIR /

# Install dependencies
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt update && apt install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
        build-essential \
        gcc-8 \
        g++-8 \
        cmake \
        git \
        curl \
        vim \
        unzip \
        wget \
        tmux \
        screen \
        ca-certificates \
        apt-utils \
        libjpeg-dev \
        libpng-dev \
        sudo \
        htop \
        apt-transport-https \
        gnupg \
        protobuf-compiler

# Set up bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
RUN mv bazel-archive-keyring.gpg /usr/share/keyrings
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
RUN apt update && apt install bazel-5.4.1
RUN ln -sf /usr/bin/bazel-5.4.1 /usr/bin/bazel
RUN ln -sf /usr/bin/gcc-8 /usr/bin/gcc
RUN ln -sf /usr/bin/g++-8 /usr/bin/g++

# Set up user
RUN --mount=type=secret,id=my_env source /run/secrets/my_env && \
    groupadd -g ${GROUP_ID} ${GROUP_NAME} && \
    groupadd -g ${NLP_GROUP_ID} ${NLP_GROUP_NAME} && \
    useradd -r -m -d /home/${USER_NAME} -s /bin/bash -g ${GROUP_ID} -G ${NLP_GROUP_NAME},sudo -u ${USER_ID} ${USER_NAME} && \
    # Change the password to make root > user
    echo -e "${USER_NAME}\n${USER_NAME}" | passwd ${USER_NAME}

# Install OpenSSH for MPI to communicate between containers
RUN apt-get update && apt-get install -y --no-install-recommends openssh-client openssh-server && \
    mkdir -p /var/run/sshd
# RUN echo 'root:root' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22

# Prepare the NFS mount folders
RUN mkdir /mnt/nlpdata1
RUN mkdir /mnt/scratch

# Git configuration (optional, you can also use a repo saved in the NFS)
RUN --mount=type=secret,id=my_env source /run/secrets/my_env && \
    git config --global user.name ${GITHUB_NAME}
RUN --mount=type=secret,id=my_env source /run/secrets/my_env && \
    git config --global user.email ${GITHUB_EMAIL}
RUN git config --global pull.rebase false

# Switch to home directory
WORKDIR ${HOME}
USER ${USER_NAME}

# Install conda (optional)
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
RUN bash miniconda.sh -b -p ${CONDA_PREFIX}
RUN ${CONDA} config --set auto_activate_base false
RUN ${CONDA} init bash
RUN ${CONDA} create -y --name ${CONDA_ENV} python=3.9

# Set up turkish morphology repo
# modified MANIFEST.in
RUN git clone git@github.com:mismayil/turkish-morphology.git
WORKDIR ${HOME}/turkish-morphology
RUN ${CONDA} run -n ${CONDA_ENV} bazel build //...
RUN ${CONDA} run -n ${CONDA_ENV} bazel-bin/setup install

WORKDIR ${HOME}

# Check if turkish morphology correctly installed
RUN ${CONDA} run -n ${CONDA_ENV} python -c "from turkish_morphology import decompose, analyze"

# Set up datatrove
# downgraded to 3.9
RUN git clone git@github.com:mismayil/datatrove.git
WORKDIR ${HOME}/datatrove
RUN ${CONDA} run -n ${CONDA_ENV} pip install -e ".[dev]"

WORKDIR ${HOME}

# Setup github repo dependencies
COPY --chown=${USER_NAME} ./requirements.txt .
RUN ${CONDA} run -n ${CONDA_ENV} pip install -r ./requirements.txt
RUN ${CONDA} run -n ${CONDA_ENV} pip install ipykernel ipywidgets

COPY --chown=${USER_NAME} ./docker/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

USER root

# ENTRYPOINT ["./entrypoint.sh"]
# ENTRYPOINT [ "sleep", "infinity" ]
ENTRYPOINT ["/usr/sbin/sshd", "-D"] 