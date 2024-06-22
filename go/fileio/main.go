package main

import (
	"fmt"
	"os"
)

func main() {
	dat, _ := os.OpenFile("../go.mod", os.O_RDONLY, 0644)

	n := make([]byte, 100)

	reads, _ := dat.Read(n)
	fmt.Print((reads))
}
