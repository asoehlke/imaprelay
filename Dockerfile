ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY run.sh /
COPY imaprelay /imaprelay/

# Install requirements for add-on
RUN apk add --no-cache python3

#WORKDIR /imaprelay

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]