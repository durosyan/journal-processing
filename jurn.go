package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	// Define command line arguments
	filePath := flag.String("file", "", "Path to the template file")
	// entryTitle := flag.String("title", "", "Entry title")
	verbose := flag.Bool("verbose", false, "Enable verbose mode")

	// Parse command line arguments
	flag.Parse()

	if *filePath == "" {
		fmt.Println("Error: -file argument is required")
		flag.Usage()
		os.Exit(1)
	}

	// Resolve the file path
	absFilePath, err := filepath.Abs(*filePath)
	if err != nil {
		fmt.Println("Error resolving file path:", err)
		os.Exit(1)
	}

	// Access the parsed arguments
	fmt.Println("File Path:", *filePath)
	fmt.Println("Verbose Mode:", *verbose)

	// Read the file
	content, err := os.Open(absFilePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Read the file content
	fileContent := make([]byte, 1024)
	_, err = content.Read(fileContent)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Print the file content
	fmt.Println(string(fileContent))
}
