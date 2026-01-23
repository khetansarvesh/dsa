# Template 1 : Traversal / Searching

<table style="width: 100%; border-collapse: collapse;">



<thead>
<tr>
<th>Question</th>
<th colspan="2">Undirected Graph</th>
<th colspan="2">Directed Graph</th>
</tr>
<tr>
<th></th>
<th>Iterative Algorithm</th>
<th>Recursive Algorithm</th>
<th>Iterative Algorithm</th>
<th>Recursive Algorithm</th>
</tr>
</thead>

<tbody>
<tr>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">📌 TEMPLATE: Traversal / Searching</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">BFS -- <a href="https://www.youtube.com/watch?v=dCvnjapI6ik&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=2">Logic</a> / Code </td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">DFS -- <a href="https://www.youtube.com/watch?v=0ql7lZS2qt0&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=3">Logic</a> / Code </td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">BFS</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">DFS</td>
</tr>
</tbody>

<tbody>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳ Has path or not</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://youtu.be/ZwGC60Ao6bQ?list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&t=1309">BFS</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=ZwGC60Ao6bQ&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=9">DFS</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">BFS</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">DFS</td>
</tr>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳ Cycle detection</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=UPfUFoWjk5w">DFS</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=GLxfoaZlRqs">DFS</a></td>
</tr>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳ Find #connected components</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=rNQDP92wWFI&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=36">logic</a> / <a href="https://www.youtube.com/watch?v=tLZrercDRww&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=37">code</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
</tr>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳ Topological sort</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=Zbbe9FYVnM4&list=PLUcsbZa0qzu1EhwPcQfbDfl9VitpSUgBp&index=7">DFS</a></td>
</tr>

</tbody>
</table>

Now for a given question both interative approach or recursive appraoch is possible (as shown for few question above) but in most cases thinking about recursive approach is easy compared to iterative approach. Hence we should always try to solve using recursion.

<br><br><br>



















# Template 2 : [BFS / DFS on Matrix (Matrix as Graph)](https://www.youtube.com/watch?v=V5flGFnlulQ&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=28)
Here it is easier to think in terms of DFS so we will use only that to solve all the questions. But keep in mind that all these questions can be solved using BFS also.

<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Question</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Undirected Graph</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Directed Graph</th>
</tr>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"></th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative (BFS) Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive (DFS) Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative (BFS) Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive (DFS) Algorithm</th>
</tr>
</thead>
<tbody>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">📌 TEMPLATE:Flood Fill </td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=ExyjnY_dU1c&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=29">logic</a> / <a href="https://www.youtube.com/watch?v=rIxAWaNZ9bo&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=30">code</a></td>
</tr>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳#Islands </td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">❌</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=YXVFqphuGLU&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=31">logic /code</a> </td>
</tr>

</tbody>
</table>

<br><br><br>





















# Template 3 : Single Source Shortest Path (SSSP)

<table style="text-align: center;">
<thead>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Question</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Undirected Graph</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Directed Graph</th>
</tr>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"></th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive Algorithm</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">📌 TEMPLATE: SSSP</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">BFS gives SSSP</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">BFS</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">⚪</td>

</tr>
<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳ Snake and ladder problem</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=8WZA471fV7g&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=39">Logic</a> / <a href="https://www.youtube.com/watch?v=N7OhwS_nzhg&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=40">Code</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
</tr>

<tr>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">↳Steps by Knight </td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=hywcrLz1T14&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=10">logic</a> / <a href="https://www.youtube.com/watch?v=aS4DwjqfMfI&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=11">code</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">⚪</td>
</tr>

</tbody>
</table>
Here we cannot use DFS since only BFS gives SSSP.

<br><br><br>
















# Template 4 : All Pair Shortest Path (APSP)

<table style="text-align: center;">
<thead>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Question</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Undirected Graph</th>
<th colspan="2" align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Directed Graph</th>
</tr>
<tr>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"></th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Iterative Algorithm</th>
<th align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;">Recursive Algorithm</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">📌 TEMPLATE: Rotten Oranges</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">⚪</td>
<td align="center" style="text-align: center; padding: 10px; border: 1px solid #ddd;"><a href="https://www.youtube.com/watch?v=53hu28rQN74&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=32">logic</a> / <a href="https://www.youtube.com/watch?v=xGiH8gN9x2g&list=PL_z_8CaSLPWcn5bKG8UMI0St2D5EmQszx&index=33">code</a></td>
<td align="center" style="text-align: center; padding: 10px; border: 3px solid #000; font-weight: bold;">⚪</td>

</tbody>
</table>
Here we cannot use DFS since only BFS gives SSSP.



