// First, we show that Fib(n)=ϕn−ψn5–√,
// where ψ=1−5–√2 using strong induction.
// Fib(0)=0 and ϕ0−ψ05–√=0
// Fib(1)=1 and ϕ1−ψ15–√=12(1+5–√−1+5–√)5–√=1
// So the statement is true for n=0,1. Given n≥1,
// assume the proposition to be true for 0,1,…,n.
// Fib(n+1)=Fib(n)+Fib(n−1)=ϕn−ψn+ϕn−1−ψn−15–√
// =ϕn−1(ϕ+1)−ψn−1(ψ+1)5–√
// =ϕn−1(ϕ2)−ψn−1(ψ2)5–√=ϕn+1−ψn+15–√, so the statement is true.
// Notice that since |ψ|<1 and 5–√>2, one has ∣∣∣ψn5–√∣∣∣<12
// Then the integer closest to Fib(n)+ψn5–√=ϕn5–√ is Fib(n). 
