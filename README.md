# Notifier

Simple telegram notifier. Right now it can lose your massage.

## Build:
```docker build -t notifier .```

## Run:
```
sudo docker run --rm -d -p 8888:8080 \
    --env TELEGRAM_TOKEN=<telegram_token> \
    -v $(pwd)/config.json:/usr/src/app/config.json \
    --name=notifier \
    registry.gitlab.com/roxpy/notifier:<tag>
```
