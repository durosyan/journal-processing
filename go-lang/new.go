package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"
)

func main() {
	// Define command line arguments
	pwd, err := os.Getwd()
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

	reader := bufio.NewReader(os.Stdin)

	// define title
	fmt.Print("Enter the title of the entry: ")
	titleInput, err := reader.ReadString('\n') // Read the entire line
	if err != nil {
		log.Fatal("Error reading title input:", err)
	}
	entryTitle := strings.TrimSpace(titleInput) // Trim newline character

	// define mood
	fmt.Print("Enter the mood of the entry between 0 and 100: ")
	moodInput, err := reader.ReadString('\n') // Read the entire line
	if err != nil {
		log.Fatal("Error reading mood input:", err)
	}
	mood := strings.TrimSpace(moodInput) // Trim newline character

	// Access the parsed arguments
	if *verbose {
		fmt.Println("Verbose Mode:", *verbose)
		fmt.Println("Entry Title:", entryTitle)
	}

	// Create the output file
	outputFile, err := os.Create(filepath.Join(absOutputDir, "Entry_"+time.Now().Format("150402012006")+".md"))
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}

	// Write the entry title to the output file
	// Write the entry title and date to the output file
	_, err = outputFile.WriteString(fmt.Sprintf("--- \nTitle: %s\nDate: %s\nMood: %s\n---\n", entryTitle, time.Now().Format("1504 02/01/2006"), mood))
	if err != nil {
		fmt.Println("Error writing title to output file:", err)
		return
	}
}
