package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"time"
)

func main() {
	// Define command line arguments
	pwd, err := os.Getwd()
	filePath := flag.String("template", "", "Path to the template file")
	entryTitle := flag.String("title", "", "Entry title")
	outputDir := flag.String("output", pwd, "Output directory")
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

	// Resolve the output directory
	absOutputDir, err := filepath.Abs(*outputDir)
	if err != nil {
		fmt.Println("Error resolving output directory:", err)
		os.Exit(1)
	}

	// Access the parsed arguments
	if *verbose {
		fmt.Println("Verbose Mode:", *verbose)
		fmt.Println("Entry Title:", *entryTitle)
		fmt.Println("File Path:", absFilePath)
	}

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

	// Get current date and time
	date := time.Now().Format("150402012006")

	// Create the output file
	outputFile, err := os.Create(filepath.Join(absOutputDir, "Entry_"+date+".md"))
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}

	// Write the entry title to the output file
	_, err = outputFile.WriteString(fmt.Sprintf("--- \n%s\n", *entryTitle))
	if err != nil {
		fmt.Println("Error writing title to output file:", err)
		return
	}
}
