package main

import "fmt"

func main() {
	var age1 int
	age2 := 20
	fmt.Println(age2)
	fmt.Println("Как тебя зовут?")
	var name string
	fmt.Scan(&name)
	fmt.Println("Привет " + name)
	fmt.Println("Сколько тебе лет?")
	fmt.Scan(&age1)
	fmt.Println("Тебе " + fmt.Sprint(age1) + " лет")
	var xxx int8 = 16
	age1 = int(xxx)
}
