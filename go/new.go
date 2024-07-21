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
	entryTitle := flag.String("title", "", "Entry title")
	outputDir := flag.String("output", pwd, "Output directory")
	verbose := flag.Bool("verbose", false, "Enable verbose mode")

	// Parse command line arguments
	flag.Parse()

	// Resolve the output directory
	absOutputDir, err := filepath.Abs(*outputDir)
	if err != nil {
		fmt.Println("Error resolving output directory:", err)
		os.Exit(1)
	}

	// define title
	if *entryTitle == "" {
		// ask the user for the title
		fmt.Print("Enter the title of the entry: ")
		fmt.Scanln(entryTitle)
	}

	// define mood
	var mood string
	fmt.Print("Enter the mood of the entry between 0 and 100: ")
	fmt.Scanln(&mood)

	// Access the parsed arguments
	if *verbose {
		fmt.Println("Verbose Mode:", *verbose)
		fmt.Println("Entry Title:", *entryTitle)
	}

	// Create the output file
	outputFile, err := os.Create(filepath.Join(absOutputDir, "Entry_"+time.Now().Format("150402012006")+".md"))
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}

	// Write the entry title to the output file
	// Write the entry title and date to the output file
	_, err = outputFile.WriteString(fmt.Sprintf("--- \nTitle: %s\nDate: %s\nMood: %s\n---\n", *entryTitle, time.Now().Format("1504 02/01/2006"), mood))
	if err != nil {
		fmt.Println("Error writing title to output file:", err)
		return
	}
}
