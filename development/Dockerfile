FROM python:3.9

ENV ROOT_PASSWORD root

WORKDIR /app

RUN apt update && apt install -y openssh-server
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "root:$ROOT_PASSWORD" | chpasswd
RUN mkdir /run/sshd

EXPOSE 22
EXPOSE 8000

CMD ["/usr/sbin/sshd", "-D"]
