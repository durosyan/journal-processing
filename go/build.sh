# apple cannot run the binary because it might be MaLwArEz..
APP_NAME=jrnl GOOS=darwin GOARCH=arm64 go build -o bin/jrnl-darwin-arm64 new.go