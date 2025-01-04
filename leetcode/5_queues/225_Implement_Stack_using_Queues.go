type MyStack struct {
	stack []int
}

func Constructor() MyStack {
	return MyStack{stack: make([]int, 0)}
}

func (this *MyStack) Push(x int) {
	this.stack = append(this.stack, x)
}

func (this *MyStack) Pop() int {
	defer func() {
		this.stack = this.stack[:len(this.stack)-1]
	}()
	return this.stack[len(this.stack)-1]
}

func (this *MyStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MyStack) Empty() bool {
	return len(this.stack) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
