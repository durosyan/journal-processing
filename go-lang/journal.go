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

	"gopkg.in/yaml.v2"
)

func main() {
	// Define command line arguments
	pwd, err := os.Getwd()
	if err != nil {
		fmt.Println("Error getting current working directory:", err)
		os.Exit(1)
	}
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
	titleInput, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal("Error reading title input:", err)
	}
	entryTitle := strings.TrimSpace(titleInput)

	// define mood
	fmt.Print("Enter the mood of the entry between 0 and 100: ")
	moodInput, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal("Error reading mood input:", err)
	}
	mood := strings.TrimSpace(moodInput)

	// Access the parsed arguments
	if *verbose {
		fmt.Println("Verbose Mode:", *verbose)
		fmt.Println("Entry Title:", entryTitle)
		fmt.Println("Mood:", mood)
		fmt.Println("Output Directory:", absOutputDir)
	}

	// Create the output file
	outputFile, err := os.Create(filepath.Join(
		absOutputDir,
		"Entry_"+time.Now().Format("150402012006")+".md"))
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}

	// Write the entry title and date to the output file
	_, err = outputFile.WriteString(
		fmt.Sprintf("--- \nTitle: %s\nDate: %s\nMood: %s\n---\n",
			entryTitle,
			time.Now().Format("1504 02/01/2006"),
			mood))
	if err != nil {
		fmt.Println("Error writing title to output file:", err)
		return
	}
}

// Metadata holds the metadata fields
type Metadata struct {
	Mood  string `yaml:"Mood"`
	Title string `yaml:"Title"`
	Date  string `yaml:"Date"`
}

// readMetadata reads the metadata from a markdown file
func readMetadata(filepath string) (Metadata, error) {
	var metadata Metadata

	// Open the markdown file
	file, err := os.Open(filepath)
	if err != nil {
		return metadata, err
	}
	defer file.Close()

	// Read the file line by line
	scanner := bufio.NewScanner(file)
	var yamlLines []string
	inMetadata := false

	for scanner.Scan() {
		line := scanner.Text()
		if strings.TrimSpace(line) == "---" {
			if inMetadata {
				break
			}
			inMetadata = true
			continue
		}
		if inMetadata {
			yamlLines = append(yamlLines, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return metadata, err
	}

	// Parse the YAML front matter
	yamlContent := strings.Join(yamlLines, "\n")
	err = yaml.Unmarshal([]byte(yamlContent), &metadata)
	if err != nil {
		return metadata, err
	}

	return metadata, nil
}
