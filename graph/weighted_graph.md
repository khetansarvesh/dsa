# Template 1 : Minimum Cost Spanning Tree (MCST)

| Question | Greedy Algorithm |
|:--------:|:------------------:|
| MCST | [Prim's Algorithm](https://www.youtube.com/watch?v=kXiqvMykeJA&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=8) |





# Template 2 : Single Source Shortest Path (SSSP)

| Question | Greedy Algorithm (❌ -ve edges) | DP Algorithm (✅ -ve edges) |
|:--------:|:------------------:|:------------------:|
| SSSP | [DIJKSTRA Algorithm](https://www.youtube.com/watch?v=wjxCG6dOwcY&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=9) (similar to Prims) | [Bellman Ford Algorithm](https://www.youtube.com/watch?v=RiWE52X5wdQ&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=10) |


Related Questions : 











# Template 3 : All Pair Shortest Path (APSP)

<style>
.apsp-table {
  border-collapse: collapse;
  width: 100%;
  margin: 20px 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.apsp-table th {
  padding: 12px;
  text-align: center;
  font-weight: 600;
  border: 2px solid #2c3e50;
}
.apsp-table th:first-child {
  background-color: #34495e;
  color: white;
}
.apsp-table thead tr:first-child th:nth-child(2),
.apsp-table thead tr:first-child th:nth-child(3) {
  background-color: #3498db;
  color: white;
}
.apsp-table thead tr:first-child th:nth-child(4),
.apsp-table thead tr:first-child th:nth-child(5) {
  background-color: #9b59b6;
  color: white;
}
.apsp-table thead tr:nth-child(2) th {
  background-color: #ecf0f1;
  color: #2c3e50;
  font-size: 0.9em;
}
.apsp-table td {
  padding: 12px;
  text-align: center;
  border: 1px solid #bdc3c7;
}
.apsp-table tbody tr td:first-child {
  background-color: #ecf0f1;
  font-weight: 600;
  color: #2c3e50;
}
.apsp-table tbody tr td:nth-child(2),
.apsp-table tbody tr td:nth-child(4) {
  background-color: #fee;
  color: #c0392b;
}
.apsp-table tbody tr td:nth-child(3),
.apsp-table tbody tr td:nth-child(5) {
  background-color: #efe;
  color: #27ae60;
}
.apsp-table a {
  color: #2980b9;
  text-decoration: none;
  font-weight: 500;
}
.apsp-table a:hover {
  text-decoration: underline;
  color: #3498db;
}
</style>

<table class="apsp-table">
<thead>
<tr>
<th>Question</th>
<th colspan="2">Undirected Graph</th>
<th colspan="2">Directed Graph</th>
</tr>
<tr>
<th></th>
<th>Iterative Algorithm</th>
<th>Recursive (DP) Algorithm</th>
<th>Iterative Algorithm</th>
<th>Recursive (DP) Algorithm</th>
</tr>
</thead>
<tbody>
<tr>
<td>APSP</td>
<td>❌</td>
<td>Floyd Warshall Algorithm - <a href="https://www.youtube.com/watch?v=oNI0rf2P9gE">Logic</a> / <a href="https://www.youtube.com/watch?v=wjv-w6q4ip4">Code</a></td>
<td>❌</td>
<td>Floyd Warshall Algorithm</td>
</tr>
</tbody>
</table>