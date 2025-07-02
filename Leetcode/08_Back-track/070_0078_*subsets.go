// https://leetcode.com/problems/subsets/
// m

package backtrack

// 求子集问题和 77.组合 和 131.分割回文串 又不一样了。
// 如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，那么:
// 组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！
// 看下代码随想录：
// https://programmercarl.com/0078.%E5%AD%90%E9%9B%86.html#%E6%80%9D%E8%B7%AF

func subsets(nums []int) (ans [][]int) {
	var path []int
	var bt func(int)
	bt = func(index int) {
		// 每次递归进入时，把当前 path 加入答案中
		// 因为每个路径都是一个子集（包括空集）
		ans = append(ans, append([]int{}, path...))

		// 这个回溯的终止就是 for 循环结束
		// 以 nums=[1,2,3] 为例，当 i=2 的时候
		// path = append(path, 3)
		// 然后进入 bt(3) 后，并不会开始 for 循环 因为 i=3，已经不满足 i < len(nums) 了
		for i := index; i < len(nums); i++ {
			path = append(path, nums[i])
			bt(i + 1)
			path = path[:len(path)-1]
		}
		// 当 i >= len(nums) 时，for 循环自动退出，相当于「递归终止条件」
	}
	bt(0)
	return
}
