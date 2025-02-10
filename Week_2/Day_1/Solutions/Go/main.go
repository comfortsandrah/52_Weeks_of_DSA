package main

import "fmt"

type MyStack struct {
	queue1 []int
	queue2 []int
}

func (this *MyStack) enqueue(queue *[]int, x int) {
	*queue = append(*queue, x)
}

func (this *MyStack) dequeue(queue *[]int) (int, []int) {
	if len(*queue) == 0 {
		return 0, nil
	}

	element := (*queue)[0]
	newQueue := (*queue)[1:]

	return element, newQueue
}

func Constructor() MyStack {
	this := MyStack{}
	return this
}

func (this *MyStack) Push(x int) {
	this.enqueue(&this.queue1, x)
}

func (this *MyStack) Pop() int {
	if len(this.queue1) == 0 {
		return -1
	}

	for len(this.queue1) > 1 {
		newInt, newQueue := this.dequeue(&this.queue1)
		this.queue1 = newQueue
		this.enqueue(&this.queue2, newInt)
	}

	newInt2 := this.queue1[0]

	this.queue1 = this.queue2
	this.queue2 = []int{}

	return newInt2
}

func (this *MyStack) Top() int {
	if len(this.queue1) == 0 {
		return -1
	}

	for len(this.queue1) > 1 {
		newInt, newQueue := this.dequeue(&this.queue1)
		this.queue1 = newQueue
		this.enqueue(&this.queue2, newInt)
	}

	newInt2 := this.queue1[0]

	this.enqueue(&this.queue2, newInt2)

	this.queue1 = this.queue2
	this.queue2 = []int{}

	return newInt2
}

func (this *MyStack) Empty() bool {
	return len(this.queue1) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

func main() {
	obj := Constructor()
	obj.Push(1)
	obj.Push(2)
	fmt.Println(obj.Top()) // Should print 2
	fmt.Println(obj.Pop()) // Should print 2
	fmt.Println(obj.Empty())
}
