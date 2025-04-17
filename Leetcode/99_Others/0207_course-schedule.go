// https://leetcode.cn/problems/top-k-frequent-elements/solutions/
// m

// https://leetcode.cn/problems/course-schedule/solutions/250377/bao-mu-shi-ti-jie-shou-ba-shou-da-tong-tuo-bu-pai-/

package main

func canFinish(numCourses int, prerequisites [][]int) bool {
	// inDegree[i] represents the number of prerequisites for course i
	inDegree := make([]int, numCourses)

	// post stores the adjacency list: post[pre] = list of courses that depend on 'pre'
	post := map[int][]int{}

	// Build the graph and compute in-degrees
	for _, pair := range prerequisites {
		cur, pre := pair[0], pair[1]
		inDegree[cur]++                    // Increment in-degree for current course
		post[pre] = append(post[pre], cur) // Add edge: pre → cur
	}

	// Initialize a queue with all courses having in-degree of 0 (no prerequisites)
	queue := []int{}
	for i := 0; i < numCourses; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	count := 0 // Count of courses that can be completed

	// Perform topological sort using BFS (Kahn's algorithm)
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		count++

		// Decrease the in-degree of all adjacent courses
		for _, next := range post[cur] {
			inDegree[next]--
			if inDegree[next] == 0 {
				queue = append(queue, next) // Add to queue if it's ready to be taken
			}
		}
	}

	// If we've completed all courses, return true
	return count == numCourses
}
