package gochan

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

// 需求: 多个协程并发查询数据,并将结果汇总到一个切片中
func getDataBat() []string {
	var wg sync.WaitGroup
	ret := make([]string, 0)
	dataChan := make(chan string, 10)
	go func() {
		for v, ok := <-dataChan; ok; {
			ret = append(ret, v)
		}
	}()
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(p int) {
			defer wg.Done()
			list := getData(p)
			for _, v := range list {
				dataChan <- v
			}
		}(i)
	}

	return ret
}

func getData(p int) []string {
	ret := []string{}
	for i := 0; i < p; i++ {
		ret = append(ret, fmt.Sprintf("id:%d; data-index:%d", p, i))
	}
	time.Sleep(time.Millisecond * 500)
	return ret
}

func Test_getDataBat(t *testing.T) {
	resMapp := getDataBat()
	fmt.Println(resMapp)
}

func TestRun(t *testing.T) {
	ch1 := make(chan string, 10)
	ch1 <- "111"
	ch1 <- "222"
	ch1 <- "333"
	go func() {
		ch1 <- "444"
		ch1 <- "555"
		time.Sleep(time.Second * 3)
		ch1 <- "666"
		close(ch1)
	}()
	for {
		v, ok := <-ch1
		fmt.Println(v, ok)
		if !ok {
			break
		}
	}
}
