# Go compiler
GO := go

# Build the project
build:
	$(GO) build -o journal.bin

# Run the project
run:
	$(GO) run journal.go

# Clean the project
clean:
	rm -f journal

# Test the project
test:
	$(GO) test ./...

# Install project dependencies
deps:
	$(GO) mod download

.PHONY: build run clean test deps